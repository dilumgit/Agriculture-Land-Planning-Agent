from graph.state import AgricultureState
from tools.llm import groq_fast
from rag.rag_service import retriever


def crop_recommendation_agent(state: AgricultureState):

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Objective: {state["objective"]}
    """

    # Retrieve relevant documents
    retrieved_docs = retriever.search(search_query, k=4)

    rag_context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are an expert agricultural crop advisor specializing in Sri Lankan agriculture.

Use the reference information below when recommending crops.

=========================
REFERENCE INFORMATION
=========================

{rag_context}

=========================
LAND ANALYSIS SUMMARY
=========================

{state["land_summary"]}

=========================
USER INFORMATION
=========================

District: {state["district"]}
Land Size: {state["land_size"]} {state["land_unit"]}
Water Source: {state["water_source"]}
Soil Type: {state["soil_type"]}
Objective: {state["objective"]}

Generate a professional report in Markdown format.

The report must contain:

# Crop Recommendation Report

## 1. Best Crop Recommendations
Recommend the most suitable crops.

## 2. Suitability Analysis
Explain why each crop is suitable.

## 3. Expected Yield

## 4. Estimated Profit Potential

## 5. Advantages

## 6. Risks

## 7. Overall Recommendation

Base your recommendations primarily on the provided reference information.

If sufficient information is unavailable, clearly mention it and use general agricultural knowledge cautiously.

===================================================
EXECUTIVE SUMMARY
===================================================

At the end of the report, create a section titled exactly:

## Executive Summary

Requirements:
- Maximum 6 bullet points.
- Include:
  • Best recommended crop
  • Second-best crop
  • Suitability score
  • Profit potential
  • Main cultivation risk
  • Overall recommendation
- Keep the summary under 120 words.
- This summary will be used by another AI agent.
"""

    response = groq_fast.invoke(prompt)

    full_report = response.content

    # Store full report
    state["crop_recommendations"] = full_report

    # Extract executive summary
    if "## Executive Summary" in full_report:
        summary = full_report.split("## Executive Summary", 1)[1].strip()
    else:
        summary = full_report

    state["crop_summary"] = summary

    return state