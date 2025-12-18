import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import mkdtemp, TemporaryDirectory
from unittest import TestCase

from requests import Session

from tesstrain import wrapper


def download(urls: list[str], paths: list[Path]) -> None:
    with Session() as session:
        for url, path in zip(urls, paths):
            response = session.get(url)
            response.raise_for_status()
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            path.write_bytes(response.content)


class SmokeTestCase(TestCase):
    data_directory: Path

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.data_directory = Path(mkdtemp())
        cls.addClassCleanup(shutil.rmtree, cls.data_directory)
        download(
            urls=[
                "https://github.com/tesseract-ocr/tessdata_best/raw/e12c65a915945e4c28e237a9b52bc4a8f39a0cec/eng.traineddata",
                "https://github.com/tesseract-ocr/tessconfigs/raw/3decf1c8252ba6dbeef0bf908f4b0aab7f18d113/configs/lstm.train",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/Latin.unicharset",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/Latin.xheights",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/radical-stroke.txt",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/desired_characters",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.numbers",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.punc",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.singles_text",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.training_text",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.unicharambigs",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.unicharset",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/eng.wordlist",
                "https://github.com/tesseract-ocr/langdata_lstm/raw/07930fd9f246622c26eb5de794d9212ceac432d3/eng/okfonts.txt",
            ],
            paths=[
                cls.data_directory / "tessdata" / "eng.traineddata",
                cls.data_directory / "tessdata" / "configs" / "lstm.train",
                cls.data_directory / "langdata_lstm" / "Latin.unicharset",
                cls.data_directory / "langdata_lstm" / "Latin.xheights",
                cls.data_directory / "langdata_lstm" / "radical-stroke.txt",
                cls.data_directory / "langdata_lstm" / "eng" / "desired_characters",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.numbers",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.punc",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.singles_text",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.training_text",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.unicharambigs",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.unicharset",
                cls.data_directory / "langdata_lstm" / "eng" / "eng.wordlist",
                cls.data_directory / "langdata_lstm" / "eng" / "okfonts.txt",
            ]
        )

    def assert_files(self, tmpdir: str, output_dir: str, with_log_file: bool) -> None:
        self.assertSetEqual(
            set(),
            set(Path(tmpdir).rglob("*"))
        )

        output_path = Path(output_dir)
        expected_paths = {
            output_path / "eng" / "eng.charset_size=110.txt",
            output_path / "eng" / "eng.traineddata",
            output_path / "eng" / "eng.unicharset",
            output_path / "eng",
            output_path / "eng.DejaVu_Sans_Regular.exp0.lstmf",
            output_path / "eng.Roboto.exp0.lstmf",
            output_path / "eng.training_files.txt",
        }
        if with_log_file:
            expected_paths.add(output_path / "tesstrain.log")
        self.assertSetEqual(
            expected_paths,
            set(output_path.rglob("*"))
        )

    def test_subprocess_call(self) -> None:
        with TemporaryDirectory() as tmpdir, TemporaryDirectory() as output_dir:
            result = subprocess.run(
                [
                    sys.executable, "-m", "tesstrain",
                    "--langdata_dir", self.data_directory / "langdata_lstm",
                    "--tessdata_dir", self.data_directory / "tessdata",
                    "--linedata_only",
                    "--lang", "eng",
                    "--tmp_dir", tmpdir,
                    "--fontlist", "Roboto", "DejaVu Sans Regular",
                    "--maxpages", "2",
                    "--output_dir", output_dir,
                ],
                # capture_output=True,
                # text=True,
            )

            self.assertEqual(0, result.returncode, result)
            self.assert_files(tmpdir, output_dir, with_log_file=True)

    def test_from_python(self) -> None:
        with TemporaryDirectory() as tmpdir, TemporaryDirectory() as output_dir:
            result = wrapper.run(
                langdata_directory=str(self.data_directory / "langdata_lstm"),
                tessdata_directory=str(self.data_directory / "tessdata"),
                linedata_only=True,
                language_code="eng",
                temporary_directory=tmpdir,
                fonts=["Roboto", "DejaVu Sans Regular"],
                maximum_pages=2,
                output_directory=output_dir,
            )

            self.assertEqual(0, result)
            self.assert_files(tmpdir, output_dir, with_log_file=False)
