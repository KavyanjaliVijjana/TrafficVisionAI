from analytics.recommendations import (
    generate_recommendations
)

stats = {

    "helmet":10,

    "triple":5
}

print(
    generate_recommendations(
        stats
    )
)