from translation.service import translate_text
from core.models import TranslationResult

result = translate_text("I am learning Norwegian")

assert isinstance(result, TranslationResult)
assert result.source_text == "I am learning Norwegian"
assert result.translation
assert isinstance(result.alternatives, list)

print(result)
print("Service test passed")
