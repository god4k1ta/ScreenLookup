from paddleocr import TextDetection, TextRecognition
from PIL import Image

detection_model = TextDetection()
recognition_model = TextRecognition()

output = detection_model.predict(
    input="cursor_area.png",
    batch_size=1
)

for res in output:
    dt_polys = res["dt_polys"]

    dt_polys_sorted = sorted(
        dt_polys,
        key=lambda poly: min(point[1] for point in poly)
    )

    image = Image.open("cursor_area.png")

    # Берём первый polygon после сортировки
    polygon = dt_polys_sorted[0]

    x_array = []
    y_array = []

    for point in polygon:
        x = point[0]
        y = point[1]

        x_array.append(x)
        y_array.append(y)

    left = min(x_array)
    right = max(x_array)
    top = min(y_array)
    bottom = max(y_array)

    # Вырезаем найденную область
    cropped = image.crop((left, top, right, bottom))
    cropped.save("crop_screen.png")

    # Распознаём вырезанную область
    output2 = recognition_model.predict(
        input="crop_screen.png",
        batch_size=1
    )

    for res2 in output2:
        rec_text = res2["rec_text"]
        print(rec_text)