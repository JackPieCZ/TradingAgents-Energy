import unittest
from unittest.mock import patch, MagicMock
from tradingagents.llm_clients.google_client import GoogleClient
import google.auth.exceptions


class TestGoogleApiKeyStandardization(unittest.TestCase):
    """Verify GoogleClient accepts unified api_key parameter."""

    @patch("tradingagents.llm_clients.google_client.NormalizedChatGoogleGenerativeAI")
    @patch("google.auth.default", side_effect=google.auth.exceptions.DefaultCredentialsError("Mocked error"))
    def test_api_key_handling(self, mock_auth_default, mock_chat):
        test_cases = [
            ("unified api_key is mapped", {"api_key": "test-key-123"}, "test-key-123"),
            ("legacy google_api_key still works", {"google_api_key": "legacy-key-456"}, "legacy-key-456"),
            ("unified api_key takes precedence", {"api_key": "unified", "google_api_key": "legacy"}, "unified"),
        ]

        for msg, kwargs, expected_key in test_cases:
            with self.subTest(msg=msg):
                mock_chat.reset_mock()
                client = GoogleClient("gemini-2.5-flash", **kwargs)
                client.get_llm()
                call_kwargs = mock_chat.call_args[1]
                # In langchain-google-genai, the parameter can be 'api_key'
                passed_key = call_kwargs.get("api_key") or call_kwargs.get("google_api_key")
                self.assertEqual(passed_key, expected_key)


if __name__ == "__main__":
    unittest.main()
