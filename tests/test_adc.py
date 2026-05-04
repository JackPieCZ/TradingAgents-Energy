import os
from pathlib import Path

secrets_adc = Path(".secrets/application_default_credentials.json")
if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") and secrets_adc.exists():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(secrets_adc.absolute())

try:
    import google.auth
    credentials, project = google.auth.default()
    print("Success! Credentials found:", type(credentials))
except Exception as e:
    print("Error:", e)
