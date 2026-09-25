from capture.cursor_capture import CursorCapture
from ocr.ocr_service import OCRService

cursor_capture = CursorCapture()
image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

ocr_service = OCRService()

result = ocr_service.recognize(image)

for res in result:
    print("TEXT:", res["rec_texts"])
    print("WORDS:", res["text_word"])
    print("WORD REGIONS:", res["text_word_region"])