import streamlit as st

from graph.workflow import build_graph

from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.dashboard import show_dashboard
from ui.results import show_results
from ui.assistant import show_ai_assistant


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Agri Land Planner AI",
    page_icon="🌾",
    layout="wide"
)

load_css()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "plan_generated" not in st.session_state:
    st.session_state.plan_generated = False

if "result" not in st.session_state:
    st.session_state.result = None

if "farmer_details" not in st.session_state:
    st.session_state.farmer_details = None

if "assistant_messages" not in st.session_state:
    st.session_state.assistant_messages = []


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="header-box">

<h1>🌾 Agri Land Planner AI</h1>

<p>
AI-Powered Agricultural Decision Support System
for Generating an Optimal Cultivation Land Plan
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

(
    district,
    land_size,
    land_unit,
    budget,
    water_source,
    soil_type,
    objective,
    generate
) = render_sidebar()


# --------------------------------------------------
# GENERATE PLAN
# --------------------------------------------------

if generate:

    graph = build_graph()

    initial_state = {

        "messages": [],

        "district": district,
        "land_size": land_size,
        "land_unit": land_unit,

        "budget": budget,

        "water_source": water_source,

        "soil_type": soil_type,

        "objective": objective,

        "land_analysis": "",

        "crop_recommendations": "",

        "budget_analysis": "",

        "cultivation_plan": "",

        "review_feedback": ""

    }

    with st.spinner(
        "🤖 AI Agents are generating the best cultivation plan..."
    ):

        result = graph.invoke(initial_state)

    # Save Result
    st.session_state.result = result

    # Save Inputs
    st.session_state.farmer_details = {

        "district": district,
        "land_size": land_size,
        "land_unit": land_unit,
        "budget": budget,
        "water_source": water_source,
        "soil_type": soil_type,
        "objective": objective

    }

    st.session_state.plan_generated = True

    # Optional: clear old chat when a new plan is generated
    st.session_state.assistant_messages = []
    # --------------------------------------------------
# DISPLAY GENERATED PLAN
# --------------------------------------------------

if st.session_state.plan_generated:

    farmer_details = st.session_state.farmer_details
    result = st.session_state.result

    # Dashboard
    show_dashboard(
        farmer_details["district"],
        farmer_details["land_size"],
        farmer_details["land_unit"],
        farmer_details["budget"],
        farmer_details["water_source"],
        farmer_details["soil_type"],
        farmer_details["objective"]
    )

    st.success("✅ Cultivation plan generated successfully!")

    # Results
    show_results(result)

    # AI Planning Assistant
    show_ai_assistant(
        farmer_details=farmer_details,
        result=result
    )

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

else:

    st.info(
        "👈 Enter your farm details from the sidebar and click **Generate AI Plan**."
    )

    st.markdown("## 🌾 What this system does")

    st.markdown("""
This AI-powered decision support system helps farmers generate an optimal cultivation plan based on:

- 📍 District
- 📏 Land Size
- 💰 Budget
- 💧 Water Source
- 🌱 Soil Type
- 🎯 Farming Objective
""")

    st.markdown("---")

    st.markdown("## 🤖 AI Workflow")

    st.markdown("""
1. 🌍 Land Analysis Agent

2. 🌾 Crop Recommendation Agent

3. 💰 Budget Analysis Agent

4. 📅 Cultivation Planning Agent

5. ✅ Review Agent

6. 💬 AI Planning Assistant
""")

    st.markdown("---")

    st.markdown(
        """
        <center>
            <h3>🌾 Agri Land Planner AI</h3>
            <p>
                Intelligent Multi-Agent Decision Support System
                for Smart Agriculture
            </p>
        </center>
        """,
        unsafe_allow_html=True
    )