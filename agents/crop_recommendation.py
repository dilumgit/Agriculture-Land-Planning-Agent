from graph.state import AgricultureState
from tools.llm import groq_llm
from rag.rag_service import retriever


def crop_recommendation_agent(state: AgricultureState):

    land_analysis = state["land_analysis"]

    # Create search query
    search_query = f"""
    District: {state["district"]}
    Soil Type: {state["soil_type"]}
    Water Source: {state["water_source"]}
    Objective: {state["objective"]}

    Land Analysis:
    {land_analysis}
    """

    # Retrieve relevant documents
    retrieved_docs = retriever.search(search_query, k=5)

    rag_context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are an experienced agricultural consultant specializing in Sri Lankan agriculture.

Use the following reference information when making recommendations.

=========================
REFERENCE INFORMATION
=========================

{rag_context}

=========================
LAND ANALYSIS
=========================

{land_analysis}

Recommend the best crops for this land.

Requirements

- Recommend the 3 most suitable crops.
- Rank them from most suitable to least suitable.

For each crop provide:

1. Crop Name
2. Suitability Score (/100)
3. Why it is suitable
4. Expected growing period
5. Estimated cultivation cost (if available in the reference information)
6. Advantages
7. Possible risks
8. Profit potential

Base your recommendations primarily on the provided reference information whenever possible.
If some information is not available in the retrieved documents, clearly mention that instead of inventing values.

Return the answer as a professional report.
"""

    response = groq_llm.invoke(prompt)

    state["crop_recommendations"] = response.content

    return state