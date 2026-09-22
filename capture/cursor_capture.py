from capture.screen_capture import ScreenCapture
from input.mouse import Mouse


class CursorCapture:
    def __init__(self):
        self.screen_capture = ScreenCapture()
        self.mouse = Mouse()

    def capture_around_cursor(
        self,
        width: int = 500,
        height: int = 300
    ):
        x, y = self.mouse.get_position()

        left = x - width // 2
        top = y - height // 2

        return self.screen_capture.capture_region(
            left,
            top,
            width,
            height
        )