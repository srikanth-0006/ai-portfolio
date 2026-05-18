from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# LOAD ENV VARIABLES
load_dotenv()

# FLASK APP
app = Flask(__name__)

# ENABLE CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# MONGODB CONNECTION
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["portfolioDB"]

contacts = db["contacts"]


# HOME ROUTE
@app.route("/")
def home():

    return jsonify({
        "message": "Portfolio Backend Running Successfully"
    })


# CONTACT FORM ROUTE
@app.route("/contact", methods=["POST"])
def contact():

    try:

        data = request.get_json(force=True)

        contacts.insert_one({

            "name": data.get("name", ""),
            "email": data.get("email", ""),
            "message": data.get("message", "")

        })

        return jsonify({

            "success": True,
            "message": "Message sent successfully"

        }), 200

    except Exception as e:

        print("CONTACT ERROR:", str(e))

        return jsonify({

            "success": False,
            "error": "Failed to send message"

        }), 500


# AI RESPONSE FUNCTION
def portfolio_reply(user_message):

    msg = user_message.lower().strip()

    # SKILLS
    if "skill" in msg or "technology" in msg:

        return (
            "Srikanth is skilled in React, Flask, MongoDB, "
            "Python, JavaScript, HTML, CSS, GitHub, "
            "Framer Motion, and AI integration."
        )

    # PROJECTS
    elif "project" in msg:

        return (
            "Srikanth has developed projects like "
            "AI Portfolio Assistant, Farmer Support System, "
            "and QR Attendance System."
        )

    # ABOUT
    elif "about" in msg or "yourself" in msg:

        return (
            "Srikanth is an AIML student and Full Stack Developer "
            "passionate about AI and modern web development."
        )

    # EDUCATION
    elif "education" in msg or "study" in msg:

        return (
            "Srikanth is currently pursuing AIML "
            "(Artificial Intelligence and Machine Learning)."
        )

    # CONTACT
    elif "contact" in msg or "linkedin" in msg or "github" in msg:

        return (
            "You can connect with Srikanth through "
            "GitHub, LinkedIn, or the contact form "
            "available in the portfolio."
        )

    # CAREER
    elif "goal" in msg or "career" in msg:

        return (
            "Srikanth aims to become a strong "
            "Full Stack and AI Developer."
        )

    # DEFAULT
    else:

        return (
            "I am Srikanth's Portfolio Assistant. "
            "Please ask about skills, projects, "
            "education, contact, or career goals."
        )


# AI CHAT ROUTE
@app.route("/ai", methods=["POST"])
@app.route("/chat", methods=["POST"])
def ai_chat():

    try:

        data = request.get_json(force=True)

        user_message = data.get("message", "")

        if not user_message.strip():

            return jsonify({
                "reply": "Please enter a message."
            }), 400

        reply = portfolio_reply(user_message)

        return jsonify({
            "reply": reply
        }), 200

    except Exception as e:

        print("AI ERROR:", str(e))

        return jsonify({
            "reply": "AI Assistant temporarily unavailable."
        }), 500


# RUN SERVER
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )