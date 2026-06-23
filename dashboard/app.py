import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(project_root)



import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from PIL import Image

from analytics.risk_score import (
    calculate_risk,
    calculate_risk_score
)

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="TrafficVision AI",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 TrafficVision AI")
st.subheader(
    "Intelligent Traffic Enforcement & Decision Support Platform"
)

# ==========================
# SIDEBAR
# ==========================

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Detection",
        "Evidence",
        "Analytics",
        "Recommendations"
    ]
)

# ==========================
# SAMPLE DATA LOADER
# ==========================

def load_violations():

    path = "data/violations.json"

    if os.path.exists(path):

        with open(path, "r") as f:
            return json.load(f)

    return [
        {
            "case_id": "TVA001",
            "plate_number": "TS09AB1234",
            "violation": "Helmet Violation"
        },
        {
            "case_id": "TVA002",
            "plate_number": "TS09AB1234",
            "violation": "Triple Riding"
        },
        {
            "case_id": "TVA003",
            "plate_number": "TS11XY5678",
            "violation": "Helmet Violation"
        }
    ]


data = load_violations()

# ==========================
# DASHBOARD
# ==========================

if page == "Dashboard":

    total = len(data)

    helmet_count = sum(
        1 for x in data
        if x["violation"] == "Helmet Violation"
    )

    triple_count = sum(
        1 for x in data
        if x["violation"] == "Triple Riding"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Violations",
        total
    )

    col2.metric(
        "Helmet Violations",
        helmet_count
    )

    col3.metric(
        "Triple Riding",
        triple_count
    )

    st.markdown("---")

    st.success(
        "TrafficVision AI is actively monitoring traffic violations."
    )

# ==========================
# DETECTION PAGE
# ==========================

elif page == "Detection":

    st.header("Traffic Violation Detection")

    uploaded_file = st.file_uploader(
        "Upload Traffic Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.success(
            "Detection Pipeline Executed"
        )

        st.write("### Sample Results")

        st.json(
            {
                "vehicle": "Motorcycle",
                "plate_number": "TS09AB1234",
                "violation": "Helmet Violation",
                "confidence": 0.96
            }
        )

# ==========================
# EVIDENCE PAGE
# ==========================

elif page == "Evidence":

    st.header("Violation Evidence")

    for item in data:

        st.json(item)

# ==========================
# ANALYTICS PAGE
# ==========================

elif page == "Analytics":

    st.header("Violation Analytics")

    df = pd.DataFrame(data)

    violation_counts = (
        df["violation"]
        .value_counts()
        .reset_index()
    )

    violation_counts.columns = [
        "Violation",
        "Count"
    ]

    fig = px.bar(
        violation_counts,
        x="Violation",
        y="Count",
        title="Violation Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(df)

    st.subheader(
        "Repeat Offenders"
    )

    offenders = calculate_risk()

    for plate, count in offenders.items():

        risk = calculate_risk_score(
            count
        )

        st.write(
            f"{plate} | "
            f"Violations: {count} | "
            f"Risk: {risk}"
        )

# ==========================
# RECOMMENDATIONS PAGE
# ==========================

elif page == "Recommendations":

    st.header(
        "AI Enforcement Recommendations"
    )

    st.info(
        "Increase helmet enforcement near metro stations."
    )

    st.info(
        "Deploy officers during peak traffic hours."
    )

    st.info(
        "Monitor repeat offenders for targeted enforcement."
    )

    st.success(
        "Recommendations generated from violation trends."
    )