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

    # Structured outputs
    land_analysis: dict
    crop_recommendations: dict
    budget_analysis: dict
    cultivation_plan: dict
    review_feedback: dict