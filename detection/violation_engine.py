# detection/violation_engine.py

def analyze_violations(vehicle_counts):

    violations = []

    motorcycles = vehicle_counts.get(
        "motorcycle", 0
    )

    persons = vehicle_counts.get(
        "person", 0
    )

    if motorcycles > 0:

        if persons >= motorcycles * 3:

            violations.append({

                "type":
                "Triple Riding",

                "severity":
                "High"
            })

    return violations

def helmet_violation_check(
        helmet_detections):

    violations = []

    for item in helmet_detections:

        cls = item["class"].lower()

        if cls in [

            "no_helmet",

            "without_helmet"

        ]:

            violations.append({

                "type":
                "Helmet Violation",

                "severity":
                "High"
            })

    return violations