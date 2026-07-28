from tools.llm import groq_llm


def planning_assistant(
    farmer_details: dict,
    result: dict,
    user_question: str,
):

    prompt = f"""
You are an expert Agricultural AI Planning Assistant.

The following cultivation plan has already been generated.

===================================================
FARMER DETAILS
===================================================

District : {farmer_details["district"]}
Land Size : {farmer_details["land_size"]} {farmer_details["land_unit"]}
Budget : Rs. {farmer_details["budget"]}
Water Source : {farmer_details["water_source"]}
Soil Type : {farmer_details["soil_type"]}
Objective : {farmer_details["objective"]}

===================================================
LAND ANALYSIS
===================================================

{result["land_analysis"]}

===================================================
CROP RECOMMENDATIONS
===================================================

{result["crop_recommendations"]}

===================================================
BUDGET ANALYSIS
===================================================

{result["budget_analysis"]}

===================================================
CULTIVATION PLAN
===================================================

{result["cultivation_plan"]}

===================================================
FINAL REVIEW
===================================================

{result["review_feedback"]}

===================================================
USER QUESTION
===================================================

{user_question}

===================================================

Instructions

- Answer ONLY based on the cultivation plan above.
- Explain recommendations clearly.
- If the user asks for another crop, compare it with the current recommendation.
- If the user changes the budget, land size or objective, provide an updated recommendation.
- Be practical and professional.
- Use Markdown.
- Keep the answer concise and useful.
"""

    response = groq_llm.invoke(prompt)

    return response.content