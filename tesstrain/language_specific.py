# (C) Copyright 2014, Google Inc.
# (C) Copyright 2018, James R Barlow
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Set some language specific variables.
"""

from __future__ import annotations

import itertools
import logging
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tesstrain.arguments import TrainingArguments

log = logging.getLogger(__name__)
del logging

# Array of all valid language codes.
VALID_LANGUAGE_CODES: str = (
    "afr amh ara asm aze aze_cyrl bel ben bih bod bos bul cat "
    "ceb ces chi_sim chi_tra chr cym cyr_lid dan deu div dzo "
    "ell eng enm epo est eus fas fil fin fra frk frm gle glg "
    "grc guj hat heb hin hrv hun hye iast iku ind isl ita ita_old "
    "jav jav_java jpn kan kat kat_old kaz khm kir kmr kor kur_ara lao lat "
    "lat_lid lav lit mal mar mkd mlt msa mya nep nld nor ori "
    "pan pol por pus ron rus san sin slk slv snd spa spa_old "
    "sqi srp srp_latn swa swe syr tam tel tgk tgl tha tir tur "
    "uig ukr urd uzb uzb_cyrl vie yid gle_uncial deu_latf"
)

# Codes for which we have webtext but no fonts:
UNUSABLE_LANGUAGE_CODES: str = ""

FRAKTUR_FONTS: list[str] = [
    "CaslonishFraxx Medium",
    "Cloister Black, Light",
    "Proclamate Light",
    "UnifrakturMaguntia",
    "Walbaum-Fraktur",
]

# List of fonts to train on
LATIN_FONTS: list[str] = [
    "Arial Bold",
    "Arial Bold Italic",
    "Arial Italic",
    "Arial",
    "Courier New Bold",
    "Courier New Bold Italic",
    "Courier New Italic",
    "Courier New",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Times New Roman,",
    "Georgia Bold",
    "Georgia Italic",
    "Georgia",
    "Georgia Bold Italic",
    "Trebuchet MS Bold",
    "Trebuchet MS Bold Italic",
    "Trebuchet MS Italic",
    "Trebuchet MS",
    "Verdana Bold",
    "Verdana Italic",
    "Verdana",
    "Verdana Bold Italic",
    "Tex Gyre Bonum Bold",
    "Tex Gyre Bonum Italic",
    "Tex Gyre Bonum Bold Italic",
    "Tex Gyre Schola Bold",
    "Tex Gyre Schola Italic",
    "Tex Gyre Schola Bold Italic",
    "Tex Gyre Schola Regular",
    "DejaVu Sans Ultra-Light",
]

# List of fonts for printed/neo-Latin ('lat' language code, different from Latin script)
NEOLATIN_FONTS: list[str] = [
    "GFS Bodoni",
    "GFS Bodoni Bold",
    "GFS Bodoni Italic",
    "GFS Bodoni Bold Italic",
    "GFS Didot",
    "GFS Didot Bold",
    "GFS Didot Italic",
    "GFS Didot Bold Italic",
    "Cardo",
    "Cardo Bold",
    "Cardo Italic",
    "Wyld",
    "Wyld Italic",
    "EB Garamond",
    "EB Garamond Italic",
    "Junicode",
    "Junicode Bold",
    "Junicode Italic",
    "Junicode Bold Italic",
    "IM FELL DW Pica PRO",
    "IM FELL English PRO",
    "IM FELL Double Pica PRO",
    "IM FELL French Canon PRO",
    "IM FELL Great Primer PRO",
    "IM FELL DW Pica PRO Italic",
    "IM FELL English PRO Italic",
    "IM FELL Double Pica PRO Italic",
    "IM FELL French Canon PRO Italic",
    "IM FELL Great Primer PRO Italic",
]

IRISH_UNCIAL_FONTS: list[str] = [
    "Bunchlo Arsa Dubh GC",
    "Bunchlo Arsa GC",
    "Bunchlo Arsa GC Bold",
    "Bunchlo Dubh GC",
    "Bunchlo GC",
    "Bunchlo GC Bold",
    "Bunchlo Nua GC Bold",
    "Bunchló na Nod GC",
    "Gadelica",
    "Glanchlo Dubh GC",
    "Glanchlo GC",
    "Glanchlo GC Bold",
    "Seanchló Dubh GC",
    "Seanchló GC",
    "Seanchló GC Bold",
    "Seanchló na Nod GC",
    "Seanchló Ársa Dubh GC",
    "Seanchló Ársa GC",
    "Seanchló Ársa GC Bold",
    "Tromchlo Beag GC",
    "Tromchlo Mor GC",
    "Urchlo GC",
    "Urchlo GC Bold",
]

EARLY_LATIN_FONTS: list[str] = [
    *FRAKTUR_FONTS,
    *LATIN_FONTS,
    # The Wyld font family renders early modern ligatures encoded in the private
    # unicode area.
    "Wyld",
    "Wyld Italic",
    # Fonts that render the Yogh symbol (U+021C, U+021D) found in Old English.
    "GentiumAlt",
]

VIETNAMESE_FONTS: list[str] = [
    "Arial Unicode MS Bold",
    "Arial Bold Italic",
    "Arial Italic",
    "Arial Unicode MS",
    "FreeMono Bold",
    "Courier New Bold Italic",
    "FreeMono Italic",
    "FreeMono",
    "GentiumAlt Italic",
    "GentiumAlt",
    "Palatino Linotype Bold",
    "Palatino Linotype Bold Italic",
    "Palatino Linotype Italic",
    "Palatino Linotype",
    "Really No 2 LT W2G Light",
    "Really No 2 LT W2G Light Italic",
    "Really No 2 LT W2G Medium",
    "Really No 2 LT W2G Medium Italic",
    "Really No 2 LT W2G Semi-Bold",
    "Really No 2 LT W2G Semi-Bold Italic",
    "Really No 2 LT W2G Ultra-Bold",
    "Really No 2 LT W2G Ultra-Bold Italic",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Times New Roman,",
    "Verdana Bold",
    "Verdana Italic",
    "Verdana",
    "Verdana Bold Italic",
    "VL Gothic",
    "VL PGothic",
]

DEVANAGARI_FONTS: list[str] = [
    "FreeSans",
    "Chandas",
    "Kalimati",
    "Uttara",
    "Lucida Sans",
    "gargi Medium",
    "Lohit Devanagari",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Noto Sans Devanagari Bold",
    "Noto Sans Devanagari",
    "Samyak Devanagari Medium",
    "Sarai",
    "Saral LT Bold",
    "Saral LT Light",
    "Nakula",
    "Sahadeva",
    "Samanata",
    "Santipur OT Medium",
]

KANNADA_FONTS: list[str] = [
    "Kedage Bold",
    "Kedage Italic",
    "Kedage",
    "Kedage Bold Italic",
    "Mallige Bold",
    "Mallige Italic",
    "Mallige",
    "Mallige Bold Italic",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "cheluvi Medium",
    "Noto Sans Kannada Bold",
    "Noto Sans Kannada",
    "Lohit Kannada",
    "Tunga",
    "Tunga Bold",
]

TELUGU_FONTS: list[str] = [
    "Pothana2000",
    "Vemana2000",
    "Lohit Telugu",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Dhurjati",
    "Gautami Bold",
    "Gidugu",
    "Gurajada",
    "Lakki Reddy",
    "Mallanna",
    "Mandali",
    "NATS",
    "NTR",
    "Noto Sans Telugu Bold",
    "Noto Sans Telugu",
    "Peddana",
    "Ponnala",
    "Ramabhadra",
    "Ravi Prakash",
    "Sree Krushnadevaraya",
    "Suranna",
    "Suravaram",
    "Tenali Ramakrishna",
    "Gautami",
]

TAMIL_FONTS: list[str] = [
    "TAMu_Kadambri",
    "TAMu_Kalyani",
    "TAMu_Maduram",
    "TSCu_Paranar",
    "TSCu_Times",
    "TSCu_Paranar Bold",
    "FreeSans",
    "FreeSerif",
    "Lohit Tamil",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Droid Sans Tamil Bold",
    "Droid Sans Tamil",
    "Karla Tamil Inclined Bold Italic",
    "Karla Tamil Inclined Italic",
    "Karla Tamil Upright Bold",
    "Karla Tamil Upright",
    "Noto Sans Tamil Bold",
    "Noto Sans Tamil",
    "Noto Sans Tamil UI Bold",
    "Noto Sans Tamil UI",
    "TSCu_Comic Normal",
    "Lohit Tamil Classical",
]

THAI_FONTS: list[str] = [
    "FreeSerif",
    "FreeSerif Italic",
    "Garuda",
    "Norasi",
    "Lucida Sans Typewriter",
    "Lucida Sans",
    "Garuda Oblique",
    "Norasi Oblique",
    "Norasi Italic",
    "Garuda Bold",
    "Norasi Bold",
    "Lucida Sans Typewriter Bold",
    "Lucida Sans Semi-Bold",
    "Garuda Bold Oblique",
    "Norasi Bold Italic",
    "Norasi Bold Oblique",
    "AnuParp LT Thai",
    "Arial Unicode MS Bold",
    "Arial Unicode MS",
    "Ascender Uni",
    "Loma",
    "Noto Serif Thai Bold",
    "Noto Serif Thai",
    "Purisa Light",
    "Sirichana LT Bold",
    "Sirichana LT",
    "Sukothai LT Bold",
    "Sukothai LT",
    "UtSaHaGumm LT Thai",
    "Tahoma",
]

KOREAN_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Baekmuk Batang Patched",
    "Baekmuk Batang",
    "Baekmuk Dotum",
    "Baekmuk Gulim",
    "Baekmuk Headline",
]

CHI_SIM_FONTS: list[str] = [
    "AR PL UKai CN",
    "AR PL UMing Patched Light",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "WenQuanYi Zen Hei Medium",
]

CHI_TRA_FONTS: list[str] = [
    "AR PL UKai TW",
    "AR PL UMing TW MBE Light",
    "AR PL UKai Patched",
    "AR PL UMing Patched Light",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "WenQuanYi Zen Hei Medium",
]

JPN_FONTS: list[str] = [
    "TakaoExGothic",
    "TakaoExMincho",
    "TakaoGothic",
    "TakaoMincho",
    "TakaoPGothic",
    "TakaoPMincho",
    "VL Gothic",
    "VL PGothic",
    "Noto Sans Japanese Bold",
    "Noto Sans Japanese Light",
]

RUSSIAN_FONTS: list[str] = [
    "Arial Bold",
    "Arial Bold Italic",
    "Arial Italic",
    "Arial",
    "Courier New Bold",
    "Courier New Bold Italic",
    "Courier New Italic",
    "Courier New",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Times New Roman,",
    "Georgia Bold",
    "Georgia Italic",
    "Georgia",
    "Georgia Bold Italic",
    "Trebuchet MS Bold",
    "Trebuchet MS Bold Italic",
    "Trebuchet MS Italic",
    "Trebuchet MS",
    "Verdana Bold",
    "Verdana Italic",
    "Verdana",
    "Verdana Bold Italic",
    "DejaVu Serif",
    "DejaVu Serif Oblique",
    "DejaVu Serif Bold",
    "DejaVu Serif Bold Oblique",
    "Lucida Bright",
    "FreeSerif Bold",
    "FreeSerif Bold Italic",
    "DejaVu Sans Ultra-Light",
]

GREEK_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "DejaVu Sans Mono",
    "DejaVu Sans Mono Oblique",
    "DejaVu Sans Mono Bold",
    "DejaVu Sans Mono Bold Oblique",
    "DejaVu Serif",
    "DejaVu Serif Semi-Condensed",
    "DejaVu Serif Oblique",
    "DejaVu Serif Bold",
    "DejaVu Serif Bold Oblique",
    "DejaVu Serif Bold Semi-Condensed",
    "FreeSerif Bold",
    "FreeSerif Bold Italic",
    "FreeSerif Italic",
    "FreeSerif",
    "GentiumAlt",
    "GentiumAlt Italic",
    "Linux Biolinum O Bold",
    "Linux Biolinum O",
    "Linux Libertine O Bold",
    "Linux Libertine O",
    "Linux Libertine O Bold Italic",
    "Linux Libertine O Italic",
    "Palatino Linotype Bold",
    "Palatino Linotype Bold Italic",
    "Palatino Linotype Italic",
    "Palatino Linotype",
    "UmePlus P Gothic",
    "VL PGothic",
]

ANCIENT_GREEK_FONTS: list[str] = [
    "GFS Artemisia",
    "GFS Artemisia Bold",
    "GFS Artemisia Bold Italic",
    "GFS Artemisia Italic",
    "GFS Bodoni",
    "GFS Bodoni Bold",
    "GFS Bodoni Bold Italic",
    "GFS Bodoni Italic",
    "GFS Didot",
    "GFS Didot Bold",
    "GFS Didot Bold Italic",
    "GFS Didot Italic",
    "GFS DidotClassic",
    "GFS Neohellenic",
    "GFS Neohellenic Bold",
    "GFS Neohellenic Bold Italic",
    "GFS Neohellenic Italic",
    "GFS Philostratos",
    "GFS Porson",
    "GFS Pyrsos",
    "GFS Solomos",
]

ARABIC_FONTS: list[str] = [
    "Arabic Transparent Bold",
    "Arabic Transparent",
    "Arab",
    "Arial Unicode MS Bold",
    "Arial Unicode MS",
    "ASVCodar LT Bold",
    "ASVCodar LT Light",
    "Badiya LT Bold",
    "Badiya LT",
    "Badr LT Bold",
    "Badr LT",
    "Dimnah",
    "Frutiger LT Arabic Bold",
    "Frutiger LT Arabic",
    "Furat",
    "Hassan LT Bold",
    "Hassan LT Light",
    "Jalal LT Bold",
    "Jalal LT Light",
    "Midan Bold",
    "Midan",
    "Mitra LT Bold",
    "Mitra LT Light",
    "Palatino LT Arabic",
    "Palatino Sans Arabic Bold",
    "Palatino Sans Arabic",
    "Simplified Arabic Bold",
    "Simplified Arabic",
    "Times New Roman, Bold",
    "Times New Roman,",
    "Traditional Arabic Bold",
    "Traditional Arabic",
]

HEBREW_FONTS: list[str] = [
    "Arial Bold",
    "Arial Bold Italic",
    "Arial Italic",
    "Arial",
    "Courier New Bold",
    "Courier New Bold Italic",
    "Courier New Italic",
    "Courier New",
    "Ergo Hebrew Semi-Bold",
    "Ergo Hebrew Semi-Bold Italic",
    "Ergo Hebrew",
    "Ergo Hebrew Italic",
    "Really No 2 LT W2G Light",
    "Really No 2 LT W2G Light Italic",
    "Really No 2 LT W2G Medium",
    "Really No 2 LT W2G Medium Italic",
    "Really No 2 LT W2G Semi-Bold",
    "Really No 2 LT W2G Semi-Bold Italic",
    "Really No 2 LT W2G Ultra-Bold",
    "Really No 2 LT W2G Ultra-Bold Italic",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Times New Roman,",
    "Lucida Sans",
    "Tahoma",
]

BENGALI_FONTS: list[str] = [
    "Bangla Medium",
    "Lohit Bengali",
    "Mukti Narrow",
    "Mukti Narrow Bold",
    "Jamrul Medium Semi-Expanded",
    "Likhan Medium",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "FreeSans",
    "FreeSans Oblique",
    "FreeSerif",
    "FreeSerif Italic",
    "Noto Sans Bengali Bold",
    "Noto Sans Bengali",
    "Ani",
    "Lohit Assamese",
    "Lohit Bengali",
    "Mitra Mono",
]

KYRGYZ_FONTS: list[str] = [
    "Arial",
    "Arial Bold",
    "Arial Italic",
    "Arial Bold Italic",
    "Courier New",
    "Courier New Bold",
    "Courier New Italic",
    "Courier New Bold Italic",
    "Times New Roman,",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "DejaVu Serif",
    "DejaVu Serif Oblique",
    "DejaVu Serif Bold",
    "DejaVu Serif Bold Oblique",
    "Lucida Bright",
    "FreeSerif Bold",
    "FreeSerif Bold Italic",
]

PERSIAN_FONTS: list[str] = [
    "Amiri Bold Italic",
    "Amiri Bold",
    "Amiri Italic",
    "Amiri",
    "Andale Sans Arabic Farsi",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Lateef",
    "Lucida Bright",
    "Lucida Sans Oblique",
    "Lucida Sans Semi-Bold",
    "Lucida Sans",
    "Lucida Sans Typewriter Bold",
    "Lucida Sans Typewriter Oblique",
    "Lucida Sans Typewriter",
    "Scheherazade",
    "Tahoma",
    "Times New Roman,",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Yakout Linotype Bold",
    "Yakout Linotype",
]

AMHARIC_FONTS: list[str] = [
    "Abyssinica SIL",
    "Droid Sans Ethiopic Bold",
    "Droid Sans Ethiopic",
    "FreeSerif",
    "Noto Sans Ethiopic Bold",
    "Noto Sans Ethiopic",
]

ARMENIAN_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "FreeMono",
    "FreeMono Italic",
    "FreeSans",
    "FreeSans Bold",
    "FreeSans Oblique",
]

BURMESE_FONTS: list[str] = [
    "Myanmar Sans Pro",
    "Noto Sans Myanmar Bold",
    "Noto Sans Myanmar",
    "Padauk Bold",
    "Padauk",
    "TharLon",
]

JAVANESE_FONTS: list[str] = ["Prada"]

NORTH_AMERICAN_ABORIGINAL_FONTS: list[str] = [
    "Aboriginal Sans",
    "Aboriginal Sans Bold Italic",
    "Aboriginal Sans Italic",
    "Aboriginal Sans Bold",
    "Aboriginal Serif Bold",
    "Aboriginal Serif Bold Italic",
    "Aboriginal Serif Italic",
    "Aboriginal Serif",
]

GEORGIAN_FONTS: list[str] = [
    "Arial Unicode MS Bold",
    "Arial Unicode MS",
    r"BPG Algeti GPL\&GNU",
    r"BPG Chveulebrivi GPL\&GNU",
    r"BPG Courier GPL\&GNU",
    r"BPG Courier S GPL\&GNU",
    "BPG DejaVu Sans 2011 GNU-GPL",
    r"BPG Elite GPL\&GNU",
    r"BPG Excelsior GPL\&GNU",
    r"BPG Glaho GPL\&GNU",
    r"BPG Gorda GPL\&GNU",
    r"BPG Ingiri GPL\&GNU",
    r"BPG Mrgvlovani Caps GNU\&GPL",
    r"BPG Mrgvlovani GPL\&GNU",
    r"BPG Nateli Caps GPL\&GNU Light",
    r"BPG Nateli Condenced GPL\&GNU Light",
    r"BPG Nateli GPL\&GNU Light",
    r"BPG Nino Medium Cond GPL\&GNU",
    r"BPG Nino Medium GPL\&GNU Medium",
    r"BPG Sans GPL\&GNU",
    r"BPG Sans Medium GPL\&GNU",
    r"BPG Sans Modern GPL\&GNU",
    r"BPG Sans Regular GPL\&GNU",
    r"BPG Serif GPL\&GNU",
    r"BPG Serif Modern GPL\&GNU",
    "FreeMono",
    "FreeMono Bold Italic",
    "FreeSans",
    "FreeSerif",
    "FreeSerif Bold",
    "FreeSerif Bold Italic",
    "FreeSerif Italic",
]

OLD_GEORGIAN_FONTS: list[str] = [
    "Arial Unicode MS Bold",
    "Arial Unicode MS",
    r"BPG Algeti GPL\&GNU",
    r"BPG Courier S GPL\&GNU",
    "BPG DejaVu Sans 2011 GNU-GPL",
    r"BPG Elite GPL\&GNU",
    r"BPG Excelsior GPL\&GNU",
    r"BPG Glaho GPL\&GNU",
    r"BPG Ingiri GPL\&GNU",
    r"BPG Mrgvlovani Caps GNU\&GPL",
    r"BPG Mrgvlovani GPL\&GNU",
    r"BPG Nateli Caps GPL\&GNU Light",
    r"BPG Nateli Condenced GPL\&GNU Light",
    r"BPG Nateli GPL\&GNU Light",
    r"BPG Nino Medium Cond GPL\&GNU",
    r"BPG Nino Medium GPL\&GNU Medium",
    r"BPG Sans GPL\&GNU",
    r"BPG Sans Medium GPL\&GNU",
    r"BPG Sans Modern GPL\&GNU",
    r"BPG Sans Regular GPL\&GNU",
    r"BPG Serif GPL\&GNU",
    r"BPG Serif Modern GPL\&GNU",
    "FreeSans",
    "FreeSerif",
    "FreeSerif Bold",
    "FreeSerif Bold Italic",
    "FreeSerif Italic",
]

KHMER_FONTS: list[str] = [
    "Khmer OS",
    "Khmer OS System",
    "Khmer OS Battambang",
    "Khmer OS Bokor",
    "Khmer OS Content",
    "Khmer OS Fasthand",
    "Khmer OS Freehand",
    "Khmer OS Metal Chrieng",
    "Khmer OS Muol Light",
    "Khmer OS Muol Pali",
    "Khmer OS Muol",
    "Khmer OS Siemreap",
    "Noto Sans Bold",
    "Noto Sans",
    "Noto Serif Khmer Bold",
    "Noto Serif Khmer Light",
]

KURDISH_FONTS: list[str] = [
    "Amiri Bold Italic",
    "Amiri Bold",
    "Amiri Italic",
    "Amiri",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Lateef",
    "Lucida Bright",
    "Lucida Sans Oblique",
    "Lucida Sans Semi-Bold",
    "Lucida Sans",
    "Lucida Sans Typewriter Bold",
    "Lucida Sans Typewriter Oblique",
    "Lucida Sans Typewriter",
    "Scheherazade",
    "Tahoma",
    "Times New Roman,",
    "Times New Roman, Bold",
    "Times New Roman, Bold Italic",
    "Times New Roman, Italic",
    "Unikurd Web",
    "Yakout Linotype Bold",
    "Yakout Linotype",
]

LAOTHIAN_FONTS: list[str] = [
    "Phetsarath OT",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Dhyana Bold",
    "Dhyana",
    "Lao Muang Don",
    "Lao Muang Khong",
    "Lao Sans Pro",
    "Noto Sans Lao Bold",
    "Noto Sans Lao",
    "Noto Sans Lao UI Bold",
    "Noto Sans Lao UI",
    "Noto Serif Lao Bold",
    "Noto Serif Lao",
    "Phetsarath Bold",
    "Phetsarath",
    "Souliyo Unicode",
]

GUJARATI_FONTS: list[str] = [
    "Lohit Gujarati",
    "Rekha Medium",
    "Samyak Gujarati Medium",
    "aakar Medium",
    "padmaa Bold",
    "padmaa Medium",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "FreeSans",
    "Noto Sans Gujarati Bold",
    "Noto Sans Gujarati",
    "Shruti",
    "Shruti Bold",
]

MALAYALAM_FONTS: list[str] = [
    "AnjaliOldLipi",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Dyuthi",
    "FreeSerif",
    "Kalyani",
    "Kartika",
    "Kartika Bold",
    "Lohit Malayalam",
    "Meera",
    "Noto Sans Malayalam Bold",
    "Noto Sans Malayalam",
    "Rachana",
    "Rachana_w01",
    "RaghuMalayalam",
    "suruma",
]

ORIYA_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "ori1Uni Medium",
    "Samyak Oriya Medium",
    "Lohit Oriya",
]

PUNJABI_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "Saab",
    "Lohit Punjabi",
    "Noto Sans Gurmukhi",
    "Noto Sans Gurmukhi Bold",
    "FreeSans",
    "FreeSans Bold",
    "FreeSerif",
]

SINHALA_FONTS: list[str] = [
    "Noto Sans Sinhala Bold",
    "Noto Sans Sinhala",
    "OCRUnicode",
    "Yagpo",
    "LKLUG",
    "FreeSerif",
]

SYRIAC_FONTS: list[str] = [
    "East Syriac Adiabene",
    "East Syriac Ctesiphon",
    "Estrangelo Antioch",
    "Estrangelo Edessa",
    "Estrangelo Midyat",
    "Estrangelo Nisibin",
    "Estrangelo Quenneshrin",
    "Estrangelo Talada",
    "Estrangelo TurAbdin",
    "Serto Batnan Bold",
    "Serto Batnan",
    "Serto Jerusalem Bold",
    "Serto Jerusalem Italic",
    "Serto Jerusalem",
    "Serto Kharput",
    "Serto Malankara",
    "Serto Mardin Bold",
    "Serto Mardin",
    "Serto Urhoy Bold",
    "Serto Urhoy",
    "FreeSans",
]

THAANA_FONTS: list[str] = ["FreeSerif"]

TIBETAN_FONTS: list[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "DDC Uchen",
    "Jomolhari",
    "Kailasa",
    "Kokonor",
    "Tibetan Machine Uni",
    "TibetanTsugRing",
    "Yagpo",
]

# The following fonts will be rendered vertically in phase I.
VERTICAL_FONTS: list[str] = [
    "TakaoExGothic",
    "TakaoExMincho",
    "AR PL UKai Patched",
    "AR PL UMing Patched Light",
    "Baekmuk Batang Patched",
]

FLAGS_WEBTEXT_PREFIX: str = os.environ.get("FLAGS_webtext_prefix", "")


# TODO(dsl): We can refactor these into functions that assign FONTS,
# TEXT_CORPUS, etc. separately.
def set_lang_specific_parameters(ctx: TrainingArguments, lang: str) -> TrainingArguments:
    """
    Set language-specific values for several global variables, including

    * ``text_corpus``: Holds the text corpus file for the language.
      Used in phase F.
    * ``fonts``: Holds a sequence of applicable fonts for the language.
      Used in phase F & I. Only set if not already set.
    * ``training_data_arguments``: Character-code-specific filtering to
      distinguish between scripts (e.g. CJK) used by
      ``filter_forbidden_characters`` in phase F.
    * ``wordlist2dawg_arguments``: Specify fixed length DAWG generation
      for non-space-delimited language.

    :param ctx: The run configuration to update.
    :param lang: The language code.
    :return: THe updated run configuration.
    """
    # The default text location is now given directly from the language code.
    text_corpus: str = f"{FLAGS_WEBTEXT_PREFIX}/{lang}.corpus.txt"
    filter_arguments: list[str] = []
    wordlist2dawg_arguments: str = ""
    # These dawg factors represent the fraction of the corpus not covered by the
    # dawg, and seem like reasonable defaults, but the optimal value is likely
    # to be highly corpus-dependent, as well as somewhat language-dependent.
    # Number dawg factor is the fraction of all numeric strings that are not
    # covered, which is why it is higher relative to the others.
    punc_dawg_factor: float | None = None
    number_dawg_factor: float = 0.125
    word_dawg_factor: float = 0.05
    bigram_dawg_factor: float = 0.015
    training_data_arguments: list[str] = []
    fragments_disabled: str = "y"
    run_shape_clustering: bool = False
    ambigs_filter_denominator: str = "100000"
    leading: int = 32
    mean_count: int = 40  # Default for latin script.
    # Language to mix with the language for maximum accuracy. Defaults to eng.
    # If no language is good, set to the base language.
    mix_lang: str = "eng"
    fonts: list[str] = ctx.fonts
    text2image_extra_args: list[str] = []
    exposures: list[int] = list(map(int, itertools.chain(*ctx.exposures or [])))

    generate_word_bigrams: int | None = None
    word_dawg_size: int | None = None

    # Latin languages.
    if lang == "enm":
        text2image_extra_args += ["--ligatures"]  # Add ligatures when supported
        if not fonts:
            fonts = EARLY_LATIN_FONTS
    elif lang == "frm":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/fra.corpus.txt"
        # Make long-s substitutions for Middle French text
        filter_arguments += ["--make_early_language_variant=fra"]
        text2image_extra_args += ["--ligatures"]  # Add ligatures when supported.
        if not fonts:
            fonts = EARLY_LATIN_FONTS
    elif lang in {"frk", "deu_latf"}:
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/deu.corpus.txt"
        if not fonts:
            fonts = FRAKTUR_FONTS
    elif lang == "ita_old":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/ita.corpus.txt"
        # Make long-s substitutions for Early Italian text
        filter_arguments += ["--make_early_language_variant=ita"]
        text2image_extra_args += ["--ligatures"]  # Add ligatures when supported.
        if not fonts:
            fonts = EARLY_LATIN_FONTS
    elif lang == "lat":
        if not exposures:
            exposures = [-3, -2, -1, 0, 1, 2, 3]
        if not fonts:
            fonts = NEOLATIN_FONTS
    elif lang == "spa_old":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/spa.corpus.txt"
        # Make long-s substitutions for Early Spanish text
        filter_arguments += ["--make_early_language_variant=spa"]
        text2image_extra_args += ["--ligatures"]  # Add ligatures when supported.
        if not fonts:
            fonts = EARLY_LATIN_FONTS
    elif lang == "srp_latn":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/srp.corpus.txt"
    elif lang == "vie":
        training_data_arguments += ["--infrequent_ratio=10000"]
        if not fonts:
            fonts = VIETNAMESE_FONTS

    # Highly inflective languages get a bigger dawg size.
    # TODO(rays) Add more here!
    elif lang == "hun":
        word_dawg_size = 1_000_000
    elif lang == "pol":
        word_dawg_size = 1_000_000

    # Latin with default treatment.
    elif lang == "afr":
        pass
    elif lang == "aze":
        pass
    elif lang == "bos":
        pass
    elif lang == "cat":
        pass
    elif lang == "ceb":
        pass
    elif lang == "ces":
        punc_dawg_factor = 0.004
    elif lang == "cym":
        pass
    elif lang == "dan":
        pass
    elif lang == "deu":
        word_dawg_factor = 0.125
    elif lang == "eng":
        word_dawg_factor = 0.03
    elif lang == "epo":
        pass
    elif lang == "est":
        pass
    elif lang == "eus":
        pass
    elif lang == "fil":
        pass
    elif lang == "fin":
        pass
    elif lang == "fra":
        word_dawg_factor = 0.08
    elif lang == "gle":
        pass
    elif lang == "gle_uncial":
        if not fonts:
            fonts = IRISH_UNCIAL_FONTS
    elif lang == "glg":
        pass
    elif lang == "hat":
        pass
    elif lang == "hrv":
        pass
    elif lang == "iast":
        pass
    elif lang == "ind":
        pass
    elif lang == "isl":
        pass
    elif lang == "ita":
        pass
    elif lang == "jav":
        pass
    elif lang == "lav":
        pass
    elif lang == "lit":
        pass
    elif lang == "mlt":
        pass
    elif lang == "msa":
        pass
    elif lang == "nld":
        word_dawg_factor = 0.02
    elif lang == "nor":
        pass
    elif lang == "por":
        pass
    elif lang == "ron":
        pass
    elif lang == "slk":
        pass
    elif lang == "slv":
        pass
    elif lang == "spa":
        pass
    elif lang == "sqi":
        pass
    elif lang == "swa":
        pass
    elif lang == "swe":
        pass
    elif lang == "tgl":
        pass
    elif lang == "tur":
        pass
    elif lang == "uzb":
        pass
    elif lang == "zlm":
        pass

    # Special code for performing language-id that is trained on
    # EFIGS+Latin+Vietnamese text with regular + fraktur fonts.
    elif lang == "lat_lid":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/lat_lid.corpus.txt"
        training_data_arguments += ["--infrequent_ratio=10000"]
        generate_word_bigrams = 0
        # Strip unrenderable words as not all fonts will render the extended
        # latin symbols found in Vietnamese text.
        word_dawg_size = 1_000_000
        if not fonts:
            fonts = EARLY_LATIN_FONTS

    # Cyrillic script-based languages. It is bad to mix Latin with Cyrillic.
    elif lang == "rus":
        if not fonts:
            fonts = RUSSIAN_FONTS
        mix_lang = "rus"
        number_dawg_factor = 0.05
        word_dawg_size = 1_000_000
    elif lang in (
            "aze_cyrl",
            "bel",
            "bul",
            "kaz",
            "mkd",
            "srp",
            "tgk",
            "ukr",
            "uzb_cyrl",
    ):
        mix_lang = f"{lang}"
        if not fonts:
            fonts = RUSSIAN_FONTS

    # Special code for performing Cyrillic language-id that is trained on
    # Russian, Serbian, Ukrainian, Belarusian, Macedonian, Tajik and Mongolian
    # text with the list of Russian fonts.
    elif lang == "cyr_lid":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/cyr_lid.corpus.txt"
        training_data_arguments += ["--infrequent_ratio=10000"]
        generate_word_bigrams = 0
        word_dawg_size = 1_000_000
        if not fonts:
            fonts = RUSSIAN_FONTS

    # South Asian scripts mostly have a lot of different graphemes, so trim
    # down the mean_count so as not to get a huge amount of text.
    elif lang in ("asm", "ben"):
        mean_count = 15
        word_dawg_factor = 0.15
        if not fonts:
            fonts = BENGALI_FONTS
    elif lang in ("bih", "hin", "mar", "nep", "san"):
        mean_count = 15
        word_dawg_factor = 0.15
        if not fonts:
            fonts = DEVANAGARI_FONTS
    elif lang == "bod":
        mean_count = 15
        word_dawg_factor = 0.15
        if not fonts:
            fonts = TIBETAN_FONTS
    elif lang == "dzo":
        word_dawg_factor = 0.01
        if not fonts:
            fonts = TIBETAN_FONTS
    elif lang == "guj":
        mean_count = 15
        word_dawg_factor = 0.15
        if not fonts:
            fonts = GUJARATI_FONTS
    elif lang == "kan":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--no_newline_in_output"]
        text2image_extra_args += ["--char_spacing=0.5"]
        if not fonts:
            fonts = KANNADA_FONTS
    elif lang == "mal":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--no_newline_in_output"]
        text2image_extra_args += ["--char_spacing=0.5"]
        if not fonts:
            fonts = MALAYALAM_FONTS
    elif lang == "ori":
        word_dawg_factor = 0.01
        if not fonts:
            fonts = ORIYA_FONTS
    elif lang == "pan":
        mean_count = 15
        word_dawg_factor = 0.01
        if not fonts:
            fonts = PUNJABI_FONTS
    elif lang == "sin":
        mean_count = 15
        word_dawg_factor = 0.01
        if not fonts:
            fonts = SINHALA_FONTS
    elif lang == "tam":
        mean_count = 30
        word_dawg_factor = 0.15
        training_data_arguments += ["--no_newline_in_output"]
        text2image_extra_args += ["--char_spacing=0.5"]
        if not fonts:
            fonts = TAMIL_FONTS
    elif lang == "tel":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--no_newline_in_output"]
        text2image_extra_args += ["--char_spacing=0.5"]
        if not fonts:
            fonts = TELUGU_FONTS

    # SouthEast Asian scripts.
    elif lang == "jav_java":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--infrequent_ratio=10000"]
        if not fonts:
            fonts = JAVANESE_FONTS
    elif lang == "khm":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--infrequent_ratio=10000"]
        if not fonts:
            fonts = KHMER_FONTS
    elif lang == "lao":
        mean_count = 15
        word_dawg_factor = 0.15
        training_data_arguments += ["--infrequent_ratio=10000"]
        if not fonts:
            fonts = LAOTHIAN_FONTS
    elif lang == "mya":
        mean_count = 12
        word_dawg_factor = 0.15
        training_data_arguments += ["--infrequent_ratio=10000"]
        if not fonts:
            fonts = BURMESE_FONTS
    elif lang == "tha":
        mean_count = 30
        word_dawg_factor = 0.01
        training_data_arguments += ["--infrequent_ratio=10000"]
        filter_arguments += ["--segmenter_lang=tha"]
        training_data_arguments += ["--no_space_in_output", "--desired_bigrams="]
        ambigs_filter_denominator = "1000"
        leading = 48
        if not fonts:
            fonts = THAI_FONTS

    # CJK
    elif lang == "chi_sim":
        mean_count = 15
        punc_dawg_factor = 0.015
        word_dawg_factor = 0.015
        generate_word_bigrams = 0
        training_data_arguments += ["--infrequent_ratio=10000"]
        training_data_arguments += ["--no_space_in_output", "--desired_bigrams="]
        filter_arguments += ["--charset_filter=chi_sim", "--segmenter_lang=chi_sim"]
        if not fonts:
            fonts = CHI_SIM_FONTS
    elif lang == "chi_tra":
        mean_count = 15
        word_dawg_factor = 0.015
        generate_word_bigrams = 0
        training_data_arguments += ["--infrequent_ratio=10000"]
        training_data_arguments += ["--no_space_in_output", "--desired_bigrams="]
        filter_arguments += ["--charset_filter=chi_tr", "--segmenter_lang=chi_tra"]
        if not fonts:
            fonts = CHI_TRA_FONTS
    elif lang == "jpn":
        mean_count = 15
        word_dawg_factor = 0.015
        generate_word_bigrams = 0
        training_data_arguments += ["--infrequent_ratio=10000"]
        training_data_arguments += ["--no_space_in_output", "--desired_bigrams="]
        filter_arguments += ["--charset_filter=jpn", "--segmenter_lang=jpn"]
        if not fonts:
            fonts = JPN_FONTS
    elif lang == "kor":
        mean_count = 20
        word_dawg_factor = 0.015
        number_dawg_factor = 0.05
        training_data_arguments += ["--infrequent_ratio=10000"]
        training_data_arguments += ["--desired_bigrams="]
        generate_word_bigrams = 0
        filter_arguments += ["--charset_filter=kor", "--segmenter_lang=kor"]
        if not fonts:
            fonts = KOREAN_FONTS

    # Middle-Eastern scripts.
    elif lang == "ara":
        if not fonts:
            fonts = ARABIC_FONTS
    elif lang == "div":
        if not fonts:
            fonts = THAANA_FONTS
    elif lang in ("fas", "pus", "snd", "uig", "urd"):
        if not fonts:
            fonts = PERSIAN_FONTS
    elif lang in ("heb", "yid"):
        number_dawg_factor = 0.05
        word_dawg_factor = 0.08
        if not fonts:
            fonts = HEBREW_FONTS
    elif lang == "syr":
        if not fonts:
            fonts = SYRIAC_FONTS

    # Other scripts.
    elif lang in ("amh", "tir"):
        if not fonts:
            fonts = AMHARIC_FONTS
    elif lang == "chr":
        if not fonts:
            fonts = [*NORTH_AMERICAN_ABORIGINAL_FONTS, "Noto Sans Cherokee"]
    elif lang == "ell":
        number_dawg_factor = 0.05
        word_dawg_factor = 0.08
        if not fonts:
            fonts = GREEK_FONTS
    elif lang == "grc":
        if not exposures:
            exposures = [-3, -2, -1, 0, 1, 2, 3]
        if not fonts:
            fonts = ANCIENT_GREEK_FONTS
    elif lang == "hye":
        if not fonts:
            fonts = ARMENIAN_FONTS
    elif lang == "iku":
        if not fonts:
            fonts = NORTH_AMERICAN_ABORIGINAL_FONTS
    elif lang == "kat":
        if not fonts:
            fonts = GEORGIAN_FONTS
    elif lang == "kat_old":
        text_corpus = f"{FLAGS_WEBTEXT_PREFIX}/kat.corpus.txt"
        if not fonts:
            fonts = OLD_GEORGIAN_FONTS
    elif lang == "kir":
        if not fonts:
            fonts = KYRGYZ_FONTS
        training_data_arguments += ["--infrequent_ratio=100"]
    elif lang == "kmr":
        if not fonts:
            fonts = LATIN_FONTS
    elif lang == "kur_ara":
        if not fonts:
            fonts = KURDISH_FONTS
    else:
        raise ValueError(f"Error: {lang} is not a valid language code")

    flags_mean_count = int(os.environ.get("FLAGS_mean_count", -1))
    if flags_mean_count > 0:
        training_data_arguments += [f"--mean_count={flags_mean_count}"]
    elif not mean_count:
        training_data_arguments += [f"--mean_count={mean_count}"]

    # Default to Latin fonts if none have been set
    if not fonts:
        fonts = LATIN_FONTS

    # Default to 0 exposure if it hasn't been set
    if not exposures:
        exposures = [0]
    # Set right-to-left and normalization mode.
    if lang in (
            "ara",
            "div",
            "fas",
            "pus",
            "snd",
            "syr",
            "uig",
            "urd",
            "kur_ara",
            "heb",
            "yid",
    ):
        lang_is_rtl = True
        norm_mode = 2
    elif lang in (
            "asm",
            "ben",
            "bih",
            "hin",
            "mar",
            "nep",
            "guj",
            "kan",
            "mal",
            "tam",
            "tel",
            "pan",
            "dzo",
            "sin",
            "san",
            "bod",
            "ori",
            "khm",
            "mya",
            "tha",
            "lao",
            "jav ",
            "jav_java",
    ):
        lang_is_rtl = False
        norm_mode = 2
    else:
        lang_is_rtl = False
        norm_mode = 1

    vars_to_transfer = {
        'ambigs_filter_denominator': ambigs_filter_denominator,
        'bigram_dawg_factor': bigram_dawg_factor,
        'exposures': exposures,
        'filter_arguments': filter_arguments,
        'fonts': fonts,
        'fragments_disabled': fragments_disabled,
        'generate_word_bigrams': generate_word_bigrams,
        'lang_is_rtl': lang_is_rtl,
        'leading': leading,
        'mean_count': mean_count,
        'mix_lang': mix_lang,
        'norm_mode': norm_mode,
        'number_dawg_factor': number_dawg_factor,
        'punc_dawg_factor': punc_dawg_factor,
        'run_shape_clustering': run_shape_clustering,
        'text2image_extra_args': text2image_extra_args,
        'text_corpus': text_corpus,
        'training_data_arguments': training_data_arguments,
        'word_dawg_factor': word_dawg_factor,
        'word_dawg_size': word_dawg_size,
        'wordlist2dawg_arguments': wordlist2dawg_arguments,
    }

    for attr, value in vars_to_transfer.items():
        if hasattr(ctx, attr):
            if getattr(ctx, attr) != value:
                log.debug(f"{attr} = {value} (was {getattr(ctx, attr)})")
                setattr(ctx, attr, value)
            else:
                log.debug(f"{attr} = {value} (set on cmdline)")
        else:
            log.debug(f"{attr} = {value}")
            setattr(ctx, attr, value)

    return ctx
