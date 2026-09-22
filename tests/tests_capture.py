from capture.screen_capture import ScreenCapture

capture = ScreenCapture()
image = capture.capture_screen()
print(image.size)
image.save("screen.png")