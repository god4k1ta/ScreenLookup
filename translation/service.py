from translation.api import translation_text
from translation.parser import parse_translation_result
from core.models import TranslationResult


def translate_text(source_text: str) -> TranslationResult:
    data = translation_text(source_text)
    result = parse_translation_result(source_text, data)
    return result
