from detection.violation_engine import (
    triple_riding_check
)

vehicle_counts = {

    "motorcycle": 1,
    "person": 3
}

violations = (
    triple_riding_check(
        vehicle_counts
    )
)

print(violations)