from paddleocr import TextDetection
model = TextDetection()
output = model.predict(input="cursor_area.png", batch_size=1)
for res in output:
    dt_polys = res["dt_polys"]

    for polygon in dt_polys:
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

        print(left, top, right, bottom)
    res.print()
    res.save_to_img(save_path="./output/")
    res.save_to_json(save_path="./output/res.json")