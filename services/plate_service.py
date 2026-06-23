from detection.plate_ocr import (
    extract_text
)

from utils.plate_formatter import (
    clean_plate
)

def get_plate_number(
        image_path):

    raw_text = extract_text(
        image_path
    )

    plate = clean_plate(
        raw_text
    )

    return plate