from core.models import OCRToken, OCRResult
from text.text_processor import TextProcessor


processor = TextProcessor()

tokens = [
    # So talk to me.
    OCRToken("So", 100, 100, 20, 20),
    OCRToken("talk", 125, 100, 30, 20),
    OCRToken("to", 160, 100, 15, 20),
    OCRToken("me", 180, 100, 20, 20),
    OCRToken(".", 205, 100, 5, 20),

    # Just listen please.
    OCRToken("Just", 100, 130, 30, 20),
    OCRToken("listen", 135, 130, 40, 20),
    OCRToken("please", 180, 130, 40, 20),
    OCRToken(".", 225, 130, 5, 20),
]


# 1. Поиск токена под курсором

found = processor.find_token_under_cursor(
    tokens,
    140,
    110
)

assert found is not None
assert found.text == "talk"


# 2. Получение токенов той же строки

same_line = processor.get_tokens_on_same_line(
    tokens,
    found
)

assert [token.text for token in same_line] == [
    "So", "talk", "to", "me", "."
]


# 3. Сборка строки

line = processor.build_line_text(same_line)

assert line == "So talk to me."


# 4. Получение контекста

context = processor.get_context(
    tokens,
    found
)

assert context == "So talk to me."


# 5. Получение текста найденного токена

word = processor.get_token_text(found)

assert word == "talk"


# 6. Проверка None

assert processor.get_token_text(None) is None
assert processor.get_context(tokens, None) == ""


# 7. Проверяем вторую строку

second_token = processor.find_token_under_cursor(
    tokens,
    150,
    140
)

assert second_token is not None
assert second_token.text == "listen"

second_context = processor.get_context(
    tokens,
    second_token
)

assert second_context == "Just listen please."


# 8. Проверяем process()

ocr_result = OCRResult(
    tokens=tokens,
    full_text="So talk to me. Just listen please."
)

word, context = processor.process(
    ocr_result,
    140,
    110
)

assert word == "talk"
assert context == "So talk to me."


# 9. process() при отсутствии токена

word, context = processor.process(
    ocr_result,
    50,
    50
)

assert word is None
assert context == ""


print("All TextProcessor tests passed.")