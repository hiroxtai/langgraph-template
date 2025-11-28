def main() -> None:
    """LangGraphサンプルアプリケーションのエントリーポイント."""
    from langchain_core.messages import HumanMessage

    from app.graph import graph
    from app.state import AgentState

    # サンプル入力
    initial_state: AgentState = {
        "messages": [HumanMessage(content="LangGraphのテストです")]
    }

    # グラフの実行
    print("=== LangGraph Sample ===")
    first_message = initial_state["messages"][0]
    if hasattr(first_message, "content"):
        content = first_message.content
        if isinstance(content, str):
            print(f"Input: {content}")
    print("\nProcessing...")

    result = graph.invoke(initial_state)

    last_message = result["messages"][-1]
    if hasattr(last_message, "content"):
        output_content = last_message.content
        if isinstance(output_content, str):
            print(f"\nOutput: {output_content}")
    print("\n=== Complete ===")


def demo_streaming() -> None:
    """ストリーミング実行のデモ."""
    from langchain_core.messages import HumanMessage

    from app.graph import graph
    from app.state import AgentState

    print("\n=== Streaming Demo ===")
    initial_state: AgentState = {
        "messages": [HumanMessage(content="ストリーミングテスト")]
    }

    for event in graph.stream(initial_state):
        print(f"Event: {event}")

    print("=== Streaming Complete ===\n")


if __name__ == "__main__":
    main()
