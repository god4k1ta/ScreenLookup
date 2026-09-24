from paddleocr import TextDetection, TextRecognition
import numpy as np

from capture.cursor_capture import CursorCapture


def is_cursor_inside(cursor_x, cursor_y, polygon):
    x_array = []
    y_array = []

    for point in polygon:
        x_array.append(point[0])
        y_array.append(point[1])

    left = min(x_array)
    right = max(x_array)
    top = min(y_array)
    bottom = max(y_array)

    if (left <= cursor_x <= right) and (top <= cursor_y <= bottom):
        return left, right, top, bottom

    return None


def find_region_under_cursor(cursor_x, cursor_y, dt_polys):
    for polygon in dt_polys:
        result = is_cursor_inside(cursor_x, cursor_y, polygon)

        if result is not None:
            return polygon, result

    return None


detection_model = TextDetection()
recognition_model = TextRecognition()
cursor_capture = CursorCapture()


image, cursor_x, cursor_y = cursor_capture.capture_around_cursor()

# PIL.Image → numpy.ndarray
img = np.array(image)

output = detection_model.predict(
    input=img,
    batch_size=1
)

for res in output:
    dt_polys = res["dt_polys"]

    result = find_region_under_cursor(
        cursor_x,
        cursor_y,
        dt_polys
    )

    print(result)

    if result is not None:
        polygon, bounds = result

        left, right, top, bottom = bounds

        cropped = image.crop(
            (left, top, right, bottom)
        )

        cropped.save("crop_screen.png")

        output = recognition_model.predict(
            input="crop_screen.png",
            batch_size=1
        )

        for res in output:
            print(res["rec_text"])