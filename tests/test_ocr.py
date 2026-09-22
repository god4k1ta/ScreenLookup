from paddleocr import TextRecognition
model = TextRecognition()
output = model.predict(input="cursor_area.png", batch_size=1)
for res in output:
    res.print()
    res.save_to_img(save_path="./output/")
    res.save_to_json(save_path="./output/res.json")
