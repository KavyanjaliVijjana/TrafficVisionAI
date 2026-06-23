import re

def clean_plate(texts):

    for text in texts:

        plate = re.sub(
            r'[^A-Z0-9]',
            '',
            text.upper()
        )

        if len(plate) >= 8:

            return plate

    return "UNKNOWN"