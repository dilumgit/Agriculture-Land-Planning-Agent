from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class AgricultureState(TypedDict):

    messages: Annotated[list, add_messages]

    district: str
    land_size: float
    land_unit: str
    budget: float
    water_source: str
    soil_type: str
    objective: str

    # Full reports
    land_analysis: str
    crop_recommendations: str
    budget_analysis: str
    cultivation_plan: str
    review_feedback: str

    # Executive summaries
    land_summary: str
    crop_summary: str
    budget_summary: str
    cultivation_summary: str