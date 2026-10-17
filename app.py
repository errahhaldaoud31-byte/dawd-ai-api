from flask import Flask, request
import os
from openai import OpenAI
app = Flask(__name__)
@app.route("/")
def home():
    return "DAWD AI khdam"
@app.route("/chat")
def chat():
    q = request.args.get("message", "salam")
    try:
        client = OpenAI(api_key=os.environ.get("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")
        response = client.chat.completions.create(model="llama-3.1-8b-instant", messages=[{"role": "user", "content": q}], max_tokens=400)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
