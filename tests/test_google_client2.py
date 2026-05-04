import os
from tradingagents.llm_clients.google_client import GoogleClient

os.environ["GOOGLE_CLOUD_PROJECT"] = "my-test-project"
client = GoogleClient('gemini-2.5-flash')
try:
    llm = client.get_llm()
    print("Success! LLM instantiated with ADC.")
except Exception as e:
    print("Error:", type(e), e)
