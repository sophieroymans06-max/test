# python
import os
from pathlib import Path
import google.generativeai as genai

# load .env if present (simple loader, no external deps)
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


# Configure API key (make sure you set this in your environment)
# Example in terminal: export GEMINI_API_KEY="your_key_here"
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it as an environment variable.")

# Initialize Gemini
genai.configure(api_key=api_key)

# Choose a model
model = genai.GenerativeModel("gemini-2.5-flash-lite")


def get_gemini_response(prompt: str) -> str:
    """Send a prompt to Gemini and return the response text."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
