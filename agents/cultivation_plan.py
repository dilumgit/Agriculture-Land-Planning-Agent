from graph.state import AgricultureState
from tools.llm import groq_smart
from rag.rag_service import retriever


def cultivation_plan_agent(state: AgricultureState):

    # Use summaries instead of full reports
    land_summary = state["land_summary"]
    crop_summary = state["crop_summary"]
    budget_summary = state["budget_summary"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Budget: Rs. {state["budget"]}
    Objective: {state["objective"]}

    Crop Summary:
    {crop_summary}
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

Generate a professional report in Markdown format.

The report must contain:

# Cultivation Plan

## 1. Recommended Primary Crop

## 2. Recommended Secondary Crop (if suitable)

## 3. Land Preparation

## 4. Planting Schedule

## 5. Irrigation Plan

## 6. Fertilizer Schedule

## 7. Pest and Disease Management

## 8. Harvest Schedule

## 9. Estimated Timeline

## 10. Expected Benefits

## 11. Important Recommendations

Guidelines

- Use the retrieved reference information wherever applicable.
- Keep the plan practical and suitable for Sri Lankan farming conditions.
- If information is unavailable, clearly state that instead of inventing details.

===================================================
EXECUTIVE SUMMARY
===================================================

At the end of the report, create a section titled exactly:

## Executive Summary

Requirements:
- Maximum 6 bullet points.
- Include:
  • Primary recommended crop
  • Secondary crop (if applicable)
  • Planting period
  • Irrigation recommendation
  • Estimated harvest period
  • Overall cultivation recommendation
- Keep the summary under 120 words.
- This summary will be used by another AI agent.
"""

    response = groq_smart.invoke(prompt)

    full_report = response.content

    # Store full report
    state["cultivation_plan"] = full_report

    # Extract executive summary
    if "## Executive Summary" in full_report:
        summary = full_report.split("## Executive Summary", 1)[1].strip()
    else:
        summary = full_report

    state["cultivation_summary"] = summary

    return state