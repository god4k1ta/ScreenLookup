from capture.cursor_capture import CursorCapture
from ocr.ocr_service import OCRService


cursor_capture = CursorCapture()
ocr_service = OCRService()

image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

ocr_service.find_and_recognize_under_cursor(
    image,
    cursor_x,
    cursor_y
)