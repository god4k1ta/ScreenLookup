from translation.parser import parse_translation_result
from core.models import TranslationResult

data = {
    "translatedText": "разговор",
    "alternatives": ["говорить", "болтать", "разговоры"]
}

result = parse_translation_result("talk", data)

assert isinstance(result, TranslationResult)
assert result.source_text == "talk"
assert result.translation == "разговор"
assert result.alternatives == ["говорить", "болтать", "разговоры"]

print(result)
print("Parser test passed")
