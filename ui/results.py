import streamlit as st


def show_results(result):

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "🌱 Land Analysis",
            "🌾 Crop Recommendations",
            "💰 Budget Analysis",
            "📅 Cultivation Plan",
            "✅ Final Review"
        ]
    )

    # ----------------------------
    # Land Analysis
    # ----------------------------
    with tab1:

        st.subheader("🌱 Land Analysis")

        with st.expander("View Land Analysis", expanded=True):
            st.markdown(result.get("land_analysis", "No data available."))

    # ----------------------------
    # Crop Recommendations
    # ----------------------------
    with tab2:

        st.subheader("🌾 Crop Recommendations")

        with st.expander("View Crop Recommendations", expanded=True):
            st.markdown(result.get("crop_recommendations", "No data available."))

    # ----------------------------
    # Budget Analysis
    # ----------------------------
    with tab3:

        st.subheader("💰 Budget Analysis")

        with st.expander("View Budget Analysis", expanded=True):
            st.markdown(result.get("budget_analysis", "No data available."))

    # ----------------------------
    # Cultivation Plan
    # ----------------------------
    with tab4:

        st.subheader("📅 Cultivation Plan")

        with st.expander("View Cultivation Plan", expanded=True):
            st.markdown(result.get("cultivation_plan", "No data available."))

    # ----------------------------
    # Final Review
    # ----------------------------
    with tab5:

        st.subheader("✅ Final Review")

        with st.expander("View Final Recommendation", expanded=True):
            st.markdown(result.get("review_feedback", "No data available."))