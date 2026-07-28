from langgraph.graph import StateGraph, END

from graph.state import AgricultureState

from agents.land_analysis import land_analysis_agent
from agents.crop_recommendation import crop_recommendation_agent
from agents.budget_analysis import budget_analysis_agent
from agents.cultivation_plan import cultivation_plan_agent
from agents.review import review_agent


def build_graph():

    workflow = StateGraph(AgricultureState)

    workflow.add_node("land_analysis", land_analysis_agent)
    workflow.add_node("crop_recommendation", crop_recommendation_agent)
    workflow.add_node("budget_analysis", budget_analysis_agent)
    workflow.add_node("cultivation_plan", cultivation_plan_agent)
    workflow.add_node("review", review_agent)

    workflow.set_entry_point("land_analysis")

    workflow.add_edge("land_analysis", "crop_recommendation")
    workflow.add_edge("crop_recommendation", "budget_analysis")
    workflow.add_edge("budget_analysis", "cultivation_plan")
    workflow.add_edge("cultivation_plan", "review")
    workflow.add_edge("review", END)

    return workflow.compile()