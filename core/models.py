from dataclasses import dataclass


@dataclass
class OCRWord:
    text: str
    x: int
    y: int
    width: int
    height: int
    confidence: float


@dataclass
class OCRResult:
    words: list[OCRWord]
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