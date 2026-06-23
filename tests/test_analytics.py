from analytics.statistics import (
    get_statistics
)

from analytics.risk_score import (
    calculate_risk
)

from analytics.recommendations import (
    generate_recommendations
)

stats = get_statistics()

risk = calculate_risk()

recs = generate_recommendations(
    stats
)

print()

print("STATISTICS")
print(stats)

print()

print("RISK")
print(risk)

print()

print("RECOMMENDATIONS")
print(recs)