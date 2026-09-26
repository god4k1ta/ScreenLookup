import time
from PIL import ImageDraw

from capture.cursor_capture import CursorCapture
from ocr.ocr_service import OCRService
from text.text_processor import TextProcessor


cursor_capture = CursorCapture()
ocr_service = OCRService()
processor = TextProcessor()


print("Move cursor to TALK. Starting in 3 seconds...")
time.sleep(3)

mouse_x, mouse_y = cursor_capture.mouse.get_position()
print("ABSOLUTE MOUSE:", mouse_x, mouse_y)

image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

print("LOCAL CURSOR:", cursor_x, cursor_y)
print("MOUSE AFTER CAPTURE:", cursor_capture.mouse.get_position())
print("MSS MONITOR:", cursor_capture.screen_capture.sct.monitors[1])
print("IMAGE SIZE:", image.size)


# Рисуем крест в точке, которую программа считает положением курсора
draw = ImageDraw.Draw(image)

draw.line(
    (cursor_x - 10, cursor_y, cursor_x + 10, cursor_y),
    fill="red",
    width=2
)

draw.line(
    (cursor_x, cursor_y - 10, cursor_x, cursor_y + 10),
    fill="red",
    width=2
)

image.save("debug_capture.png")


results = ocr_service.recognize(image)

print("RESULTS:", len(results))

result = results[0]

for token in result.tokens:
    print(token)


found = processor.find_token_under_cursor(
    result.tokens,
    cursor_x,
    cursor_y
)
same_line_tokens = processor.get_tokens_on_same_line(
    result.tokens,
    found
)

print("SAME LINE:")

for token in same_line_tokens:
    print(token)

print("FOUND:", found)

word = processor.get_token_text(found)
context = processor.build_line_text(same_line_tokens)

print("CONTEXT:", context)
print("FOUND WORD:", word)