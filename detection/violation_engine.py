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