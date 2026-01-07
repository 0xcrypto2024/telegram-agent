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

# Auto-Reply Toggle
ENABLE_AUTO_REPLY = os.getenv("ENABLE_AUTO_REPLY", "true").lower() == "true"
# Working Hours (24h format, integer). Auto-reply disabled during these hours.
WORKING_HOURS_START = int(os.getenv("WORKING_HOURS_START", "9"))
WORKING_HOURS_END = int(os.getenv("WORKING_HOURS_END", "18"))

# Long-term Memory Config
ENABLE_LONG_TERM_MEMORY = os.getenv("ENABLE_LONG_TERM_MEMORY", "true").lower() == "true"
MEMORY_FILE_PATH = os.getenv("MEMORY_FILE_PATH", "memory.json")

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
