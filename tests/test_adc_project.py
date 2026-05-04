import os
from pathlib import Path
import google.auth
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path(".secrets/application_default_credentials.json").absolute())
credentials, project = google.auth.default()
print("Project:", project)
