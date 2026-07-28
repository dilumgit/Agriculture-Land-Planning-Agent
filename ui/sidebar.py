import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/wheat.png",
            width=70
        )

        st.title("Agri Land Planner AI")
        st.caption("AI-Powered Agricultural Decision Support System")

        st.markdown("---")

        st.subheader("📍 Farm Information")

        districts = [
            "Ampara",
            "Anuradhapura",
            "Badulla",
            "Batticaloa",
            "Colombo",
            "Galle",
            "Gampaha",
            "Hambantota",
            "Jaffna",
            "Kalutara",
            "Kandy",
            "Kegalle",
            "Kilinochchi",
            "Kurunegala",
            "Mannar",
            "Matale",
            "Matara",
            "Monaragala",
            "Mullaitivu",
            "Nuwara Eliya",
            "Polonnaruwa",
            "Puttalam",
            "Ratnapura",
            "Trincomalee",
            "Vavuniya"
        ]
        district = st.selectbox(
            "District",
            options=districts,
            index=districts.index("Kurunegala")  # Default selection
        )

        land_size = st.number_input(
            "Land Size",
            min_value=0.1,
            value=2.0,
            step=0.5
        )

        land_unit = st.selectbox(
            "Land Unit",
            ["Acres", "Hectares"]
        )

        budget = st.number_input(
            "Budget (Rs.)",
            min_value=10000,
            value=500000,
            step=10000
        )

        water_source = st.selectbox(
            "Water Source",
            [
                "Well",
                "Canal",
                "Tank",
                "Rain"
            ]
        )

        soil_type = st.selectbox(
            "Soil Type",
            [
                "Loamy",
                "Clay",
                "Sandy"
            ]
        )

        objective = st.selectbox(
            "Objective",
            [
                "Maximum Profit",
                "Balanced",
                "Minimum Water Usage"
            ]
        )

        st.markdown("---")

        generate = st.button(
            "🚀 Generate AI Plan",
            use_container_width=True
        )

    return (
        district,
        land_size,
        land_unit,
        budget,
        water_source,
        soil_type,
        objective,
        generate
    )