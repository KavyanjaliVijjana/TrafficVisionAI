from detection.helmet_detector import (
    detect_helmet
)

from detection.violation_engine import (
    helmet_violation_check
)

result = detect_helmet(
    "test_images/test1.jpg"
)

print(result)

violation = helmet_violation_check(
    result["helmets"],
    result["no_helmets"]
)

print(violation)