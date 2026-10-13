from core.models import (TranslationResult)


def parse_translation_result(source_text, translation):
    translation_result = translation["translatedText"]
    alternatives = translation.get("alternatives", [])
    return TranslationResult(
        source_text=source_text,
        translation=translation_result,
        alternatives=alternatives
    )
