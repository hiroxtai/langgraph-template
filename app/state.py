"""State definition for the LangGraph agent."""

from typing import Annotated

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class AgentState(TypedDict):
    """グラフのステート定義.

    Attributes:
        messages: エージェントとユーザー間のメッセージ履歴。
                 add_messagesリデューサーにより、メッセージが追加される。
    """

    messages: Annotated[list[BaseMessage], add_messages]
