from capture.cursor_capture import CursorCapture
from paddleocr import PaddleOCR
import numpy as np

cursor_capture = CursorCapture()

image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

ocr = PaddleOCR(
    lang="en",
    return_word_box=True
)

result = ocr.predict(np.array(image))

for res in result:
    print("TEXT:", res["rec_texts"])
    print("WORDS:", res["text_word"])
    print("WORD REGIONS:", res["text_word_region"])
    print("WORD BOXES:", res["text_word_boxes"])