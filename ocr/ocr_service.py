from paddleocr import  PaddleOCR
import numpy as np
from core.models import OCRToken, OCRResult

class OCRService:
    def __init__(self):
        self.ocr = PaddleOCR( lang="en",return_word_box=True)

    def recognize(self, image):
        img = np.array(image)

        result = self.ocr.predict(img)
        results = []

        for res in result:
            tokens = self.parse_tokens(res["text_word"],res["text_word_region"])
            full_text = " ".join(res["rec_texts"])
            ocr_result = OCRResult(tokens, full_text)
            results.append(ocr_result)

        return results

    def parse_tokens(self, words, regions):
        result = []

        for word_list, region_list in zip(words, regions):
            for word, region in zip(word_list, region_list):
                x = min(point[0] for point in region)
                y = min(point[1] for point in region)

                right = max(point[0] for point in region)
                bottom = max(point[1] for point in region)

                width = right - x
                height = bottom - y

                token = OCRToken(
                    text=word,
                    x=x,
                    y=y,
                    width=width,
                    height=height
                )

                result.append(token)

        return result
