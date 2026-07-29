from tools.llm import groq_smart


def planning_assistant(
    farmer_details: dict,
    result: dict,
    user_question: str,
):

    prompt = f"""
You are an expert Agricultural AI Planning Assistant.

Use the following executive summaries to answer the user's question.

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
LAND SUMMARY
===================================================

{result["land_summary"]}

===================================================
CROP SUMMARY
===================================================

{result["crop_summary"]}

===================================================
BUDGET SUMMARY
===================================================

{result["budget_summary"]}

===================================================
CULTIVATION SUMMARY
===================================================

{result["cultivation_summary"]}

===================================================
FINAL REVIEW
===================================================

{result["review_feedback"]}

===================================================
USER QUESTION
===================================================

{user_question}

Instructions

- Answer ONLY using the summaries above.
- If the user changes the budget, land size, or objective, update the recommendation accordingly.
- Keep the response concise.
- Use Markdown.
"""

    response = groq_smart.invoke(prompt)

    return response.content