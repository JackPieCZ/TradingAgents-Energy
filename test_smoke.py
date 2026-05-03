from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
import copy

config = copy.deepcopy(DEFAULT_CONFIG)
config.update({
    "data_vendors": {"price_data": "mock", "system_data": "mock", "weather_data": "mock"},
    "llm_provider": "openai",
    "deep_think_llm": "gpt-4o-mini",
    "quick_think_llm": "gpt-4o-mini",
})

from unittest.mock import patch
from langchain_core.language_models import FakeListChatModel

class PatchedFakeListChatModel(FakeListChatModel):
    def bind_tools(self, tools, **kwargs):
        return self

fake_llm = PatchedFakeListChatModel(responses=["This is a mock response from the LLM.", "Mock response 2", "Mock response 3", "Mock response 4", "Mock response 5", "Mock response 6", "Mock response 7", "Mock response 8", "Mock response 9", "Mock response 10", "Mock response 11", "Mock response 12"])

class MockClient:
    def get_llm(self):
        return fake_llm

def mock_create_llm_client(*args, **kwargs):
    return MockClient()

with patch('tradingagents.graph.trading_graph.create_llm_client', side_effect=mock_create_llm_client):
    graph = TradingAgentsGraph(config=config)
    state, signal = graph.propagate(
        delivery_period="2026-05-01",
        trade_timestamp="2026-04-30T18:00",
        market_area="CZ"
    )

    assert state["market_report"] != ""
    assert state["sentiment_report"] != ""
    assert state["news_report"] != ""
    assert state["fundamentals_report"] != ""
    assert state["final_trade_decision"] != ""
    print("Smoke Test 1 passed!")
    print("Signal:", signal)

