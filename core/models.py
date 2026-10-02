from dataclasses import dataclass


@dataclass
class OCRToken:
    text: str
    x: int
    y: int
    width: int
    height: int


@dataclass
class OCRResult:
    tokens: list[OCRToken]
    full_text: str
    language: str | None = None


@dataclass
class WordInfo:
    word: str
    pronunciation: str | None
    translation: str
    definition: str | None


@dataclass
class LookupResult:
    word_info: WordInfo
    context: str | None
    context_translation: str | None


@dataclass
class Pronunciation:
    text : str
    audio : str


@dataclass
class Phonetics:
    uk : Pronunciation
    us : Pronunciation


@dataclass
class Definition:
    part_of_speech: str
    definition : str
    examples : list[str]


@dataclass
class DictionaryEntry:
    word : str
    phonetics : Phonetics
    definitions : list[Definition]
