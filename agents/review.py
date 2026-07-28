from graph.state import AgricultureState
from tools.llm import groq_llm
from rag.rag_service import retriever


def review_agent(state: AgricultureState):

    land_analysis = state["land_analysis"]
    crop_recommendations = state["crop_recommendations"]
    budget_analysis = state["budget_analysis"]
    cultivation_plan = state["cultivation_plan"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Budget: Rs. {state["budget"]}
    Objective: {state["objective"]}

    Cultivation Plan:
    {cultivation_plan}
    """

    # Retrieve relevant documents
    retrieved_docs = retriever.search(search_query, k=6)

    rag_context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are a senior agricultural consultant.

Use the following reference information to review the farming proposal.

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

==============================
CULTIVATION PLAN
==============================

{cultivation_plan}

Review the complete proposal.

First provide:

## Recommended Land Allocation

Show the recommended field layout.

For each field include:
- Field Name
- Crop
- Area (using the user's land size)
- Reason for allocation

Then provide a professional review.

Include:

1. Overall Assessment
2. Strengths
3. Weaknesses
4. Possible Risks
5. Suggestions for Improvement
6. Final Recommendation
7. Confidence Level (High / Medium / Low)

Guidelines

- Use the retrieved reference information wherever applicable.
- If information is unavailable in the retrieved documents, clearly state that.
- Keep the report practical and suitable for Sri Lankan agriculture.

Return a professional report.
"""

    response = groq_llm.invoke(prompt)

    state["review_feedback"] = response.content

    return state