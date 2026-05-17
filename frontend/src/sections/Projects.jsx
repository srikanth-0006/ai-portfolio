import "../styles/projects.css";

import { motion } from "framer-motion";

export default function Projects() {
  const projects = [
    {
      title: "AI Portfolio Assistant",

      description:
        "A modern full stack portfolio website integrated with AI chatbot functionality using Gemini AI, Flask backend, and MongoDB database.",

      tech: "React, Flask, MongoDB, Gemini AI",

      github: "https://github.com/YOUR_USERNAME/portfolio-project",

      demo: "https://your-demo-link.vercel.app",
    },

    {
      title: "Farmer Support System",

      description:
        "An intelligent platform designed to support farmers with modern technology solutions and smart assistance features.",

      tech: "React, Python, Flask",

      github: "https://github.com/YOUR_USERNAME/farmer-support-system",

      demo: "https://your-demo-link.vercel.app",
    },

    {
      title: "QR Attendance System",

      description:
        "A QR code based attendance management system that simplifies attendance tracking and improves efficiency.",

      tech: "Python, Flask, QR Code Integration",

      github: "https://github.com/YOUR_USERNAME/qr-attendance-system",

      demo: "https://your-demo-link.vercel.app",
    },
  ];

  return (
    <motion.section className="projects" id="projects">
      <div className="projects-container">
        <h2>Projects</h2>

        <p>
          Some of the projects I have built using modern technologies and AI
          tools.
        </p>

        <div className="projects-grid">
          {projects.map((project, index) => (
            <motion.div
              className="project-card"
              key={index}
              whileHover={{ y: -10 }}
            >
              <h3>{project.title}</h3>

              <p>{project.description}</p>

              <span>{project.tech}</span>

              <div className="project-buttons">
                <a href={project.demo} target="_blank" rel="noreferrer">
                  <button>Live Demo</button>
                </a>

                <a href={project.github} target="_blank" rel="noreferrer">
                  <button>GitHub</button>
                </a>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </motion.section>
  );
}
