from graph.state import AgricultureState
from tools.llm import groq_fast
from rag.rag_service import retriever


def budget_analysis_agent(state: AgricultureState):

    crop_summary = state["crop_summary"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Budget: Rs. {state["budget"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Objective: {state["objective"]}

    Crop Summary:
    {crop_summary}
    """

    # Retrieve relevant documents
    retrieved_docs = retriever.search(search_query, k=5)

    rag_context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are an agricultural financial advisor specializing in Sri Lankan farming.

Use the following reference information when preparing the financial analysis.

=========================
REFERENCE INFORMATION
=========================

{rag_context}

=========================
FARMER INFORMATION
=========================

District: {state["district"]}
Land Size: {state["land_size"]} {state["land_unit"]}
Budget: Rs. {state["budget"]}
Objective: {state["objective"]}

=========================
CROP RECOMMENDATION SUMMARY
=========================

{crop_summary}

Generate a professional report in Markdown format.

The report must contain:

# Budget Analysis Report

## 1. Budget Sufficiency
- Is the available budget sufficient?
- Explain why.

## 2. Estimated Cultivation Costs
- Estimated cost for each recommended crop.
- Use reference information where available.

## 3. Expected Return on Investment (ROI)

## 4. Most Profitable Crop
- Explain why.

## 5. Cost Saving Recommendations

## 6. Financial Risks

## 7. Final Financial Recommendation

Base your calculations and recommendations primarily on the provided reference information.

If exact cost figures are not available in the retrieved documents, clearly state that instead of making up values.

===================================================
EXECUTIVE SUMMARY
===================================================

At the end of the report, create a section titled exactly:

## Executive Summary

Requirements:
- Maximum 6 bullet points.
- Include:
  • Budget sufficiency
  • Best ROI crop
  • Estimated financial outlook
  • Main financial risk
  • Cost-saving recommendation
  • Overall financial recommendation
- Keep the summary under 120 words.
- This summary will be used by another AI agent.
"""

    response = groq_fast.invoke(prompt)

    full_report = response.content

    # Store full report
    state["budget_analysis"] = full_report

    # Extract executive summary
    if "## Executive Summary" in full_report:
        summary = full_report.split("## Executive Summary", 1)[1].strip()
    else:
        summary = full_report

    state["budget_summary"] = summary

    return state