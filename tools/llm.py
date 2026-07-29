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
    model="llama-3.1-8b-instant",
    temperature=0
)

# Smart model (Complex reasoning)
groq_smart = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)