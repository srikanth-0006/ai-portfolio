import "../styles/aichat.css";

import { useState } from "react";

import axios from "axios";

import { motion } from "framer-motion";

export default function AIChat() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = {
      type: "user",
      text: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = message;

    setMessage("");

    setLoading(true);

    try {
      const response = await axios.post(
        "https://portfolio-backend-39kn.onrender.com/ai",
        {
          message: currentMessage,
        },
      );

      const aiMessage = {
        type: "ai",
        text: response.data.reply,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.log("AI ERROR:", error);

      const errorMessage = {
        type: "ai",
        text: "Backend connection failed.",
      };

      setMessages((prev) => [...prev, errorMessage]);
    }

    setLoading(false);
  };

  return (
    <motion.section
      className="chat-section"
      initial={{ opacity: 0 }}
      whileInView={{ opacity: 1 }}
      transition={{ duration: 1 }}
      viewport={{ once: true }}
    >
      <div className="chat-container">
        <motion.h2
          initial={{ opacity: 0, y: -50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
        >
          AI Portfolio Assistant
        </motion.h2>

        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
        >
          Ask anything about technology, coding, projects, AI, or general
          topics.
        </motion.p>

        {/* CHAT AREA */}

        <motion.div
          className="messages-container"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.6 }}
        >
          {messages.map((msg, index) => (
            <motion.div
              key={index}
              className={
                msg.type === "user"
                  ? "message user-message"
                  : "message ai-message"
              }
              initial={{
                opacity: 0,
                y: 20,
              }}
              animate={{
                opacity: 1,
                y: 0,
              }}
              transition={{
                duration: 0.4,
              }}
            >
              {msg.text}
            </motion.div>
          ))}

          {loading && (
            <motion.div
              className="message ai-message"
              animate={{
                opacity: [0.5, 1, 0.5],
              }}
              transition={{
                repeat: Infinity,
                duration: 1,
              }}
            >
              Thinking...
            </motion.div>
          )}
        </motion.div>

        {/* INPUT AREA */}

        <motion.div
          className="chat-input-container"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          <textarea
            placeholder="Ask something..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          ></textarea>

          <button onClick={sendMessage}>Ask AI</button>
        </motion.div>
      </div>
    </motion.section>
  );
}
