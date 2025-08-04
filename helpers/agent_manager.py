from langgraph.graph import StateGraph, END
from typing import TypedDict, List

from agents.affirm_agent import affirm_agent
from agents.sentiment_agent import sentiment_agent
from agents.escalate_agent import escalate_agent
from agents.neutral_agent import neutral_agent
from agents.positive_agent import positive_agent
from agents.suggest_agent import suggest_agent

class AgentState(TypedDict):
    user_input: str
    sentiment: str
    emotion: str
    response: List[str]

def sentiment_node(state: AgentState) -> AgentState:
    result = sentiment_agent(state["user_input"])
    state["sentiment"] = result["sentiment"]
    state["emotion"] = result["emotion"]
    return state

def positive_node(state: AgentState) -> AgentState:
    result = positive_agent(state["user_input"])
    state["response"].append({
        "agent": "positive",  # change based on the agent
        "response": result["response"]
    })
    return state

def neutral_node(state: AgentState) -> AgentState:
    result = neutral_agent(state["user_input"])
    state["response"].append({
        "agent": "neutral",  # change based on the agent
        "response": result["response"]
    })
    return state

def escalate_node(state: AgentState) -> AgentState:
    result = escalate_agent(state["user_input"])
    state["response"].append({
        "agent": "escalate",  # change based on the agent
        "response": result["response"]
    })

    return state

def affirm_node(state: AgentState) -> AgentState:
    result = affirm_agent(state["user_input"])
    state["response"].append({
        "agent": "affirm",  # change based on the agent
        "response": result["response"]
    })

    return state

def suggest_node(state: AgentState) -> AgentState:
    result = suggest_agent(state["user_input"])
    state["response"].append({
        "agent": "suggest",  # change based on the agent
        "response": result["response"]
    })
    return state

def sentiment_router(state: AgentState) -> str:
    sentiment = state["sentiment"]
    
    if sentiment == "positive":
        return "positive"
    elif sentiment == "neutral":
        return "neutral"
    else:
        emotion = state["emotion"]
        if emotion in ["sadness", "anger", "fear", "disgust"]:
            return "escalate"
        else:
            return "affirm"

workflow = StateGraph(AgentState)

workflow.add_node("sentiment", sentiment_node)

workflow.add_node("positive", positive_node)
workflow.add_node("neutral", neutral_node)
workflow.add_node("escalate", escalate_node)
workflow.add_node("affirm", affirm_node)
workflow.add_node("suggest", suggest_node)


workflow.set_entry_point("sentiment")

workflow.add_conditional_edges(
    "sentiment",
    sentiment_router,
    {
        "positive": "positive",
        "neutral":"neutral",
        "escalate": "escalate",
        "affirm": "affirm"
    }
)

workflow.add_edge("positive", "suggest")
workflow.add_edge("neutral", "suggest")
workflow.add_edge("escalate", "suggest")
workflow.add_edge("affirm", "suggest")
workflow.add_edge("suggest", END)

graph = workflow.compile()

def process_user_message(user_input: str) -> dict:
    initial_state: AgentState = {
        "user_input": user_input,
        "sentiment": "",
        "emotion": "",
        "response": []
    }
    result = graph.invoke(initial_state)
    
    messages = result["response"]
    final_response = messages[0]["response"] if messages else ""
    
    return {
        "final": final_response,
        "all_responses": messages,
        "sentiment": result["sentiment"],
        "emotion": result["emotion"]
    }