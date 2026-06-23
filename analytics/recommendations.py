def generate_recommendations(
        stats):

    recommendations = []

    if stats["helmet"] > 5:

        recommendations.append(

            "Increase helmet "
            "enforcement checks"
        )

    if stats["triple"] > 3:

        recommendations.append(

            "Deploy officers "
            "near high-risk roads"
        )

    return recommendations