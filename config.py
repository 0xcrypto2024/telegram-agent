import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
GENAI_KEY = os.getenv("GENAI_KEY")
SESSION_STRING = os.getenv("SESSION_STRING")  # For persistent sessions in containers
