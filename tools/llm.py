import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter

# Load environment variables
load_dotenv()

# Read API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Groq LLM
groq_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0
)

# OpenRouter LLM
openrouter_llm = ChatOpenRouter(
    api_key=OPENROUTER_API_KEY,
    model="nemotron-3-ultra-550b-a55b:free",
    temperature=0
)