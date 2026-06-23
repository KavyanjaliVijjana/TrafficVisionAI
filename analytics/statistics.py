import json

def get_statistics():

    with open(
        "data/violations.json",
        "r"
    ) as f:

        data = json.load(f)

    total = len(data)

    helmet = 0
    triple = 0

    for row in data:

        if row["violation"] == \
            "Helmet Violation":

            helmet += 1

        if row["violation"] == \
            "Triple Riding":

            triple += 1

    return {

        "total": total,

        "helmet": helmet,

        "triple": triple
    }