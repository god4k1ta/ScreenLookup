from capture.cursor_capture import CursorCapture
from ocr.ocr_service import OCRService

cursor_capture = CursorCapture()
image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

ocr_service = OCRService()

result = ocr_service.recognize(image)

for res in result:
    print("TEXT:", res.full_text)
    print("TOKENS:", res.tokens)