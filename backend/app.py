from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

# =========================
# MONGODB CONNECTION
# =========================

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise Exception("MONGO_URI is missing")

try:
    client = MongoClient(
        mongo_uri,
        serverSelectionTimeoutMS=3000,
        connectTimeoutMS=3000,
        socketTimeoutMS=3000
    )

    # CHECK CONNECTION
    client.admin.command("ping")

    print("MongoDB Connected Successfully")

    db = client["portfolioDB"]

    contacts = db["contacts"]

except Exception as e:

    print("MongoDB Connection Error:", str(e))

    contacts = None

# =========================
# HOME ROUTE
# =========================

@app.route("/")
def home():

    return jsonify({
        "message": "Portfolio Backend Running Successfully"
    })

# =========================
# CONTACT FORM API
# =========================

@app.route("/contact", methods=["POST"])
def contact():

    try:

        if contacts is None:

            return jsonify({
                "success": False,
                "error": "Database connection failed"
            }), 500

        data = request.get_json(force=True)

        if not data:

            return jsonify({
                "success": False,
                "error": "No data received"
            }), 400

        name = data.get("name", "").strip()

        email = data.get("email", "").strip()

        message = data.get("message", "").strip()

        if not name or not email or not message:

            return jsonify({
                "success": False,
                "error": "All fields are required"
            }), 400

        result = contacts.insert_one({

            "name": name,

            "email": email,

            "message": message

        })

        return jsonify({

            "success": True,

            "message": "Message sent successfully",

            "id": str(result.inserted_id)

        }), 200

    except Exception as e:

        print("CONTACT ERROR:", str(e))

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500

# =========================
# AI ASSISTANT API
# =========================

@app.route("/ai", methods=["POST"])
@app.route("/chat", methods=["POST"])
def ai_chat():

    try:

        data = request.get_json(force=True)

        user_message = data.get("message", "").strip()

        if not user_message:

            return jsonify({
                "reply": "Please enter a message."
            }), 400

        msg = user_message.lower()

        if "skill" in msg or "technology" in msg:

            reply = (
                "Srikanth is skilled in React, Flask, MongoDB, Python, "
                "JavaScript, HTML, CSS, GitHub, Framer Motion, and AI integration."
            )

        elif "project" in msg:

            reply = (
                "Srikanth has developed projects like AI Portfolio Assistant, "
                "Farmer Support System, and QR Attendance System."
            )

        elif "about" in msg or "yourself" in msg:

            reply = (
                "Srikanth is an AIML student and Full Stack Developer passionate "
                "about AI and modern web development."
            )

        elif "education" in msg or "study" in msg:

            reply = (
                "Srikanth is currently pursuing AIML "
                "(Artificial Intelligence and Machine Learning)."
            )

        elif "contact" in msg or "linkedin" in msg or "github" in msg:

            reply = (
                "You can connect with Srikanth through GitHub, LinkedIn, "
                "or the contact form available in the portfolio."
            )

        elif "goal" in msg or "career" in msg:

            reply = (
                "Srikanth aims to become a strong Full Stack and AI Developer."
            )

        else:

            reply = (
                "I am Srikanth's Portfolio Assistant. "
                "Please ask about skills, projects, education, contact, or career goals."
            )

        return jsonify({
            "reply": reply
        }), 200

    except Exception as e:

        print("AI ERROR:", str(e))

        return jsonify({
            "reply": "AI Assistant temporarily unavailable."
        }), 500

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )