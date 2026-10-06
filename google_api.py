"""Small LLM API project: Q&A app using Google Gemini (free key).

Setup:  pip install google-genai
Run:    python project1.py
"""
from google import genai
import time
API_KEY = "paste_your_api.key"

client = genai.Client(api_key=API_KEY)

question = input("You: ")

response = None 
for attempt in range(5):
    try:
        response = client.models.generate_content(model = "gemini-3.8-flash",contents= question)
        break
    except Exception as e:
        print("busy, retrying...",attempt+1)
        time.sleep(5)
    
# Response comes back: AI model -> API -> program -> screen
if response:
    print("AI:", response.text)
else:
    print("server busy, try again later.")