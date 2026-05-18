import "../styles/contact.css";

import { useState } from "react";

import axios from "axios";

export default function Contact() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post(
        "https://portfolio-backend-39kn.onrender.com/contact",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
          timeout: 20000,
        },
      );

      if (response.data?.success) {
        alert("Message Sent Successfully!");
        setFormData({
          name: "",
          email: "",
          message: "",
        });
      } else {
        alert(response.data?.error || "Failed to send message");
      }
    } catch (error) {
      console.log("CONTACT ERROR:", error?.response?.data || error.message);
      alert(error?.response?.data?.error || "Failed to send message");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="contact" id="contact">
      <div className="contact-container">
        <h2>Contact Me</h2>

        <p>
          Feel free to connect with me regarding internships, collaborations,
          projects, or technology discussions.
        </p>

        <form className="contact-form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            placeholder="Your Name"
            value={formData.name}
            onChange={handleChange}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Your Email"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <textarea
            name="message"
            placeholder="Your Message"
            rows="6"
            value={formData.message}
            onChange={handleChange}
            required
          ></textarea>

          <button type="submit" disabled={loading}>
            {loading ? "Sending..." : "Send Message"}
          </button>
        </form>

        <div className="social-links">
          <a
            href="https://github.com/srikanth-0006"
            target="_blank"
            rel="noreferrer"
          >
            GitHub
          </a>

          <a
            href="https://www.linkedin.com/in/srikanth-k-139990330?utm_source=share_via&utm_content=profile&utm_medium=member_android"
            target="_blank"
            rel="noreferrer"
          >
            LinkedIn
          </a>
        </div>
      </div>
    </section>
  );
}
