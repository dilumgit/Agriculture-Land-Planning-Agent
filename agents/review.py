from graph.state import AgricultureState
from tools.llm import groq_smart
from rag.rag_service import retriever


def review_agent(state: AgricultureState):

    # Use summaries instead of full reports
    land_summary = state["land_summary"]
    crop_summary = state["crop_summary"]
    budget_summary = state["budget_summary"]
    cultivation_summary = state["cultivation_summary"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Budget: Rs. {state["budget"]}
    Objective: {state["objective"]}

    Cultivation Summary:
    {cultivation_summary}
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
LAND ANALYSIS SUMMARY
==============================

{land_summary}

==============================
CROP RECOMMENDATION SUMMARY
==============================

{crop_summary}

==============================
BUDGET ANALYSIS SUMMARY
==============================

{budget_summary}

==============================
CULTIVATION PLAN SUMMARY
==============================

{cultivation_summary}

Review the complete proposal.

Generate a professional report in Markdown format.

The report must contain:

# Final Review Report

## Recommended Land Allocation

Show the recommended field layout.

For each field include:
- Field Name
- Crop
- Area (using the user's land size)
- Reason for allocation

## Overall Assessment

## Strengths

## Weaknesses

## Possible Risks

## Suggestions for Improvement

## Final Recommendation

## Confidence Level
(High / Medium / Low)

Guidelines

- Use the retrieved reference information wherever applicable.
- If information is unavailable in the retrieved documents, clearly state that.
- Keep the report practical and suitable for Sri Lankan agriculture.
"""

    response = groq_smart.invoke(prompt)

    state["review_feedback"] = response.content

    return state