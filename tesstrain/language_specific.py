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
Set some language specific variables.
"""

from __future__ import annotations

import itertools
import logging
import os
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from tesstrain.arguments import TrainingArguments

log = logging.getLogger(__name__)

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

FRAKTUR_FONTS: List[str] = [
    "CaslonishFraxx Medium",
    "Cloister Black, Light",
    "Proclamate Light",
    "UnifrakturMaguntia",
    "Walbaum-Fraktur",
]

# List of fonts to train on
LATIN_FONTS: List[str] = [
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
NEOLATIN_FONTS: List[str] = [
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

IRISH_UNCIAL_FONTS: List[str] = [
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

EARLY_LATIN_FONTS: List[str] = [
    *FRAKTUR_FONTS,
    *LATIN_FONTS,
    # The Wyld font family renders early modern ligatures encoded in the private
    # unicode area.
    "Wyld",
    "Wyld Italic",
    # Fonts that render the Yogh symbol (U+021C, U+021D) found in Old English.
    "GentiumAlt",
]

VIETNAMESE_FONTS: List[str] = [
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

DEVANAGARI_FONTS: List[str] = [
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

KANNADA_FONTS: List[str] = [
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

TELUGU_FONTS: List[str] = [
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

TAMIL_FONTS: List[str] = [
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

THAI_FONTS: List[str] = [
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

KOREAN_FONTS: List[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Baekmuk Batang Patched",
    "Baekmuk Batang",
    "Baekmuk Dotum",
    "Baekmuk Gulim",
    "Baekmuk Headline",
]

CHI_SIM_FONTS: List[str] = [
    "AR PL UKai CN",
    "AR PL UMing Patched Light",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "WenQuanYi Zen Hei Medium",
]

CHI_TRA_FONTS: List[str] = [
    "AR PL UKai TW",
    "AR PL UMing TW MBE Light",
    "AR PL UKai Patched",
    "AR PL UMing Patched Light",
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "WenQuanYi Zen Hei Medium",
]

JPN_FONTS: List[str] = [
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

RUSSIAN_FONTS: List[str] = [
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

GREEK_FONTS: List[str] = [
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

ANCIENT_GREEK_FONTS: List[str] = [
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

ARABIC_FONTS: List[str] = [
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

HEBREW_FONTS: List[str] = [
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

BENGALI_FONTS: List[str] = [
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

KYRGYZ_FONTS: List[str] = [
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

PERSIAN_FONTS: List[str] = [
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

AMHARIC_FONTS: List[str] = [
    "Abyssinica SIL",
    "Droid Sans Ethiopic Bold",
    "Droid Sans Ethiopic",
    "FreeSerif",
    "Noto Sans Ethiopic Bold",
    "Noto Sans Ethiopic",
]

ARMENIAN_FONTS: List[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "FreeMono",
    "FreeMono Italic",
    "FreeSans",
    "FreeSans Bold",
    "FreeSans Oblique",
]

BURMESE_FONTS: List[str] = [
    "Myanmar Sans Pro",
    "Noto Sans Myanmar Bold",
    "Noto Sans Myanmar",
    "Padauk Bold",
    "Padauk",
    "TharLon",
]

JAVANESE_FONTS: List[str] = ["Prada"]

NORTH_AMERICAN_ABORIGINAL_FONTS: List[str] = [
    "Aboriginal Sans",
    "Aboriginal Sans Bold Italic",
    "Aboriginal Sans Italic",
    "Aboriginal Sans Bold",
    "Aboriginal Serif Bold",
    "Aboriginal Serif Bold Italic",
    "Aboriginal Serif Italic",
    "Aboriginal Serif",
]

GEORGIAN_FONTS: List[str] = [
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

OLD_GEORGIAN_FONTS: List[str] = [
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

KHMER_FONTS: List[str] = [
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

KURDISH_FONTS: List[str] = [
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

LAOTHIAN_FONTS: List[str] = [
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

GUJARATI_FONTS: List[str] = [
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

MALAYALAM_FONTS: List[str] = [
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

ORIYA_FONTS: List[str] = [
    "Arial Unicode MS",
    "Arial Unicode MS Bold",
    "Ascender Uni",
    "ori1Uni Medium",
    "Samyak Oriya Medium",
    "Lohit Oriya",
]

PUNJABI_FONTS: List[str] = [
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

SINHALA_FONTS: List[str] = [
    "Noto Sans Sinhala Bold",
    "Noto Sans Sinhala",
    "OCRUnicode",
    "Yagpo",
    "LKLUG",
    "FreeSerif",
]

SYRIAC_FONTS: List[str] = [
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

THAANA_FONTS: List[str] = ["FreeSerif"]

TIBETAN_FONTS: List[str] = [
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
VERTICAL_FONTS: List[str] = [
    "TakaoExGothic",
    "TakaoExMincho",
    "AR PL UKai Patched",
    "AR PL UMing Patched Light",
    "Baekmuk Batang Patched",
]

FLAGS_webtext_prefix: str = os.environ.get("FLAGS_webtext_prefix", "")


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
    TEXT_CORPUS: str = f"{FLAGS_webtext_prefix}/{lang}.corpus.txt"
    FILTER_ARGUMENTS: List[str] = []
    WORDLIST2DAWG_ARGUMENTS: str = ""
    # These dawg factors represent the fraction of the corpus not covered by the
    # dawg, and seem like reasonable defaults, but the optimal value is likely
    # to be highly corpus-dependent, as well as somewhat language-dependent.
    # Number dawg factor is the fraction of all numeric strings that are not
    # covered, which is why it is higher relative to the others.
    PUNC_DAWG_FACTOR: Optional[float] = None
    NUMBER_DAWG_FACTOR: float = 0.125
    WORD_DAWG_FACTOR: float = 0.05
    BIGRAM_DAWG_FACTOR: float = 0.015
    TRAINING_DATA_ARGUMENTS: List[str] = []
    FRAGMENTS_DISABLED: str = "y"
    RUN_SHAPE_CLUSTERING: bool = False
    AMBIGS_FILTER_DENOMINATOR: str = "100000"
    LEADING: int = 32
    MEAN_COUNT: int = 40  # Default for latin script.
    # Language to mix with the language for maximum accuracy. Defaults to eng.
    # If no language is good, set to the base language.
    MIX_LANG: str = "eng"
    FONTS: List[str] = ctx.fonts
    TEXT2IMAGE_EXTRA_ARGS: List[str] = []
    EXPOSURES: List[int] = list(map(int, itertools.chain(*ctx.exposures or [])))

    GENERATE_WORD_BIGRAMS: Optional[int] = None
    WORD_DAWG_SIZE: Optional[int] = None

    # Latin languages.
    if lang == "enm":
        TEXT2IMAGE_EXTRA_ARGS += ["--ligatures"]  # Add ligatures when supported
        if not FONTS:
            FONTS = EARLY_LATIN_FONTS
    elif lang == "frm":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/fra.corpus.txt"
        # Make long-s substitutions for Middle French text
        FILTER_ARGUMENTS += ["--make_early_language_variant=fra"]
        TEXT2IMAGE_EXTRA_ARGS += ["--ligatures"]  # Add ligatures when supported.
        if not FONTS:
            FONTS = EARLY_LATIN_FONTS
    elif lang in {"frk", "deu_latf"}:
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/deu.corpus.txt"
        if not FONTS:
            FONTS = FRAKTUR_FONTS
    elif lang == "ita_old":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/ita.corpus.txt"
        # Make long-s substitutions for Early Italian text
        FILTER_ARGUMENTS += ["--make_early_language_variant=ita"]
        TEXT2IMAGE_EXTRA_ARGS += ["--ligatures"]  # Add ligatures when supported.
        if not FONTS:
            FONTS = EARLY_LATIN_FONTS
    elif lang == "lat":
        if not EXPOSURES:
            EXPOSURES = [-3, -2, -1, 0, 1, 2, 3]
        if not FONTS:
            FONTS = NEOLATIN_FONTS
    elif lang == "spa_old":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/spa.corpus.txt"
        # Make long-s substitutions for Early Spanish text
        FILTER_ARGUMENTS += ["--make_early_language_variant=spa"]
        TEXT2IMAGE_EXTRA_ARGS += ["--ligatures"]  # Add ligatures when supported.
        if not FONTS:
            FONTS = EARLY_LATIN_FONTS
    elif lang == "srp_latn":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/srp.corpus.txt"
    elif lang == "vie":
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        if not FONTS:
            FONTS = VIETNAMESE_FONTS
        # Highly inflective languages get a bigger dawg size.
        # TODO(rays) Add more here!
    elif lang == "hun":
        WORD_DAWG_SIZE = 1_000_000
    elif lang == "pol":
        WORD_DAWG_SIZE = 1_000_000

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
        PUNC_DAWG_FACTOR = 0.004
    elif lang == "cym":
        pass
    elif lang == "dan":
        pass
    elif lang == "deu":
        WORD_DAWG_FACTOR = 0.125
    elif lang == "eng":
        WORD_DAWG_FACTOR = 0.03
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
        WORD_DAWG_FACTOR = 0.08
    elif lang == "gle":
        pass
    elif lang == "gle_uncial":
        if not FONTS:
            FONTS = IRISH_UNCIAL_FONTS
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
        WORD_DAWG_FACTOR = 0.02
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
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/lat_lid.corpus.txt"
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        GENERATE_WORD_BIGRAMS = 0
        # Strip unrenderable words as not all fonts will render the extended
        # latin symbols found in Vietnamese text.
        WORD_DAWG_SIZE = 1_000_000
        if not FONTS:
            FONTS = EARLY_LATIN_FONTS

        # Cyrillic script-based languages. It is bad to mix Latin with Cyrillic.
    elif lang == "rus":
        if not FONTS:
            FONTS = RUSSIAN_FONTS
        MIX_LANG = "rus"
        NUMBER_DAWG_FACTOR = 0.05
        WORD_DAWG_SIZE = 1_000_000
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
        MIX_LANG = f"{lang}"
        if not FONTS:
            FONTS = RUSSIAN_FONTS

        # Special code for performing Cyrillic language-id that is trained on
        # Russian, Serbian, Ukrainian, Belarusian, Macedonian, Tajik and Mongolian
        # text with the list of Russian fonts.
    elif lang == "cyr_lid":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/cyr_lid.corpus.txt"
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        GENERATE_WORD_BIGRAMS = 0
        WORD_DAWG_SIZE = 1_000_000
        if not FONTS:
            FONTS = RUSSIAN_FONTS

        # South Asian scripts mostly have a lot of different graphemes, so trim
        # down the MEAN_COUNT so as not to get a huge amount of text.
    elif lang in ("asm", "ben"):
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        if not FONTS:
            FONTS = BENGALI_FONTS
    elif lang in ("bih", "hin", "mar", "nep", "san"):
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        if not FONTS:
            FONTS = DEVANAGARI_FONTS
    elif lang == "bod":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        if not FONTS:
            FONTS = TIBETAN_FONTS
    elif lang == "dzo":
        WORD_DAWG_FACTOR = 0.01
        if not FONTS:
            FONTS = TIBETAN_FONTS
    elif lang == "guj":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        if not FONTS:
            FONTS = GUJARATI_FONTS
    elif lang == "kan":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--no_newline_in_output"]
        TEXT2IMAGE_EXTRA_ARGS += ["--char_spacing=0.5"]
        if not FONTS:
            FONTS = KANNADA_FONTS
    elif lang == "mal":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--no_newline_in_output"]
        TEXT2IMAGE_EXTRA_ARGS += ["--char_spacing=0.5"]
        if not FONTS:
            FONTS = MALAYALAM_FONTS
    elif lang == "ori":
        WORD_DAWG_FACTOR = 0.01
        if not FONTS:
            FONTS = ORIYA_FONTS
    elif lang == "pan":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.01
        if not FONTS:
            FONTS = PUNJABI_FONTS
    elif lang == "sin":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.01
        if not FONTS:
            FONTS = SINHALA_FONTS
    elif lang == "tam":
        MEAN_COUNT = 30
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--no_newline_in_output"]
        TEXT2IMAGE_EXTRA_ARGS += ["--char_spacing=0.5"]
        if not FONTS:
            FONTS = TAMIL_FONTS
    elif lang == "tel":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--no_newline_in_output"]
        TEXT2IMAGE_EXTRA_ARGS += ["--char_spacing=0.5"]
        if not FONTS:
            FONTS = TELUGU_FONTS

        # SouthEast Asian scripts.
    elif lang == "jav_java":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        if not FONTS:
            FONTS = JAVANESE_FONTS
    elif lang == "khm":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        if not FONTS:
            FONTS = KHMER_FONTS
    elif lang == "lao":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        if not FONTS:
            FONTS = LAOTHIAN_FONTS
    elif lang == "mya":
        MEAN_COUNT = 12
        WORD_DAWG_FACTOR = 0.15
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        if not FONTS:
            FONTS = BURMESE_FONTS
    elif lang == "tha":
        MEAN_COUNT = 30
        WORD_DAWG_FACTOR = 0.01
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        FILTER_ARGUMENTS += ["--segmenter_lang=tha"]
        TRAINING_DATA_ARGUMENTS += ["--no_space_in_output", "--desired_bigrams="]
        AMBIGS_FILTER_DENOMINATOR = "1000"
        LEADING = 48
        if not FONTS:
            FONTS = THAI_FONTS

        # CJK
    elif lang == "chi_sim":
        MEAN_COUNT = 15
        PUNC_DAWG_FACTOR = 0.015
        WORD_DAWG_FACTOR = 0.015
        GENERATE_WORD_BIGRAMS = 0
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        TRAINING_DATA_ARGUMENTS += ["--no_space_in_output", "--desired_bigrams="]
        FILTER_ARGUMENTS += ["--charset_filter=chi_sim", "--segmenter_lang=chi_sim"]
        if not FONTS:
            FONTS = CHI_SIM_FONTS
    elif lang == "chi_tra":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.015
        GENERATE_WORD_BIGRAMS = 0
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        TRAINING_DATA_ARGUMENTS += ["--no_space_in_output", "--desired_bigrams="]
        FILTER_ARGUMENTS += ["--charset_filter=chi_tr", "--segmenter_lang=chi_tra"]
        if not FONTS:
            FONTS = CHI_TRA_FONTS
    elif lang == "jpn":
        MEAN_COUNT = 15
        WORD_DAWG_FACTOR = 0.015
        GENERATE_WORD_BIGRAMS = 0
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        TRAINING_DATA_ARGUMENTS += ["--no_space_in_output", "--desired_bigrams="]
        FILTER_ARGUMENTS += ["--charset_filter=jpn", "--segmenter_lang=jpn"]
        if not FONTS:
            FONTS = JPN_FONTS
    elif lang == "kor":
        MEAN_COUNT = 20
        WORD_DAWG_FACTOR = 0.015
        NUMBER_DAWG_FACTOR = 0.05
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=10000"]
        TRAINING_DATA_ARGUMENTS += ["--desired_bigrams="]
        GENERATE_WORD_BIGRAMS = 0
        FILTER_ARGUMENTS += ["--charset_filter=kor", "--segmenter_lang=kor"]
        if not FONTS:
            FONTS = KOREAN_FONTS

        # Middle-Eastern scripts.
    elif lang == "ara":
        if not FONTS:
            FONTS = ARABIC_FONTS
    elif lang == "div":
        if not FONTS:
            FONTS = THAANA_FONTS
    elif lang in ("fas", "pus", "snd", "uig", "urd"):
        if not FONTS:
            FONTS = PERSIAN_FONTS
    elif lang in ("heb", "yid"):
        NUMBER_DAWG_FACTOR = 0.05
        WORD_DAWG_FACTOR = 0.08
        if not FONTS:
            FONTS = HEBREW_FONTS
    elif lang == "syr":
        if not FONTS:
            FONTS = SYRIAC_FONTS

        # Other scripts.
    elif lang in ("amh", "tir"):
        if not FONTS:
            FONTS = AMHARIC_FONTS
    elif lang == "chr":
        if not FONTS:
            FONTS = [*NORTH_AMERICAN_ABORIGINAL_FONTS, "Noto Sans Cherokee"]
    elif lang == "ell":
        NUMBER_DAWG_FACTOR = 0.05
        WORD_DAWG_FACTOR = 0.08
        if not FONTS:
            FONTS = GREEK_FONTS
    elif lang == "grc":
        if not EXPOSURES:
            EXPOSURES = [-3, -2, -1, 0, 1, 2, 3]
        if not FONTS:
            FONTS = ANCIENT_GREEK_FONTS
    elif lang == "hye":
        if not FONTS:
            FONTS = ARMENIAN_FONTS
    elif lang == "iku":
        if not FONTS:
            FONTS = NORTH_AMERICAN_ABORIGINAL_FONTS
    elif lang == "kat":
        if not FONTS:
            FONTS = GEORGIAN_FONTS
    elif lang == "kat_old":
        TEXT_CORPUS = f"{FLAGS_webtext_prefix}/kat.corpus.txt"
        if not FONTS:
            FONTS = OLD_GEORGIAN_FONTS
    elif lang == "kir":
        if not FONTS:
            FONTS = KYRGYZ_FONTS
        TRAINING_DATA_ARGUMENTS += ["--infrequent_ratio=100"]
    elif lang == "kmr":
        if not FONTS:
            FONTS = LATIN_FONTS
    elif lang == "kur_ara":
        if not FONTS:
            FONTS = KURDISH_FONTS
    else:
        raise ValueError(f"Error: {lang} is not a valid language code")

    FLAGS_mean_count = int(os.environ.get("FLAGS_mean_count", -1))
    if FLAGS_mean_count > 0:
        TRAINING_DATA_ARGUMENTS += [f"--mean_count={FLAGS_mean_count}"]
    elif not MEAN_COUNT:
        TRAINING_DATA_ARGUMENTS += [f"--mean_count={MEAN_COUNT}"]

    # Default to Latin fonts if none have been set
    if not FONTS:
        FONTS = LATIN_FONTS

    # Default to 0 exposure if it hasn't been set
    if not EXPOSURES:
        EXPOSURES = [0]
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
        LANG_IS_RTL = True
        NORM_MODE = 2
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
        LANG_IS_RTL = False
        NORM_MODE = 2
    else:
        LANG_IS_RTL = False
        NORM_MODE = 1

    vars_to_transfer = {
        'ambigs_filter_denominator': AMBIGS_FILTER_DENOMINATOR,
        'bigram_dawg_factor': BIGRAM_DAWG_FACTOR,
        'exposures': EXPOSURES,
        'filter_arguments': FILTER_ARGUMENTS,
        'fonts': FONTS,
        'fragments_disabled': FRAGMENTS_DISABLED,
        'generate_word_bigrams': GENERATE_WORD_BIGRAMS,
        'lang_is_rtl': LANG_IS_RTL,
        'leading': LEADING,
        'mean_count': MEAN_COUNT,
        'mix_lang': MIX_LANG,
        'norm_mode': NORM_MODE,
        'number_dawg_factor': NUMBER_DAWG_FACTOR,
        'punc_dawg_factor': PUNC_DAWG_FACTOR,
        'run_shape_clustering': RUN_SHAPE_CLUSTERING,
        'text2image_extra_args': TEXT2IMAGE_EXTRA_ARGS,
        'text_corpus': TEXT_CORPUS,
        'training_data_arguments': TRAINING_DATA_ARGUMENTS,
        'word_dawg_factor': WORD_DAWG_FACTOR,
        'word_dawg_size': WORD_DAWG_SIZE,
        'wordlist2dawg_arguments': WORDLIST2DAWG_ARGUMENTS,
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
