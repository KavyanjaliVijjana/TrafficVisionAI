from datetime import datetime

def generate_report(
        violations):

    return {

        "timestamp":
        str(datetime.now()),

        "violations":
        violations,

        "status":
        "Generated"
    }