from capture.cursor_capture import CursorCapture


capture = CursorCapture()

image = capture.capture_around_cursor()

print(image.size)

image.save("cursor_area.png")