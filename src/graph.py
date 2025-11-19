"""LangGraph graph definition and compilation."""

from langchain_core.messages import BaseMessage
from langgraph.graph import END, START, StateGraph

from src.models import create_chat_model
from src.state import AgentState


def agent_node(state: AgentState) -> dict[str, list[BaseMessage]]:
    """エージェントノード - メッセージを処理して応答を生成.

    Args:
        state: 現在のグラフステート

    Returns:
        更新されたメッセージを含む辞書
    """
    messages = state["messages"]

    # チャットモデルを取得して応答を生成
    llm = create_chat_model()
    response = llm.invoke(messages)

    return {"messages": [response]}


# グラフの構築
workflow = StateGraph(AgentState)

# ノードの追加
workflow.add_node("agent", agent_node)

# エッジの定義
workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)

# グラフのコンパイル
graph = workflow.compile()
