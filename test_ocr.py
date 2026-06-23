from detection.plate_ocr import (
    extract_text
)

text = extract_text(
    "test_images/plate.jpeg"
)

print(text)