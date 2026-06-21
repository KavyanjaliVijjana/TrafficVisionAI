# test_full_pipeline.py

from detection.vehicle_detector import detect_vehicles
from detection.violation_engine import (
    triple_riding_check
)

detections, counts = detect_vehicles(
    "test_images/test1.jpg"
)

violations = triple_riding_check(
    counts
)

print("Detections")
print(detections)

print("Counts")
print(counts)

print("Violations")
print(violations)