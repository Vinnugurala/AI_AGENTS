from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()  # reads GEMINI_API_KEY from environment
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain an API in one sentence."
)
print(response.text)