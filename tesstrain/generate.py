# (C) Copyright 2014, Google Inc.
# (C) Copyright 2018, James R Barlow
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Utility for generating the various files.

For a detailed description of the phases, see
https://tesseract-ocr.github.io/tessdoc/Training-Tesseract.html.
"""

from __future__ import annotations

import concurrent.futures
import logging
import os
import pathlib
import shutil
import subprocess
import sys
from operator import itemgetter
from typing import cast, Any, Dict, Generator, List, NoReturn, Optional, TYPE_CHECKING, Union

from tqdm import tqdm

if TYPE_CHECKING:
    from tesstrain.arguments import TrainingArguments
from tesstrain.language_specific import VERTICAL_FONTS

log = logging.getLogger(__name__)


def err_exit(msg: str) -> NoReturn:
    """
    Exit the application with exit code 1.

    :param msg: The message to log before the exit.
    """
    log.critical(msg)
    sys.exit(1)


def run_command(cmd: str, *args: Union[str, pathlib.Path], env: Optional[Dict[str, Any]] = None) -> None:
    """
    Helper function to run a command and append its output to a log. Aborts early if
    the program file is not found.

    :param cmd: Binary to use.
    :param args: Arguments to pass.
    :param env: Environment variables to use.
    """
    for d in ("", "api/", "training/"):
        testcmd = f"{d}{cmd}"
        if shutil.which(testcmd):
            cmd = testcmd
            break
    if not shutil.which(cmd):
        err_exit(f"{cmd} not found")

    log.debug(f"Running {cmd}")
    args_list = list(args)
    for idx, arg in enumerate(args_list):
        log.debug(arg)
        # Workaround for https://bugs.python.org/issue33617
        # TypeError: argument of type 'WindowsPath' is not iterable
        if isinstance(arg, pathlib.WindowsPath):
            args_list[idx] = str(arg)

    proc = subprocess.run(
        [cmd, *args_list], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env
    )
    proclog = logging.getLogger(cmd)
    if proc.returncode == 0:
        proclog.debug(proc.stdout.decode("utf-8", errors="replace"))
    else:
        try:
            proclog.error(proc.stdout.decode("utf-8", errors="replace"))
        except Exception as e:
            proclog.error(e)
        err_exit(f"Program {cmd} failed with return code {proc.returncode}. Abort.")


def check_file_readable(*filenames: Union[str, pathlib.Path]) -> bool:
    """
    Check if all the given files exist, or exit otherwise.

    Used to check required input files and produced output files in each phase.

    :param filenames: The filenames to check.
    :return: Whether all files exist.
    """
    if isinstance(filenames, (str, pathlib.Path)):
        filenames = [filenames]
    for filename in filenames:
        try:
            with pathlib.Path(filename).open():
                pass
        except FileNotFoundError:
            err_exit(f"Required/expected file '{filename}' does not exist")
        except PermissionError:
            err_exit(f"{filename} is not readable")
        except IOError as e:
            err_exit(f"{filename} IO Error: {str(e)}")
    return True


def cleanup(ctx: TrainingArguments) -> None:
    """
    Move the log file to the output directory and remove the training directory.

    :param ctx: The run configuration.
    """
    if os.path.exists(ctx.log_file):
        shutil.copy(ctx.log_file, ctx.output_dir)
    shutil.rmtree(ctx.training_dir)


def initialize_fontconfig(ctx: TrainingArguments) -> None:
    """
    Initialize the font configuration with a unique font cache directory.

    :param ctx: The run configuration.
    """
    sample_path = pathlib.Path(ctx.font_config_cache) / "sample_text.txt"
    pathlib.Path(sample_path).write_text("Text\n")
    log.info(f"Testing font: {ctx.fonts[0]}")
    run_command(
        "text2image",
        f"--fonts_dir={ctx.fonts_dir}",
        f"--font={ctx.fonts[0]}",
        f"--outputbase={sample_path}",
        f"--text={sample_path}",
        f"--fontconfig_tmpdir={ctx.font_config_cache}",
        f"--ptsize={ctx.ptsize}",
    )


def make_fontname(font: str) -> str:
    """
    Convert the font name to one without special characters.

    :param font: The name to convert.
    :return: The converted name.
    """
    return font.replace(" ", "_").replace(",", "")


def make_outbase(ctx: TrainingArguments, fontname: str, exposure: int) -> pathlib.Path:
    """
    Generate the base output path.

    :param ctx: The run configuration.
    :param fontname: The name of the font to train.
    :param exposure: The current exposure value.
    :return: The generated path.
    """
    return pathlib.Path(ctx.training_dir) / f"{ctx.lang_code}.{fontname}.exp{exposure}"


def generate_font_image(
        ctx: TrainingArguments, font: str, exposure: int, char_spacing: float
) -> str:
    """
    Helper function for `phaseI_generate_image`.

    Generates the image for a single language/font combination in a way that can be run
    in parallel.

    :param ctx: The run configuration.
    :param font: The name of the font to use.
    :param exposure: The exposure value to use.
    :param char_spacing: The character spacing to use.
    :return: A corresponding identifier.
    """
    log.info(f"Rendering using {font}")
    fontname = make_fontname(font)
    outbase = make_outbase(ctx, fontname, exposure)

    common_args = [
        f"--fontconfig_tmpdir={ctx.font_config_cache}",
        f"--fonts_dir={ctx.fonts_dir}",
        f"--strip_unrenderable_words",
        f"--leading={ctx.leading}",
        f"--char_spacing={char_spacing}",
        f"--exposure={exposure}",
        f"--outputbase={outbase}",
        f"--max_pages={ctx.max_pages}",
    ]

    if ctx.distort_image:
        common_args.append("--distort_image")

    # add --writing_mode=vertical-upright to common_args if the font is
    # specified to be rendered vertically.
    vertical_fonts = ctx.vertical_fonts or VERTICAL_FONTS
    if font in vertical_fonts:
        common_args.append("--writing_mode=vertical-upright")

    run_command(
        "text2image",
        *common_args,
        f"--font={font}",
        f"--text={ctx.training_text}",
        f"--ptsize={ctx.ptsize}",
        *ctx.text2image_extra_args,
    )

    check_file_readable(str(outbase) + ".box", str(outbase) + ".tif")

    if ctx.extract_font_properties and pathlib.Path(ctx.train_ngrams_file).exists():
        log.info(f"Extracting font properties of {font}")
        run_command(
            "text2image",
            *common_args,
            f"--font={font}",
            f"--ligatures=false",
            f"--text={ctx.train_ngrams_file}",
            f"--only_extract_font_properties",
            f"--ptsize=32",
        )
        check_file_readable(str(outbase) + ".fontinfo")
    return f"{font}-{exposure}"


def phase_I_generate_image(ctx: TrainingArguments, par_factor: Optional[int] = None) -> None:
    """
    Phase I: Generate (I)mages from training text for each font.

    :param ctx: The run configuration.
    :param par_factor: Maximun number of workers.
    """
    if not par_factor or par_factor <= 0:
        par_factor = 1

    log.info("=== Phase I: Generating training images ===")
    check_file_readable(ctx.training_text)
    char_spacing = 0.0

    for exposure in ctx.exposures:
        if ctx.extract_font_properties and pathlib.Path(ctx.bigram_freqs_file).exists():
            # Parse .bigram_freqs file and compose a .train_ngrams file with text
            # for tesseract to recognize during training. Take only the ngrams whose
            # combined weight accounts for 95% of all the bigrams in the language.
            lines = pathlib.Path(ctx.bigram_freqs_file).read_text(encoding="utf-8").split("\n")
            records = [line.split() for line in lines]
            p = 0.99
            ngram_frac = p * sum(int(rec[1]) for rec in records if len(rec) >= 2)

            with open(ctx.train_ngrams_file, mode="w", encoding="utf-8") as fd:
                cumsum = 0
                for bigram, count in sorted(records, key=itemgetter(1), reverse=True):
                    if cumsum > ngram_frac:
                        break
                    fd.write(bigram + " ")
                    cumsum += int(count)

            check_file_readable(ctx.train_ngrams_file)

        with tqdm(
                total=len(ctx.fonts)
        ) as pbar, concurrent.futures.ThreadPoolExecutor(max_workers=par_factor) as executor:
            futures = [
                executor.submit(generate_font_image, ctx, font, exposure, char_spacing)
                for font in ctx.fonts
            ]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    err_exit("Failed while generating images " + str(exc))
                else:
                    pbar.update(1)

        # Check that each process was successful.
        for font in ctx.fonts:
            fontname = make_fontname(font)
            outbase = make_outbase(ctx, fontname, exposure)
            check_file_readable(str(outbase) + ".box", str(outbase) + ".tif")


def phase_UP_generate_unicharset(ctx: TrainingArguments) -> None:
    """
    Phase UP: Generate (U)nicharset and (P)roperties file.

    :param ctx: The run configuration.
    """
    log.info("=== Phase UP: Generating unicharset and unichar properties files ===")

    box_files = pathlib.Path(ctx.training_dir).glob("*.box")

    ctx.unicharset_file = pathlib.Path(ctx.training_dir) / f"{ctx.lang_code}.unicharset"

    run_command(
        "unicharset_extractor",
        "--output_unicharset",
        f"{ctx.unicharset_file}",
        "--norm_mode",
        f"{ctx.norm_mode}",
        *box_files,
    )
    check_file_readable(ctx.unicharset_file)

    ctx.xheights_file = pathlib.Path(ctx.training_dir) / f"{ctx.lang_code}.xheights"
    run_command(
        "set_unicharset_properties",
        "-U",
        f"{ctx.unicharset_file}",
        "-O",
        f"{ctx.unicharset_file}",
        "-X",
        f"{ctx.xheights_file}",
        f"--script_dir={ctx.langdata_dir}",
    )
    check_file_readable(ctx.xheights_file)


def phase_E_extract_features(ctx: TrainingArguments, box_config: List[str], ext: str) -> None:
    """
    Phase E: (E)xtract .tr feature files from .tif/.box files.

    :param ctx: The run configuration.
    :param box_config: The box configuration values.
    """
    log.info(f"=== Phase E: Generating {ext} files ===")

    img_files = list(pathlib.Path(ctx.training_dir).glob("*.exp*.tif"))
    log.debug(img_files)

    # Use any available language-specific configs.
    config: List[str] = []
    testconfig = pathlib.Path(ctx.langdata_dir) / ctx.lang_code / f"{ctx.lang_code}.config"
    if testconfig.exists():
        config = [str(testconfig)]
        log.info(f"Using {ctx.lang_code}.config")

    tessdata_environ = os.environ.copy()
    tessdata_environ["TESSDATA_PREFIX"] = str(ctx.tessdata_dir)

    log.info(f"Using TESSDATA_PREFIX={tessdata_environ['TESSDATA_PREFIX']}")

    with tqdm(total=len(img_files)) as pbar, concurrent.futures.ThreadPoolExecutor(
            max_workers=2
    ) as executor:
        futures = []
        for img_file in img_files:
            future = executor.submit(
                run_command,
                "tesseract",
                img_file,
                pathlib.Path(img_file).with_suffix(""),
                *box_config,
                *config,
                env=tessdata_environ,
            )
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                err_exit("Failed while extracting features: " + str(exc))
            else:
                pbar.update(1)
    # Check that all the output files were produced.
    for img_file in img_files:
        check_file_readable(pathlib.Path(img_file.with_suffix("." + ext)))


def make_lstmdata(ctx: TrainingArguments) -> None:
    """
    Construct LSTM training data.
    """
    log.info("=== Constructing LSTM training data ===")
    lang_prefix = f"{ctx.langdata_dir}/{ctx.lang_code}/{ctx.lang_code}"
    path_output = pathlib.Path(ctx.output_dir)
    if not path_output.is_dir():
        log.info(f"Creating new directory {ctx.output_dir}")
        path_output.mkdir(exist_ok=True, parents=True)

    args = []
    if ctx.lang_is_rtl:
        args.append("--lang_is_rtl")
    if ctx.norm_mode >= 2:
        args.append("--pass_through_recoder")

    # Build the starter traineddata from the inputs.
    run_command(
        "combine_lang_model",
        "--input_unicharset",
        f"{ctx.training_dir}/{ctx.lang_code}.unicharset",
        "--script_dir",
        f"{ctx.langdata_dir}",
        "--words",
        f"{lang_prefix}.wordlist",
        "--numbers",
        f"{lang_prefix}.numbers",
        "--puncs",
        f"{lang_prefix}.punc",
        "--output_dir",
        f"{ctx.output_dir}",
        "--lang",
        f"{ctx.lang_code}",
        *args,
    )

    def get_file_list() -> Generator[pathlib.Path, None, None]:
        training_path = pathlib.Path(ctx.training_dir)
        if ctx.save_box_tiff:
            log.info("=== Saving box/tiff pairs for training data ===")
            yield from training_path.glob(f"{ctx.lang_code}*.box")
            yield from training_path.glob(f"{ctx.lang_code}*.tif")
        log.info("=== Moving lstmf files for training data ===")
        yield from training_path.glob(f"{ctx.lang_code}.*.lstmf")

    for f in get_file_list():
        log.debug(f"Moving {f} to {path_output / f.name}")
        shutil.move(str(f), path_output / f.name)

    lstm_list = f"{ctx.output_dir}/{ctx.lang_code}.training_files.txt"
    dir_listing = (str(p) for p in path_output.glob(f"{ctx.lang_code}.*.lstmf"))
    with open(lstm_list, mode="w", encoding="utf-8", newline="\n") as fd:
        fd.write("\n".join(dir_listing))
