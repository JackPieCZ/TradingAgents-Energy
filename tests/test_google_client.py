from tradingagents.llm_clients.google_client import GoogleClient

client = GoogleClient('gemini-2.5-flash')
try:
    llm = client.get_llm()
    print("Success! LLM instantiated with ADC.")
except Exception as e:
    print("Error:", e)
