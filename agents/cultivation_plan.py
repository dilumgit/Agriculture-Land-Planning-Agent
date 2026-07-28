from graph.state import AgricultureState
from tools.llm import groq_llm
from rag.rag_service import retriever


def cultivation_plan_agent(state: AgricultureState):

    land_analysis = state["land_analysis"]
    crop_recommendations = state["crop_recommendations"]
    budget_analysis = state["budget_analysis"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Budget: Rs. {state["budget"]}
    Objective: {state["objective"]}

    Recommended Crops:
    {crop_recommendations}
    """

    # Retrieve relevant documents
    retrieved_docs = retriever.search(search_query, k=6)

    rag_context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are a senior agricultural planning consultant specializing in Sri Lankan farming.

Use the following reference information when preparing the cultivation plan.

==============================
REFERENCE INFORMATION
==============================

{rag_context}

==============================
LAND ANALYSIS
==============================

{land_analysis}

==============================
CROP RECOMMENDATIONS
==============================

{crop_recommendations}

==============================
BUDGET ANALYSIS
==============================

{budget_analysis}

Prepare a practical cultivation plan.

Include the following sections.

1. Recommended Primary Crop
2. Recommended Secondary Crop (if suitable)
3. Land Preparation
4. Planting Schedule
5. Irrigation Plan
6. Fertilizer Schedule
7. Pest and Disease Management
8. Harvest Schedule
9. Estimated Timeline
10. Expected Benefits
11. Important Recommendations

Guidelines

- Use the retrieved reference information wherever applicable.
- Keep the plan practical and suitable for Sri Lankan farming conditions.
- If some information is unavailable in the reference documents, clearly mention that instead of inventing details.

Write the report professionally using headings and bullet points.
"""

    response = groq_llm.invoke(prompt)

    state["cultivation_plan"] = response.content

    return state