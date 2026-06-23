import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    result = reader.readtext(image_path)

    texts = []

    for item in result:

        texts.append(item[1])

    return texts