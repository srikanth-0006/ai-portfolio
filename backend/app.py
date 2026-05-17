from flask import Flask, request, jsonify

from flask_cors import CORS

from pymongo import MongoClient

from dotenv import load_dotenv

import google.generativeai as genai

import os

# LOAD ENV VARIABLES

load_dotenv()

# GEMINI CONFIGURATION

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# GEMINI MODEL

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# FLASK APP

app = Flask(__name__)

CORS(app)

# MONGODB CONNECTION

client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["portfolioDB"]

contacts_collection = db["contacts"]

# HOME ROUTE

@app.route("/")

def home():

    return {
        "message": "Backend Running Successfully"
    }

# CONTACT FORM ROUTE

@app.route("/contact", methods=["POST"])

def contact():

    data = request.json

    contacts_collection.insert_one({

        "name": data["name"],
        "email": data["email"],
        "message": data["message"]

    })

    return jsonify({

        "message": "Message Stored Successfully"

    })

# AI CHAT ROUTE

@app.route("/chat", methods=["POST"])

def chat():

    try:

        user_message = request.json["message"].lower()

        # PREDEFINED RESPONSES

        if "skill" in user_message:

            reply = """
            Srikanth is skilled in:
            React, Flask, MongoDB, Python,
            JavaScript, AI Integration,
            Frontend and Backend Development.
            """

        elif "project" in user_message:

            reply = """
            Srikanth's major projects are:
            1. AI Portfolio Assistant
            2. Farmer Support System
            3. QR Attendance System
            """

        elif "about" in user_message:

            reply = """
            Srikanth is an AIML student and Full Stack Developer
            passionate about AI-powered applications.
            """

        elif "contact" in user_message:

            reply = """
            You can contact Srikanth using the
            contact form available in this portfolio.
            """

        elif "technology" in user_message:

            reply = """
            Technologies used in this portfolio:
            React, Flask, MongoDB,
            Framer Motion, Gemini AI.
            """

        elif "education" in user_message:

            reply = """
            Srikanth is currently pursuing AIML
            (Artificial Intelligence and Machine Learning).
            """

        else:

            prompt = f"""

            You are Srikanth's Portfolio AI Assistant.

            Answer ONLY portfolio-related questions.

            Keep answers short, professional,
            and portfolio-focused.

            Portfolio Information:

            - AIML Student
            - Full Stack Developer
            - Skilled in React, Flask, MongoDB, Python
            - Built AI Portfolio Assistant
            - Built Farmer Support System
            - Built QR Attendance System

            User Question:
            {user_message}

            """

            response = model.generate_content(prompt)

            reply = response.text

        return jsonify({

            "reply": reply

        })

    except Exception:

        return jsonify({

            "reply":
            "Portfolio assistant is temporarily busy. Please try again."

        })

# RUN APP

if __name__ == "__main__":

    app.run(debug=True)