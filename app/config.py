import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    # --- GEMINI EMBEDDINGS ---
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # --- VECTOR DB (QDRANT) ---
    QDRANT_URL = os.getenv("QDRANT_URL") or os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_API_KEY = (os.getenv("QDRANT_API_KEY") or "").strip()
    QDRANT_COLLECTION = "enterprise_rag"

    # --- OBSERVABILITY (LOGFIRE) ---
    LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN")

    # --- REASONING ENGINE (GROQ) ---
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY") or os.getenv("GROQ_FALLBACK_KEY")

    # --- LLM GATEWAY (PORTKEY) — optional; falls back to direct Groq if unset ---
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    GROQ_SLUG = os.getenv("GROQ_SLUG", "rag")
    GROQ_SLUG_2 = os.getenv("GROQ_SLUG_2", "brag")
