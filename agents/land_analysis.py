from graph.state import AgricultureState
from tools.llm import groq_fast
from rag.rag_service import retriever


def land_analysis_agent(state: AgricultureState):

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
You are an expert agricultural land analyst specializing in Sri Lankan agriculture.

Use the reference information below when preparing your analysis.

=========================
REFERENCE INFORMATION
=========================

{rag_context}

=========================
USER LAND INFORMATION
=========================

District: {state["district"]}
Land Size: {state["land_size"]} {state["land_unit"]}
Water Source: {state["water_source"]}
Soil Type: {state["soil_type"]}
Objective: {state["objective"]}

Generate a professional report in Markdown format.

The report must contain the following sections:

# Land Analysis Report

## 1. Land Summary

## 2. Climate Analysis
- Temperature
- Rainfall
- Seasonal Suitability

## 3. Soil Analysis
- Suitability
- Advantages
- Limitations

## 4. Water Availability
- Water Source Evaluation
- Irrigation Recommendations

## 5. Opportunities

## 6. Risks

## 7. Overall Suitability Score (0-100)

Base your analysis primarily on the provided reference information whenever it is relevant.

If the reference information does not contain sufficient details for a specific point, clearly state that and use general agricultural knowledge cautiously.

===================================================
EXECUTIVE SUMMARY
===================================================

At the end of the report, create a section titled exactly:

## Executive Summary

Requirements:
- Maximum 6 bullet points.
- Include:
  • Overall land suitability
  • Climate suitability
  • Soil suitability
  • Water availability
  • Main opportunity
  • Main risk
- Keep the summary under 120 words.
- This summary will be used by another AI agent.
"""

    response = groq_fast.invoke(prompt)

    full_report = response.content

    # Store full report
    state["land_analysis"] = full_report

    # Extract executive summary
    if "## Executive Summary" in full_report:
        summary = full_report.split("## Executive Summary", 1)[1].strip()
    else:
        summary = full_report

    state["land_summary"] = summary

    return state