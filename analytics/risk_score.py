import json

def calculate_risk():

    with open(
        "data/violations.json",
        "r"
    ) as f:

        data = json.load(f)

    offenders = {}

    for row in data:

        plate = row[
            "plate_number"
        ]

        offenders[plate] = (
            offenders.get(
                plate,
                0
            ) + 1
        )

    return offenders