from detection.violation_engine import (
    analyze_violations
)

from utils.report_generator import (
    generate_report
)

vehicle_counts = {

    "motorcycle": 1,
    "person": 3
}

violations = analyze_violations(
    vehicle_counts
)

report = generate_report(
    violations
)

print(report)