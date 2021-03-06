#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of asrt.

# asrt is free software: you can redistribute it and/or modify
# it under the terms of the BSD 3-Clause License as published by
# the Open Source Initiative.

# asrt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# BSD 3-Clause License for more details.

# You should have received a copy of the BSD 3-Clause License
# along with asrt. If not, see <http://opensource.org/licenses/>.

__author__ = "Alexandre Nanchen"
__version__ = "Revision: 1.0"
__date__ = "Date: 2015/09"
__copyright__ = "Copyright (c) 2015 Idiap Research Institute"
__license__ = "BSD 3-Clause"

from asrt.config.AsrtConfig import FRENCH, GERMAN, ENGLISH

SPACEPATTERN = "[ ]+"
CAPTURINGDIGITPATTERN = "([0-9\.,]+)"
GROUPINGDOTCOMMAPATTERN = "( |$)([.,])( |$)"
EXPANDEXCEPTIONS = {FRENCH: "[0-9]+(er|re|ère|e|ème)",
                    ENGLISH: "[0-9]+(st|nd|rd|th)"}

UNITD2W = {1: 'ein', 2: 'zwei', 3: 'drei', 4: 'vier', 5: 'fünf', 6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun',
           10: 'zehn', 11: 'elf', 12: 'zwölf', 13: 'dreizehn', 14: 'vierzehn', 15: 'fünfzehn', 16: 'sechszehn',
           17: 'siebzehn', 18: 'achtzehn', 19: 'neunzehn'}

DECADED2W = {1: 'zehn', 2: 'zwanzig', 3: 'dreissig', 4: 'vierzig', 5: 'fünfzig', 6: 'sechzig', 7: 'siebzig',
             8: 'achtzig', 9: 'neunzig'}
GERMANMONTHESREGEX = "(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)"

# See https://en.wikipedia.org/wiki/List_of_Unicode_characters
# http://www.cloford.com/resources/charcodes/utf-8_punctuation.htm
# http://xahlee.info/comp/unicode_matching_brackets.html
# Format is matching pattern, substitution, comment, language id
UTF8MAP = [
    ("\u00A0", " ", "Spaces: non-breaking space", "0"),
    ("\ufeff", " ", "Spaces: invisible", "0"),
    ("\u200B", " ", "Spaces: zero-width space", "0"),
    ("\u200c", " ", "Spaces: zero-width non-joiner", "0"),
    ("\u200d", " ", "Spaces: zero-width joiner", "0"),
    ("\u2002", " ", "Spaces: en space", "0"),
    ("\u2003", " ", "Spaces: em space", "0"),
    ("\u2000", " ", "Spaces: en quad", "0"),
    ("\u2001", " ", "Spaces: em quad", "0"),
    ("\u2004", " ", "Spaces: three-per-em space", "0"),
    ("\u2005", " ", "Spaces: four-per-em space", "0"),
    ("\u2006", " ", "Spaces: six-per-em space", "0"),
    ("\u2007", " ", "Spaces: figure space", "0"),
    ("\u2008", " ", "Spaces: punctuation space", "0"),
    ("\u2009", " ", "Spaces: thin space", "0"),
    ("\u200A", " ", "Spaces: hair space", "0"),
    ("\u200e", " ", "Spaces: left to right mark, narrow no-break space", "0"),
    ("\u200f", " ", "Spaces: right to left mark, narrow no-break space", "0"),
    ("\u205f", " ", "Spaces: math space", "0"),
    ("\u3000", " ", "Spaces: ideographic space", "0"),
    ("\u060c", ",", "Comma: arabic comma", "0"),
    ("\u066b", ",", "Comma: arabic decimal separator", "0"),
    ("\u066c", ",", "Comma: arabic thousands separator", "0"),
    ("\u3001", ",", "Comma: ideographic comma", "0"),
    ("\ufe50", ",", "Comma: small comma", "0"),
    ("\uff0c", ",", "Comma: fullwidth comma", "0"),
    ("\u06d4", ".", "Full stop: arabic full stop", "0"),
    ("\u2024", ".", "Full stop: one dot leader", "0"),
    ("\ufe52", ".", "Full stop: small full stop", "0"),
    ("\uff0e", ".", "Full stop: fullwidth full stop", "0"),
    ("\u3002", ".", "Full stop: ideographic full stop", "0"),
    ("\ufe55", ":", "Colon: small colon", "0"),
    ("\uff1a", ":", "Colon: fullwidth colon", "0"),
    ("\u0387", ";", "Semi colon: greek ano teleia", "0"),
    ("\u061B", ";", "Semi colon: arabic semicolon", "0"),
    ("\ufe54", ";", "Semi colon: small semicolon", "0"),
    ("\uff1b", ";", "Semi colon: fullwidth semicolon", "0"),
    ("\u2010", "-", "Hyphen: hyphen", "0"),
    ("\u2011", "-", "Hyphen: non-breaking hyphen", "0"),
    ("\u2012", "-", "Hyphen: figure dash", "0"),
    ("\u2013", "-", "Hyphen: en dash", "0"),
    ("\uff0d", "-", "Hyphen: fullwidth hyphen minus", "0"),
    ("\u2014", "-", "Hyphen: em dash", "0"),
    ("\u2015", "-", "Hyphen: horizontal bar ", "0"),
    ("\u2018", "'", "Quotation mark: left single quotation mark", "0"),
    ("\u2019", "'", "Quotation mark: right single quotation mark", "0"),
    ("\u201a", "'", "Quotation mark: single low-9 quotation mark", "0"),
    ("\u201b", "'", "Quotation mark: single reversed-9 quotation mark", "0"),
    ("\u201c", "'", "Quotation mark: left double quotation mark", "0"),
    ("\u201d", "'", "Quotation mark: right double quotation mark", "0"),
    ("\u201e", "'", "Quotation mark: double low-9 quotation mark", "0"),
    ("\u2032", "'", "Quotation mark: prime", "0"),
    ("\u2033", "'", "Quotation mark: double prime", "0"),
    ("\u2034", "'", "Quotation mark: triple prime", "0"),
    ("\u2035", "'", "Quotation mark: reversed prime", "0"),
    ("\u2036", "'", "Quotation mark: reversed double prime", "0"),
    ("\u2037", "'", "Quotation mark: reversed triple prime", "0"),
    ("\u2039", "'", "Quotation mark: single left-pointing angle quotation mark", "0"),
    ("\u203A", "'", "Quotation mark: single right-pointing angle quotation mark", "0"),
    ("\u00b4", "'", "Quotation mark: acute accent", "0"),
    ("\uff07", "'", "Quotation mark: fullwidth apostrophe", "0"),
    ("\u00ab", "\"", "Quotation mark: left-pointing double angle quotation mark", "0"),
    ("\u00bb", "\"", "Quotation mark: right-pointing double angle quotation mark", "0"),
    ("\u037e", "?", "Question mark: greek question mark", "0"),
    ("\u00bf", "?", "Question mark: inverted question mark", "0"),
    ("\u061f", "?", "Question mark: arabic question mark", "0"),
    ("\u203d", "?", "Question mark: interrobang combined question and exclamation marks", "0"),
    ("\ufe56", "?", "Question mark: small question mark", "0"),
    ("\uff1f", "?", "Question mark: fullwidth question mark", "0"),
    ("\uff01", "!", "Exclamation mark: fullwidth exclamation mark", "0"),
    ("\ufe6b", "@", "Commercial at: small commercial at", "0"),
    ("\uff20", "@", "Commercial at: fullwidth commercial at", "0"),
    ("\u2022", " ", "Bullet: bullet", "0"),
    ("\u2023", " ", "Bullet: triangular bullet", "0"),
    ("\u2025", " ", "Dot leader: two dot leader", "0"),
    ("\u2026", " ", "Horizontal ellipsis:horizontal ellipsis", "0"),
    ("\u2027", " ", "Hyphenation: hyphenation point", "0"),
    ("\u2028", r"", "Separator: line separator", "0"),
    ("\u2029", r"", "Separator: paragraph separator", "0"),
    ("\u00BC", "1/4", "Number forms: un quart", "0"),
    ("\u00BD", "1/2", "Number forms: un demi", "0"),
    ("\u00BE", "3/4", "Number forms: trois quarts", "0"),
    ("\u2150", "1/7", "Number forms: un septieme", "0"),
    ("\u2151", "1/9", "Number forms: un neuvieme", "0"),
    ("\u2152", "1/10", "Number forms: un dixieme", "0"),
    ("\u2153", "1/3", "Number forms: un tiers", "0"),
    ("\u2154", "2/3", "Number forms: deux tiers", "0"),
    ("\u2155", "1/5", "Number forms: un cinqieme", "0"),
    ("\u2156", "2/5", "Number forms: deux cinqieme", "0"),
    ("\u2157", "3/5", "Number forms: trois cinqieme", "0"),
    ("\u2158", "4/5", "Number forms: quatre cinqieme", "0"),
    ("\u2159", "1/6", "Number forms: un sixieme", "0"),
    ("\u215A", "5/6", "Number forms: cinq sixieme", "0"),
    ("\u215B", "1/8", "Number forms: un huitieme", "0"),
    ("\u215C", "3/8", "Number forms: trois huitieme", "0"),
    ("\u215D", "5/8", "Number forms: cinq huitieme", "0"),
    ("\u215E", "7/8", "Number forms: sept huitieme", "0"),
    ("\u0152", "oe", "Ligatures: lattin small ligature oe", "0"),
    ("\u0153", "oe", "Ligatures: lattin small ligature oe", "0"),

    # Some more
    ("\u2794", "", "HEAVY WIDE-HEADED RIGHTWARDS ARROW", "0"),
    #("\u002E",u"",u"FULL STOP",u"0"),
    ("\u00A1", "", "INVERTED EXCLAMATION MARK", "0"),
    ("\u00A2", "", "CENT SIGN", "0"),
    ("\u00A3", "livre", "POUND SIGN", "1"),
    ("\u00A9", "", "COPYRIGHT SIGN", "0"),
    ("\u00AE", "", "REGISTERED SIGN", "0"),
    ("\u00B2", "carré", "SUPERSCRIPT TWO", "1"),
    ("\u00B3", "cube", "SUPERSCRIPT THREE", "1"),
    ("\u00B5", "micro", "MICRO SIGN", "1"),
    ("\u00B7", "", "MIDDLE DOT", "0"),
    ("\u00B9", "", "SUPERSCRIPT ONE", "0"),
    # Accentuation
    # ("\u00C0",u"A",u"LATIN CAPITAL LETTER A WITH GRAVE",u"2"),
    # ("\u00E0",u"a",u"LATIN SMALL LETTER A WITH GRAVE",u"2"),
    # ("\u00C1",u"A",u"LATIN CAPITAL LETTER A WITH ACUTE",u"0"),
    # ("\u00E1",u"a",u"LATIN SMALL LETTER A WITH ACUTE",u"0"),
    # ("\u00C2",u"A",u"LATIN CAPITAL LETTER A WITH CIRCUMFLEX",u"2"),
    # ("\u00E2",u"a",u"LATIN SMALL LETTER A WITH CIRCUMFLEX",u"2"),
    # ("\u00C3",u"A",u"LATIN CAPITAL LETTER A WITH TILDE",u"0"),
    # ("\u00E3",u"a",u"LATIN SMALL LETTER A WITH TILDE",u"0"),
    # ("\u00C4",u"A",u"LATIN CAPITAL LETTER A WITH DIAERESIS",u"1"),
    # ("\u00E4",u"a",u"LATIN SMALL LETTER A WITH DIAERESIS",u"1"),
    # ("\u0100",u"A",u"LATIN CAPITAL LETTER A WITH MACRON",u"0"),
    # ("\u0101",u"a",u"LATIN SMALL LETTER A WITH MACRON",u"0"),
    # ("\u0102",u"A",u"LATIN CAPITAL LETTER A WITH BREVE",u"0"),
    # ("\u0103",u"a",u"LATIN SMALL LETTER A WITH BREVE",u"0"),

    # ("\u00C8",u"E",u"LATIN CAPITAL LETTER E WITH GRAVE",u"2"),
    # ("\u00E8",u"e",u"LATIN SMALL LETTER E WITH GRAVE",u"2"),
    # ("\u00C9",u"E",u"LATIN CAPITAL LETTER E WITH ACUTE",u"2"),
    # ("\u00E9",u"e",u"LATIN SMALL LETTER E WITH ACUTE",u"2"),
    # ("\u00CA",u"E",u"LATIN CAPITAL LETTER E WITH CIRCUMFLEX",u"2"),
    # ("\u00EA",u"e",u"LATIN SMALL LETTER E WITH CIRCUMFLEX",u"2"),
    # ("\u00CB",u"E",u"LATIN CAPITAL LETTER E WITH DIAERESIS",u"2"),
    # ("\u00EB",u"e",u"LATIN SMALL LETTER E WITH DIAERESIS",u"2"),
    # ("\u0114",u"E",u"LATIN CAPITAL LETTER E WITH BREVE",u"0"),
    # ("\u0115",u"e",u"LATIN SMALL LETTER E WITH BREVE",u"0"),
    # ("\u0116",u"E",u"LATIN CAPITAL LETTER E WITH DOT ABOVE",u"0"),
    # ("\u0117",u"e",u"LATIN SMALL LETTER E WITH DOT ABOVE",u"0"),
    # ("\u011A",u"E",u"LATIN CAPITAL LETTER E WITH CARON",u"0"),
    # ("\u011B",u"e",u"LATIN SMALL LETTER E WITH CARON",u"0"),

    # ("\u00CC",u"I",u"LATIN CAPITAL LETTER I WITH GRAVE",u"0"),
    # ("\u00EC",u"i",u"LATIN SMALL LETTER I WITH GRAVE",u"0"),
    # ("\u00CD",u"I",u"LATIN CAPITAL LETTER I WITH ACUTE",u"0"),
    # ("\u00ED",u"i",u"LATIN SMALL LETTER I WITH ACUTE",u"0"),
    # ("\u00CE",u"I",u"LATIN CAPITAL LETTER I WITH CIRCUMFLEX",u"2"),
    # ("\u00EE",u"i",u"LATIN SMALL LETTER I WITH CIRCUMFLEX",u"2"),
    # ("\u00CF",u"I",u"LATIN CAPITAL LETTER I WITH DIAERESIS",u"2"),
    # ("\u00EF",u"i",u"LATIN SMALL LETTER I WITH DIAERESIS",u"2"),
    # ("\u0128",u"I",u"LATIN CAPITAL LETTER I WITH TILDE",u"0"),
    # ("\u0129",u"i",u"LATIN SMALL LETTER I WITH TILDE",u"0"),
    # ("\u0131",u"i",u"LATIN SMALL LETTER DOTLESS I",u"0"),

    # ("\u00D2",u"O",u"LATIN CAPITAL LETTER O WITH GRAVE",u"0"),
    # ("\u00F2",u"o",u"LATIN SMALL LETTER O WITH GRAVE",u"0"),
    # ("\u00D3",u"O",u"LATIN CAPITAL LETTER O WITH ACUTE",u"0"),
    # ("\u00F3",u"o",u"LATIN SMALL LETTER O WITH ACUTE",u"0"),
    # ("\u00D4",u"O",u"LATIN CAPITAL LETTER O WITH CIRCUMFLEX",u"2"),
    # ("\u00F4",u"o",u"LATIN SMALL LETTER O WITH CIRCUMFLEX",u"2"),
    # ("\u00D5",u"O",u"LATIN CAPITAL LETTER O WITH TILDE",u"0"),
    # ("\u00F5",u"o",u"LATIN SMALL LETTER O WITH TILDE",u"0"),
    # ("\u00D8",u"O",u"LATIN CAPITAL LETTER O WITH STROKE",u"0"),
    # ("\u00F8",u"o",u"LATIN SMALL LETTER O WITH STROKE",u"0"),
    # ("\u0150",u"O",u"LATIN CAPITAL LETTER O WITH DOUBLE ACUTE",u"0"),
    # ("\u0151",u"o",u"LATIN SMALL LETTER O WITH DOUBLE ACUTE",u"0"),

    # ("\u00D9",u"U",u"LATIN CAPITAL LETTER U WITH GRAVE",u"2"),
    # ("\u00F9",u"u",u"LATIN SMALL LETTER U WITH GRAVE",u"2"),
    # ("\u00DA",u"u",u"LATIN CAPITAL LETTER U WITH ACUTE",u"0"),
    # ("\u00FA",u"u",u"LATIN SMALL LETTER U WITH ACUTE",u"0"),
    # ("\u00DB",u"U",u"LATIN CAPITAL LETTER U WITH CIRCUMFLEX",u"2"),
    # ("\u00FB",u"u",u"LATIN SMALL LETTER U WITH CIRCUMFLEX",u"2"),
    # ("\u016E",u"u",u"LATIN CAPITAL LETTER U WITH RING ABOVE",u"0"),
    # ("\u016F",u"u",u"LATIN SMALL LETTER U WITH RING ABOVE",u"0"),

    # ("\u0106",u"C",u"LATIN CAPITAL LETTER C WITH ACUTE",u"0"),
    # ("\u0107",u"c",u"LATIN SMALL LETTER C WITH ACUTE",u"0"),
    # ("\u010C",u"C",u"LATIN CAPITAL LETTER C WITH CARON",u"0"),
    # ("\u010D",u"c",u"LATIN SMALL LETTER C WITH CARON",u"0"),
    # ("\u010E",u"d",u"LATIN CAPITAL LETTER D WITH CARON",u"0"),
    # ("\u010F",u"d",u"LATIN SMALL LETTER D WITH CARON",u"0"),
    # ("\u0110",u"d",u"LATIN CAPITAL LETTER D WITH STROKE",u"0"),
    # ("\u0111",u"d",u"LATIN SMALL LETTER D WITH STROKE",u"0"),
    # ("\u011E",u"g",u"LATIN CAPITAL LETTER G WITH BREVE",u"0"),
    # ("\u011F",u"g",u"LATIN SMALL LETTER G WITH BREVE",u"0"),
    # ("\u0141",u"L",u"LATIN CAPITAL LETTER L WITH STROKE",u"0"),
    # ("\u0142",u"l",u"LATIN SMALL LETTER L WITH STROKE",u"0"),
    # ("\u0143",u"N",u"LATIN CAPITAL LETTER N WITH ACUTE",u"0"),
    # ("\u0144",u"n",u"LATIN SMALL LETTER N WITH ACUTE",u"0"),
    # ("\u015C",u"S",u"LATIN CAPITAL LETTER S WITH CIRCUMFLEX",u"0"),
    # ("\u015D",u"s",u"LATIN SMALL LETTER S WITH CIRCUMFLEX",u"0"),
    # ("\u0160",u"S",u"LATIN CAPITAL LETTER S WITH CARON",u"0"),
    # ("\u0161",u"s",u"LATIN SMALL LETTER S WITH CARON",u"0"),
    # ("\u0162",u"T",u"LATIN CAPITAL LETTER T WITH CEDILLA",u"0"),
    # ("\u0163",u"t",u"LATIN SMALL LETTER T WITH CEDILLA",u"0"),
    # ("\u0174",u"W",u"LATIN CAPITAL LETTER W WITH CIRCUMFLEX",u"0"),
    # ("\u0175",u"w",u"LATIN SMALL LETTER W WITH CIRCUMFLEX",u"0"),
    # ("\u0176",u"Y",u"LATIN CAPITAL LETTER Y WITH CIRCUMFLEX",u"0"),
    # ("\u0177",u"y",u"LATIN SMALL LETTER Y WITH CIRCUMFLEX",u"0"),
    # ("\u01B5",u"Z",u"LATIN CAPITAL LETTER Z WITH STROKE",u"0"),
    # ("\u01B6",u"z",u"LATIN SMALL LETTER Z WITH STROKE",u"0"),
    ("\u00C6", "AE", "LATIN CAPITAL LETTER AE", "0"),
    ("\u00E6", "ae", "LATIN SMALL LETTER AE", "0"),
    ("\u00F0", "", "LATIN SMALL LETTER ETH", "0"),
    ("\u00D1", "N", "LATIN CAPITAL LETTER N WITH TILDE", "0"),
    ("\u00F1", "n", "LATIN SMALL LETTER N WITH TILDE", "0"),
    ("\u00F7", "", "DIVISION SIGN", "0"),
    ("\uFB01", "fi", "LATIN SMALL LIGATURE FI", "0"),
    ("\uFB02", "fl", "LATIN SMALL LIGATURE FL", "0"),
    ("\u2016", "", "DOUBLE VERTICAL LINE", "0"),
    ("\u2017", "", "DOUBLE LOW LINE", "0"),
    ("\u2040", "", "CHARACTER TIE", "0"),
    ("\u2192", "", "RIGHTWARDS ARROW", "0"),
    ("\u2205", "", "EMPTY SET", "0"),
    ("\u2260", "", "NOT EQUAL TO", "0"),
    ("\u2264", "", "LESS-THAN OR EQUAL TO", "0"),
    ("\u2500", "", "BOX DRAWINGS LIGHT HORIZONTAL", "0"),
    ("\u25AA", "", "BLACK SMALL SQUARE", "0"),
    ("\u25AC", "", "BLACK RECTANGLE", "0"),
    ("\u263A", "", "WHITE SMILING FACE", "0"),
    ("\u02C7", "", "CARON", "0"),
    ("\u00A8", "", "DIAERESIS", "0"),
    ("\u00B0", "", "DEGREE SIGN", "0"),
    ("\u00A6", "", "BROKEN BAR", "0"),
    ("\u00AF", "", "MACRON", "0"),
    ("\u00B8", "", "CEDILLA", "0"),
    ("\u0027", "'", "APOSTROPHE", "0"),
    ("\u00B6", "", "PILCROW SIGN", "0"),
    ("\u20AC", "euro", "EURO SIGN", "0"),
    ("\u20FC", "", "NARROW NO-BREAK SPACE", "0"),
    ("\u2191", "", "UPWARDS ARROW", "0"),
    ("\u2193", "", "DOWNWARDS ARROW", "0"),
    ("\u2122", "", "TRADE MARK SIGN", "0"),
    ("\u02C6", "", "MODIFIER LETTER CIRCUMFLEX ACCENT", "0"),
    ("\uFB00", "ff", "LATIN SMALL LIGATURE FF", "0"),
    ("\u025B", "", "LATIN SMALL LETTER OPEN E", "0"),
    ("\u00BA", "", "MASCULINE ORDINAL INDICATOR", "0"),
    ("\u00DF", "ss", "LATIN SMALL LETTER SHARP S", "0"),
    ("\u1E9E", "ss", "LATIN SMALL LETTER SHARP S", "0"),
    ("\u0391", "alpha", "GREEK CAPITAL LETTER ALPHA", "0"),
    ("\u03B1", "alpha", "GREEK SMALL LETTER ALPHA", "0"),
    ("\u039C", "micro", "GREEK CAPITAL LETTER MU", "0"),
    ("\u03BC", "micro", "GREEK SMALL LETTER MU", "0"),
    ("\u0394", "delta", "GREEK CAPITAL LETTER DELTA", "0"),
    ("\u03B4", "delta", "GREEK SMALL LETTER DELTA", "0"),
    ("\u03BD", "", "GREEK SMALL LETTER NU", "0"),
    ("\u039D", "", "GREEK CAPITAL LETTER NU", "0"),
    ("\u03C3", "sigma", "GREEK SMALL LETTER SIGMA", "0"),
    ("\u03A3", "sigma", "GREEK CAPITAL LETTER SIGMA", "0"),
    ("\u03C4", "tau", "GREEK SMALL LETTER TAU", "0"),
    ("\u03A4", "tau", "GREEK CAPITAL LETTER TAU", "0"),
    ("\u03A8", "psi", "GREEK CAPITAL LETTER PSI", "0"),
    ("\u03C8", "psi", "GREEK SMALL LETTER PSI", "0"),
    ("\u03C9", "omega", "GREEK SMALL LETTER OMEGA", "0"),
    ("\u03A9", "omega", "GREEK CAPITAL LETTER OMEGA", "0"),
    ("\u1D49", "", "MODIFIER LETTER SMALL E", "0"),
    ("\uFFFD", "", "REPLACEMENT CHARACTER", "0"),
    ("\u2044", "/", "FRACTION SLASH", "0"),
    ("\u2200", "", "FOR ALL", "0"),
    ("\u2217", "x", "ASTERISK OPERATOR", "0"),
    ("\u22EF", "", "MIDLINE HORIZONTAL ELLIPSIS", "0"),
    ("\u2467", "", "CIRCLED DIGIT EIGHT", "0"),
    ("\u2468", "", "CIRCLED DIGIT NINE", "0"),
    ("\u2469", "", "CIRCLED DIGIT TEN", "0"),
    ("\u25A0", "", "BLACK SQUARE", "0"),
    ("\u25C6", "", "BLACK DIAMOND", "0"),
    ("\u275A", "", "HEAVY VERTICAL BAR", "0"),
    ("\u2AFA", "", "DOUBLE-LINE SLANTED GREATER-THAN OR EQUAL TO", "0"),
    ("\u2B0D", "", "UP DOWN BLACK ARROW", "0"),
    ("\uC532", "", "", "0"),
    ("\uC569", "", "", "0"),
    ("\u221E", "", "INFINITY", "0"),
    #("\u1D434",u"A",u"MATHEMATICAL ITALIC CAPITAL A",u"0"),
    #("\u1D436",u"C",u"MATHEMATICAL ITALIC CAPITAL C",u"0"),
    #("\u1D437",u"D",u"MATHEMATICAL ITALIC CAPITAL D",u"0"),
    #("\u1D438",u"E",u"MATHEMATICAL ITALIC CAPITAL E",u"0"),
    #("\u1D440",u"M",u"MATHEMATICAL ITALIC CAPITAL M",u"0"),
    #("\u1D443",u"P",u"MATHEMATICAL ITALIC CAPITAL P",u"0"),
    #("\u1D445",u"R",u"MATHEMATICAL ITALIC CAPITAL R",u"0"),
    #("\u1D446",u"S",u"MATHEMATICAL ITALIC CAPITAL S",u"0"),
    #("\u1D44B",u"X",u"MATHEMATICAL ITALIC CAPITAL X",u"0"),
    #("\u1D44C",u"Y",u"MATHEMATICAL ITALIC CAPITAL Y",u"0"),
    #("\u1D44D",u"Z",u"MATHEMATICAL ITALIC CAPITAL Z",u"0"),
    #("\u1D44E",u"a",u"MATHEMATICAL ITALIC SMALL a",u"0"),
    #("\u1D44F",u"b",u"MATHEMATICAL ITALIC SMALL b",u"0"),
    #("\u1D451",u"d",u"MATHEMATICAL ITALIC SMALL d",u"0"),
    #("\u1D453",u"f",u"MATHEMATICAL ITALIC SMALL f",u"0"),
    #("\u1D456",u"i",u"MATHEMATICAL ITALIC SMALL i",u"0"),
    #("\u1D458",u"k",u"MATHEMATICAL ITALIC SMALL k",u"0"),
    #("\u1D45E",u"q",u"MATHEMATICAL ITALIC SMALL q",u"0"),
    #("\u1D45F",u"r",u"MATHEMATICAL ITALIC SMALL r",u"0"),
    #("\u1D461",u"t",u"MATHEMATICAL ITALIC SMALL t",u"0"),
    #("\u1D466",u"y",u"MATHEMATICAL ITALIC SMALL y",u"0"),
    #("\u1D70B",u"pi",u"MATHEMATICAL ITALIC SMALL PI",u"0"),
]

# Do not exclude single quote
PUNCTUATIONEXCLUDE = ['!', '"', '#', '(', ')', '*', '+', '-',
                      '/', ':', ';', '<', '=', '>', '?', '[', '\\',
                      ']', '^', '_', '`', '{', '|', '}', '~']
PUNCTUATIONKEEPINWORD = ['/', '-']
DOTCOMMAEXCLUDE = ['.', ',']
PUNCTUATIONMAP = {
    "%": (r"%", r"pourcent", "Prozent", "percent", "per cento"),
    "‰": ("‰", r"pour mille", "Promille", "per mill", "grammi al litro"),
    "&": (r"&", r"et", "und", "and", "e"),
    "@": (r"@", r"at", "at", "at", "at"),
    '$': (r'$', r"dollars", "Dollar", "dollars", "dollari"),
}

PUNCTUATIONPATTERN = r"(\!|\"|#|\$|%|&|'|\(|\)|\*|\+|,|-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|\{|\}|~|\|){4,}"

# No row specifier
ACRONYMDELIMITER = "\$\$\$\$\$"
ACRONYMREGEXLIST = [(r"( |^)([A-Z]{2,4})s[.,:;]?( |$)",
                     r"\g<1>\g<2>S\g<3>", r"1", r"0", r"Acronyms"),
                    (r"( |^)([A-Z])([A-Z])([A-Z])([A-Z])([A-Z])[.,:;]?( |$)",
                     r"lambda p: p.group(1)+p.group(2).lower()+'. '+p.group(3).lower()+'. '+p.group(4).lower()+'. '+p.group(5).lower()+'. '+p.group(6).lower()+'.'+p.group(7)+'$$$$$'", r"1", r"0", r"Acronyms"),
                    (r"( |^)([A-Z])([A-Z])([A-Z])([A-Z])[.,:;]?( |$)",
                     r"lambda p: p.group(1)+p.group(2).lower()+'. '+p.group(3).lower()+'. '+p.group(4).lower()+'. '+p.group(5).lower()+'.'+p.group(6)+'$$$$$'", r"1", r"0", r"Acronyms"),
                    (r"( |^)([A-Z])([A-Z])([A-Z])[.,:;]?( |$)",
                     r"lambda p: p.group(1)+p.group(2).lower()+'. '+p.group(3).lower()+'. '+p.group(4).lower()+'.'+p.group(5)+'$$$$$'", r"1", r"0", r"Acronyms"),
                    (r"( |^)([A-Z])([A-Z])[.,:;]?( |$)",
                     r"lambda p: p.group(1)+p.group(2).lower()+'. '+p.group(3).lower()+'.'+p.group(4)+'$$$$$'", r"1", r"0", r"Acronyms")]

DATEREGEXLIST = [(r"([0-9][0-9])[./]([0-9][0-9])[./]([0-9][0-9][0-9]?[0-9]?)",
                  r"\g<1> \g<2> \g<3>", r"1", r"0", r"Dates")]

APOSTHROPHELIST = [(r"[']", r"' ", r"1", r"0", r"Spaces after apostrophes")]

CONTRACTIONPREFIXELIST = [
    (r"á", r"à", "2", r"1", ""),
    (r"-á-", r"-à-", "2", r"1", ""),
    (r"^[aA] ", r"à ", "1", r"1", ""),
    #("quelqu' un",ur"quelqu'un",u"2",ur"1",u""),
    #("c' qu",ur"ce qu",u"2",ur"1",u""),
    #("c' ",ur"c'",u"2",ur"1",u""),
    #("s' est",ur"s'est",u"2",ur"1",u""),
    #("s' agit ",ur"s'agit",u"2",ur"1",u""),
    #("s' agir",ur"s'agir",u"2",ur"1",u""),
    #("s' agiss",ur"s'agiss",u"2",ur"1",u""),
    #("s' il",ur"s'il",u"2",ur"1",u""),
    #("s' ils",ur"s'ils",u"2",ur"1",u""),
    #("d' abord",ur"d'abord",u"2",ur"1",u""),
    (r"d un(?P<gr1>e?)", r"d' un\g<gr1>", "2", r"1", ""),
    #("(?P<gr1>[jl])' ai",ur"\g<gr1>'ai",u"2",ur"1",u""),
    #("(?P<gr1>[jl])' y",ur"\g<gr1>'y",u"2",ur"1",u""),
    #("(?P<gr1>[ltm])' a",ur"\g<gr1>'a",u"2",ur"1",u""),
    #("n' est",ur"n'est",u"2",ur"1",u""),
    #("n' a",ur"n'a",u"2",ur"1",u""),
    #("(?P<gr1>[djlmnst])' y",ur"\g<gr1>'y",u"2",ur"1",u""),
    #("(?P<gr1>[cdjlmnst])' en",ur"\g<gr1>'en",u"2",ur"1",u""),
    #("(?P<gr1>qu)' y",ur"\g<gr1>'y",u"2",ur"1",u""),
    #("(?P<gr1>qu)' en",ur"\g<gr1>'en",u"2",ur"1",u""),
    (r"[ -]t[ -](?P<gr1>il|elle|on)", r" -t-\g<gr1>", "1", r"1", ""),
    (r"' s(?P<gr1> |$)", r"'s\g<gr1>", "1", r"3", "")]


TRANSITIONNUMBERS = {
    FRENCH: {'1.': 'premièrement', '2.': 'deuxièmement', '3.': 'troisièmement', '4.': 'quatrièmement',
             '5.': 'cinquièmement', '6.': 'sixièmement', '7.': 'septièmement', '8.': 'huitièmement',
             '9.': 'neuvièmement', '10.': 'dixièmement'},
    ENGLISH: {'1.': 'first', '2.': 'second', '3.': 'third', '4.': 'fourth', '5.': 'fifth', '6.': 'sixth', '7.': 'seventh', '8.': 'eigth', '9.': 'nineth', '10.': 'tenth'}
}


ABBREVIATIONS = {
    FRENCH: {'A/R': 'accusé de réception', 'adj.': 'adjectif', 'admin': 'administration', 'ann.': 'annexe', 'art.': 'article',
             'assoc.': 'association', 'av.': 'avenue', 'bibliogr.': 'bibliographie', 'bibl.': 'bibliothèque', 'biogr.': 'biographie', 'bd.': 'boulevard ',
             'cad': 'c’est-à-dire', 'cap.': 'capitale', 'C.Q.F.D.': 'ce qu’il fallait démontrer', 'chap.': 'chapitre', 'ch.': 'chemin', 'circ.': 'circonscription',
             'col.': 'colonne', 'Cie': 'compagnie', 'c/c': 'compte courant', 'concl.': 'conclusion', 'cf.': 'confer', 'conj.': 'conjonction', 'coop.': 'coopération',
             'c.v.': 'curriculum vitae', 'dest.': 'destinataire', 'disp.': 'disponible', 'Dr.': 'docteur', 'Drs.': 'docteurs', 'Dre.': 'doctoresse',
             'Dres.': 'doctoresses', 'doc.': 'document', 'env.': 'environ', 'etc.': 'et cetera', 'ex.': 'exemple', 'e.g.': 'exempli gratia', 'ext.': 'externe',
             'féd.': 'fédéral', 'fém.': 'féminin', 'fig.': 'figure', 'id.': 'idem', 'intro': 'introduction', 'MM.': 'messieurs', 'maj.': 'majuscule',
             'méd.': 'médecine', 'Mgr': 'monseigneur', 'Mgrs': 'messeigneurs ', 'Mlle': 'mademoiselle ', 'Mlles': 'mesdemoiselles', 'Mme': 'madame',
             'Mmes': 'mesdames', 'Mo': 'mégaoctet', 'N.B.': 'nota bene', 'nbre': 'nombre', 'nbx': 'nombreux', 'N/Réf.': 'notre référence', 'obs.': 'observation',
             'pcq': 'parce que', 'pers.': 'personne', 'plur.': 'pluriel', 'Prof.': 'professeur', 'P.-S.': 'post-scriptum', 'qté': 'quantité', 'qqn': 'quelqu’un',
             'tps': 'temps', 'qqch': 'quelque chose', 'qqf.': 'quelquefois', 'qqn': 'quelqu’un', 'RDV': 'rendez-vous', 'réf.': 'référence', 'rte': 'route',
             'sing.': 'singulier', 'St': 'saint', 'stat.': 'statistique', 'Ste': 'sainte', 'Sté': 'société', 'Stes': 'saintes', 'Sts': 'saints', 'suiv.': 'suivant',
             'sup.': 'supra', 'suppl.': 'supplément', 'S.V.P.': 's’il vous plaît', 'tél.': 'téléphone', 'téléc.': 'télécopieur', 'temp.': 'température',
             'trad.': 'traducteur', 'tjrs': 'toujours', 'univ.': 'université', 'us.': 'usage', 'UV': 'ultraviolet', 'V/Réf.': 'votre référence'},
    GERMAN: {'a.A.': 'auf Anfrage', 'Abb.': 'Abbildung', 'Abf.': 'Abfahrt', 'Abh.': 'Abhandlung', 'Abk.': 'Abkürzung', 'Abs.': 'Absender', 'Abschn.': 'Abschnitt',
             'Abt.': 'Abteilung', 'abw.': 'abwesend', 'akad.': 'Akademisch', 'AK': 'Aktienkapital', 'Akk.': 'Akkusativ', 'Akku': 'Akkumulator', 'allg.': 'allgemein',
             'a.M.': 'am Main', 'Anh.': 'Anhang', 'Ank.': 'Ankunft', 'Anm.': 'Anmerkung', 'Antw.': 'Antwort', 'Anw.': 'Anweisung', 'Anz.': 'Anzeiger', 'Aufl.': 'Auflage',
             'aussch.': 'Ausschliesslich', 'Az': 'Aktenzeichen', 'Bed.': 'Bedarf', 'begl.': 'beglaubigt', 'beil.': 'beiliegend', 'beisp.': 'beispielweise',
             'Ber.': 'Bericht', 'bes.': 'besonders', 'Betr.': 'Betreff', 'betr.': 'betreffend', 'Bez.': 'Bezirk', 'bez.': 'Bezeichnung', 'BH': 'Bustenhalter',
             'Bhf.': 'Bahnhof', 'Bl.': 'Blatt', 'Br.': 'Bruder', 'bz.': 'bezahlt', 'bzw.': 'beziehungsweise', 'cal.': 'Kalorie', 'cand.': 'Kandidat', 'cbm': 'Kubikmeter',
             'ccm': 'Kubiczentimeter', 'dag.': 'dagegen', 'dam.': 'damals', 'Dat.': 'Dativ', 'dazw.': 'dazwischen', 'db': 'Dezibel', 'desgl.': 'desgleichen',
             'dgl.': 'dergleichen', 'Dipl.': 'Diplom', 'Doz.': 'Dozent', 'Dr.': 'Doktor', 'Dr.h.c.': 'Doktor honoris causa', 'dt.': 'deutsch', 'dz.': 'derzeit',
             'ehem.': 'ehemals', 'eigtl.': 'eigentlich', 'EKG': 'Elektrokardiogramm', 'entspr.': 'entsprechend', 'entw.': 'entweder', 'ER': 'Europarat',
             'Erdg.': 'Erdgeschoss', 'Essl.': 'Esslöffel', 'etw.': 'etwas', 'exkl.': 'exklusive', 'Ff.': 'Fortsetzung folgt', 'Fak.': 'Fakultät', 'Fam.': 'Familie',
             'Fdw.': 'Feldwebel', 'Fr.': 'Frau', 'Frl.': 'Fraulein', 'geb.': 'geboren', 'Gebr.': 'Gebrüder', 'gegr.': 'gegrundet', 'gesch.': 'geschieden',
             'geschr.': 'geschrieben', 'ges.gesch.': 'gesetzlich geschützt', 'geschl.': 'geschlossen', 'gest.': 'gestorben', 'gez.': 'gezeichnet', 'GG': 'Grundgesetz',
             'GmbH': 'Gesellschaft mit beschränkter Haftung', 'gzj.': 'ganzjährig', 'ha.': 'Hektar', 'habil.': 'habilitiert', 'Hbf.': 'Hauptbahnhof', 'hdt.': 'hundert',
             'hj.': 'halbjährlich', 'höfl.': 'höflichst', 'Hptst.': 'Hauptstadt', 'Hr.': 'Herr', 'i.allg.': 'im allgemeinen', 'i.F': 'in der Fassung', 'ill.': 'illustriert',
             'inbegr.': 'inbegriffen', 'Ind.': 'Indikativ', 'Ing.': 'Ingenieur', 'Inh.': 'Inhaber', 'inkl.': 'inklusive', 'Insp.': 'Inspektor', 'Inst.': 'Instanz',
             'Inst.': 'Institut', 'int.': 'international', 'inzw.': 'inzwischen', 'i.R.': 'im Ruhestand', 'iZm.': 'in Zusammenhang mit', 'jew.': 'jewelig', 'Jg.': 'Jahrgang',
             'Jh.': 'Jahrhundert', 'jun.': 'junior', 'jur.': 'juristisch', 'kath.': 'katholisch', 'Kfm.': 'Kaufmann', 'kg.': 'Kilogramm', 'kgl.': 'königlich', 'Kl.': 'Klasse',
             'km.': 'Kilometer', 'kn.': 'Knoten', 'kompl.': 'komplett', 'Kpt.': 'Kapitän', 'Kt.': 'Kanton', 'k.u.k.': 'kaiserlich und königlich', 'kW': 'Kilowatt',
             'led.': 'ledig', 'lfd.': 'laufend', 'Lfrg.': 'Lieferung', 'Lit.': 'Literatur', 'lt.': 'laut', 'Lt.': 'Leutnant', 'MA': 'Mittelalter', 'ma.': 'mittelälterlich',
             'Mag.': 'Magister', 'm.a.W.': 'mit anderen Worten', 'm.E': 'meines Erachtens', 'mech.': 'mechanisch', 'med.': 'medizinisch', 'mehrf.': 'mehrfach',
             'MEZ': 'Mitteleuropäische Zeit', 'MFG': 'mit freundlichen Grüssen', 'mg': 'Milligramm', 'Mill.': 'Million', 'Min.': 'Minute', 'mm': 'millimeter', 'Mo': 'Montag',
             'Mrd.': 'Milliarde', 'mtl.': 'monatlich', 'm.W.': 'meines Wissens', 'MWSt': 'Mehrwertsteuer', 'Mz.': 'Mehrzahl', 'N': 'Nord', 'Nachf.': 'Nachfolger',
             'nachm.': 'nachmittags', 'nat.': 'national', 'n.J.': 'nächsten Jahres', 'n.M.': 'nächsten Monats', 'N.N.': 'Name unbekannt', 'NO': 'Nordost',
             'Nr.': 'Nummer', 'NS': 'Nachschrift', 'NW': 'Nordwest', 'NZ': 'Nachrichtenzentrale', 'od.': 'oder', 'o.a.': 'oben angeführt', 'o.ä.': 'oder ähnliches',
             'o.A.': 'ohne Adresse', 'OB': 'Oberbefelshaber', 'o.B.': 'ohne Befund', 'OEZ': 'Osteuropäische Zeit', 'o.J.': 'ohne Jahr', 'ö.L': 'östlicher Länge',
             'o.Pr.': 'ordentlicher Professor', 'örtl.': 'örtlich', 'o.V.': 'ohne Verfasser', 'p.A.': 'per Adresse', 'Part.': 'Parterre', 'pat.': 'patentiert',
             'pharm.': 'pharmazeutisch', 'Pkt.': 'Punkt', 'Pl.': 'Platz', 'pl': 'Plural', 'pol.': 'politisch', 'pol.': 'polizeilich', 'Postf.': 'Postfach', 'priv.': 'privat',
             'Prof.': 'Professor', 'prot.': 'protestantisch', 'Prov.': 'Provinz', 'qkm': 'Quadratkilometer', 'qm': 'Quadratmeter', 'Quitt.': 'Quittung', 'rd.': 'rund',
             'Red.': 'Redacteur', 'Reg.': 'Regierung', 'Rep.': 'Republik', 'resp.': 'respektiv', 'Rgt.': 'Regiment', 'Rhld.': 'Rheinland', 'rm.': 'raummeter', 'Rzpt.': 'Rezept',
             'S-Bahn': 'Schnellbahn', 'SB': 'Selbstbedienung', 'SBB': 'Schweizerische Bundesbahn', 's.Br.': 'südliche Breite', 'sek.': 'sekunde', 'Sekr.': 'Sekretär',
             'sel.': 'selig', 'Sem.': 'Semester', 'Sen.': 'Senator', 'sen.': 'senior', 'sfr.': 'Schweizer Franken', 's.g.e.': 'sehr gut erhalten', 'sm.': 'Seemeile',
             'SM': 'Seine Majestät', 'SO': 'Südost', 's.o.': 'siehe oben', 's.u.': 'siehe unten', 'spez.': 'speziell', 'St.': 'Stück', 'städt.': 'städtisch', 'Std.': 'Stunde',
             'stdl.': 'stündlich', 'stellv.': 'stellvertretend', 'StGB': 'Strafgesetzbuch', 'StKl': 'Steuerklasse', 'StPO': 'Strafprozessordnung', 'Str.': 'Strasse',
             'StVO': 'Strassenverkehrsordnung', 'svw.': 'soviel wie', 'SW': 'Südwest', 'sZ': 'seinerzeit', 'SZ': 'Sommerzeit', 't': 'Tonne', 'TA': 'Tierartzt', 'Tab.': 'Tabelle',
             'tägl.': 'täglich', 'Tb.': 'Tuberkulose', 'Teilh.': 'Teilhaber', 'Tel.': 'Telefon', 'TH': 'Technische Hochschule', 'Tnd.': 'Tausend', 'TU': 'Technische Universität',
             'TV': 'Tarifvertrag', 'u.a.': 'unter anderem', 'u.ä.': 'und ähnliches', 'u.A.w.g.': 'um Antwort wird gebeten', 'Übers.': 'Übersetzer', 'übl.': 'üblich',
             'üblw.': 'üblicherweise', 'U-Boot': 'Unterseeboot', 'u.dsgl.': 'und desgleichen', 'u.d.M.': 'unter dem Meeresspiegel', 'ue.': 'unehelich', 'u.E.': 'unseres Erachtens',
             'U/min.': 'Umdrehungen in der Minute', 'Univ.': 'Universität', 'unverk.': 'unverkäuflich', 'urspr.': 'ursprünglich', 'usw.': 'und so weiter', 'u.U.': 'unter Ümständen',
             'u.ü.V.': 'unter üblichem Vorbehalt', 'u.v.a.': 'und veil andere', 'u.W.': 'unseres Wissens', 'u.zw.': 'und zwar', 'v.a.': 'vor allem', 'var.': 'variabel',
             'v.A.w.': 'von Amts wegen', 'v.D.': 'vom Dienst', 'verb.': 'verbessert', 'verh.': 'verheiratet', 'Verl.': 'Verlag', 'Verm.': 'Vermerk', 'verst.': 'verstorben',
             'vgl.': 'vergleiche', 'v.H.': 'vom Hundert', 'v.J.': 'vorigen Jahres', 'v.M.': 'vorigen Monats', 'v.o.': 'von oben', 'Vollm.': 'Vollmacht', 'vollst.': 'vollständig',
             'vorl.': 'vorläufig', 'vorm.': 'vormittags', 'Vors.': 'Vorsitzender', 'v.T.': 'vom Tausend', 'Wb.': 'Wörterbuch', 'WEZ': 'Westeuropäische Zeit', 'Whg.': 'Wohnung',
             'Wkst.': 'Werkstatt', 'w.L.': 'westlicher Länge', 'w.o.': 'wie oben', 'Wz.': 'Warenzeichen', 'z.A.': 'zur Ansicht', 'z.B.': 'zum Beispiel', 'z.d.A.': 'zu den Akten',
             'zgl.': 'zugleich', 'z.H.': 'zu Händen', 'Zi': 'Zimmer', 'Ziff.': 'Ziffer', 'z.K.': 'zur Kenntnisnahme', 'ZPO': 'Zivilprozessordnung', 'z.S.': 'zur See',
             'z.T.': 'zum Teil', 'Ztg.': 'Zeitung', 'zuf.': 'zufolge', 'zus.': 'zusammen', 'zw.': 'zwischen', 'z.w.V.': 'zur weiteren Veranlassung', 'zzgl.': 'zuzüglich',
             'z.Z.': 'zur Zeit'},
    ENGLISH: {'Mr.': 'Mister', 'Mrs.': 'Misses', 'Ms.': 'Miss', 'Dr.': 'Doctor', 'Prof.': 'Professor',
              'etc.': 'et cetera'}
}
