from pynput.mouse import Controller


class Mouse:
    def __init__(self):
        self.mouse = Controller()

    def get_position(self) -> tuple[int, int]:
        return self.mouse.position