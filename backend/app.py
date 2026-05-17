from flask import Flask, request, jsonify

from flask_cors import CORS

from pymongo import MongoClient

from dotenv import load_dotenv

import google.generativeai as genai

import os


# LOAD ENV VARIABLES

load_dotenv()


# FLASK APP

app = Flask(__name__)

CORS(app)


# GEMINI CONFIGURATION

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


# GEMINI MODEL

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


# MONGODB CONNECTION

client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["portfolioDB"]

contacts = db["contacts"]


# HOME ROUTE

@app.route("/")

def home():

    return jsonify({
        "message": "Portfolio Backend Running Successfully"
    })


# CONTACT FORM API

@app.route("/contact", methods=["POST"])

def contact():

    try:

        data = request.json

        contacts.insert_one({

            "name": data.get("name"),

            "email": data.get("email"),

            "message": data.get("message")

        })

        return jsonify({

            "success": True,

            "message": "Message sent successfully"

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        })


# AI CHAT API

@app.route("/ai", methods=["POST"])

def ai_chat():

    try:

        data = request.json

        user_message = data.get("message")


        prompt = f"""
You are Srikanth's AI Portfolio Assistant.

ONLY answer questions related to:
- Srikanth
- portfolio
- skills
- projects
- education
- technologies
- contact information
- career goals

If user asks unrelated questions,
reply politely:
"I am designed only for portfolio-related questions."

User Question:
{user_message}
"""


        response = model.generate_content(
            prompt
        )

        return jsonify({

            "reply": response.text

        })

    except Exception as e:

        return jsonify({

            "reply": "AI service temporarily unavailable.",

            "error": str(e)

        })


# RUN SERVER

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )