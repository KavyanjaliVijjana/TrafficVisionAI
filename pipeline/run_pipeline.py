import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from detection.helmet_detector import detect_helmet
from detection.violation_engine import helmet_violation_check

helmets = detect_helmet(
    "test_images/test1.jpg"
)

violations = helmet_violation_check(
    helmets
)

print(violations)