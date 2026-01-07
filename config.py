import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
GENAI_KEY = os.getenv("GENAI_KEY")
SESSION_STRING = os.getenv("SESSION_STRING")  # For persistent sessions in containers

# Keyword Filter Configuration
KEYWORD_FILTER_STR = os.getenv("KEYWORD_FILTER", "")
KEYWORD_FILTER = [k.strip() for k in KEYWORD_FILTER_STR.split(",") if k.strip()]

# Group Trigger Keywords (Implicit Mentions)
GROUP_TRIGGER_KEYWORDS = [
    'everyone', 
    'all', 
    'channel', 
    'team', 
    'guys', 
    '@everyone', 
    '@all', 
    '@channel'
]
