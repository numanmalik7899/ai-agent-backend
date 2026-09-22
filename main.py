import os
from fastapi import FastAPI
from google import genai

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


@app.get("/")
def home():
  return {"status": "AI Agent Server is Running!"}


@app.get("/generate")
def generate_post(topic: str):
  prompt = f"Facebook page ke liye '{topic}' par ek engaging post aur trending hashtags Urdu/Roman Urdu me likho."
  response = client.models.generate_content(
      model="gemini-2.5-flash", contents=prompt
  )
  return {"topic": topic, "content": response.text}
