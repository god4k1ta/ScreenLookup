from translation.api import translation_text

result = translation_text("talk")

print(result["translatedText"])
print(result.get("alternatives", []))
print(result.get("detectedLanguage"))
