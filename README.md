# LLM API Project

A small Python app that sends a question to the Google Gemini API and prints the AI response.

## How to run
1. pip install google-genai
2. Add your Gemini API key in google_api.py
3. python google_api.py

## How the request moves
The user types a question into my Python program. The program uses the Google GenAI SDK to send an HTTPS request to the Gemini API. The request contains the model name and the user's message, and the API key is sent for authentication. Google's server checks the key, passes the message to the AI model, and the model generates a reply. The reply returns to my program as a response. My program reads the text from the response and prints it on the screen. If the server is busy, the program retries with other models.
