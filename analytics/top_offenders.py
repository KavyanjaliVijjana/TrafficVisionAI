# analytics/top_offenders.py

import json

def get_top_offenders():

    with open(
        "data/violations.json",
        "r"
    ) as f:

        data = json.load(f)

    offenders = {}

    for row in data:

        plate = row["plate_number"]

        offenders[plate] = (
            offenders.get(
                plate,
                0
            ) + 1
        )

    return sorted(
        offenders.items(),
        key=lambda x: x[1],
        reverse=True
    )