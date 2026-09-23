import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Read API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Fast model (Quick tasks)
groq_fast = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-20b",
    temperature=0
)

# Smart model (Complex reasoning)
groq_smart = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)
