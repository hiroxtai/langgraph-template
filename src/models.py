"""チャットモデルファクトリ.

このモジュールはチャットモデルのインスタンス作成を担当します。
LangChainの推奨パターンに従い、init_chat_model() を使用して
プロバイダー非依存のモデル作成を実現します。
"""

from functools import lru_cache

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from src.config import settings


@lru_cache(maxsize=1)
def create_chat_model() -> BaseChatModel:
    """チャットモデルを作成するファクトリ関数.

    設定ファイルから読み込んだパラメータを使用してチャットモデルを初期化します。
    @lru_cache によりキャッシュされるため、同じ設定での複数回の呼び出しは
    同一インスタンスを返します。

    Returns:
        設定済みのチャットモデルインスタンス

    Note:
        - init_chat_model() を使用してプロバイダー非依存のモデル作成を実現
        - 設定ファイルから OPENAI_API_KEY を読み込んで使用
        - モデル名から自動的にプロバイダーを推論（gpt-* -> openai）
    """
    return init_chat_model(
        model=settings.openai_model,
        model_provider="openai",
        api_key=settings.openai_api_key.get_secret_value(),
        temperature=settings.openai_temperature,
        timeout=settings.openai_timeout,
    )
