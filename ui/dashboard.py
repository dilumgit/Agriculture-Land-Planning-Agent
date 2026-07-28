import streamlit as st


def show_dashboard(
    district,
    land_size,
    land_unit,
    budget,
    water_source,
    soil_type,
    objective,
):
    st.markdown("## 📊 Farm Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📍 District",
            value=district
        )

    with col2:
        st.metric(
            label="🌱 Land Size",
            value=f"{land_size} {land_unit}"
        )

    with col3:
        st.metric(
            label="💰 Budget",
            value=f"Rs. {budget:,.0f}"
        )

    with col4:
        st.metric(
            label="🎯 Objective",
            value=objective
        )

    st.markdown("")

    col5, col6 = st.columns(2)

    with col5:
        st.info(f"💧 **Water Source**\n\n{water_source}")

    with col6:
        st.info(f"🌾 **Soil Type**\n\n{soil_type}")

    st.divider()