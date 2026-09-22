import mss
from PIL import Image


class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()
    def capture_screen(self) -> Image.Image:
        monitor = self.sct.monitors[1]
        screenshot = self.sct.grab(monitor)
        return Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )
    def capture_region(
        self,
        x: int,
        y: int,
        width: int,
        height: int
    ) -> Image.Image:
        region = {
            "left": x,
            "top": y,
            "width": width,
            "height": height
        }

        screenshot = self.sct.grab(region)

        return Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )