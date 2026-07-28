from graph.state import AgricultureState
from tools.llm import groq_llm
from rag.rag_service import retriever


def budget_analysis_agent(state: AgricultureState):

    crop_recommendations = state["crop_recommendations"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Budget: Rs. {state["budget"]}
    Land Size: {state["land_size"]} {state["land_unit"]}
    Objective: {state["objective"]}

    Crop Recommendations:
    {crop_recommendations}
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
RECOMMENDED CROPS
=========================

{crop_recommendations}

Prepare a professional financial analysis.

Include:

1. Budget Sufficiency
   - Is the available budget sufficient?
   - Explain why.

2. Estimated Cultivation Costs
   - Estimated cost for each recommended crop.
   - Use reference information where available.

3. Expected Return on Investment (ROI)

4. Most Profitable Crop
   - Explain why.

5. Cost Saving Recommendations

6. Financial Risks

7. Final Financial Recommendation

Base your calculations and recommendations primarily on the provided reference information.
If exact cost figures are not available in the retrieved documents, clearly state that instead of making up values.

Return the answer as a professional report.
"""

    response = groq_llm.invoke(prompt)

    state["budget_analysis"] = response.content

    return state