from paddleocr import  PaddleOCR
import numpy as np


class OCRService:
    def __init__(self):
        self.ocr = PaddleOCR( lang="en",return_word_box=True)

    def recognize(self, image):
        img=np.array(image)

        result = self.ocr.predict(img)
        return result

