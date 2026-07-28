from graph.state import AgricultureState
from tools.llm import groq_llm
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

Generate a professional report with the following sections.

1. Land Summary

2. Climate Analysis
- Temperature
- Rainfall
- Seasonal suitability

3. Soil Analysis
- Suitability
- Advantages
- Limitations

4. Water Availability
- Water source evaluation
- Irrigation recommendations

5. Opportunities

6. Risks

7. Overall Suitability Score (0-100)

Base your analysis primarily on the provided reference information whenever it is relevant.
If the reference information does not contain sufficient details for a specific point, clearly state that and use general agricultural knowledge cautiously.

Return a professional report.
"""

    response = groq_llm.invoke(prompt)

    state["land_analysis"] = response.content

    return state