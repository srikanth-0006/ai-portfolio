import "../styles/about.css";

import { motion } from "framer-motion";

export default function About() {
  return (
    <motion.section
      className="about"
      id="about"
      initial={{ opacity: 0, y: 100 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 1 }}
      viewport={{ once: true }}
    >
      <div className="about-container">
        <motion.h2
          initial={{ opacity: 0, y: -50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          viewport={{ once: true }}
        >
          About Me
        </motion.h2>

        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
          viewport={{ once: true }}
        >
          I am an AIML student and passionate Full Stack Developer who enjoys
          building modern web applications and AI-powered solutions. I
          continuously learn new technologies and focus on creating scalable,
          responsive, and user-friendly applications. My interests include
          Artificial Intelligence, Web Development, Backend Systems, and
          Intelligent Automation.
        </motion.p>

        <motion.p
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ delay: 0.6 }}
          viewport={{ once: true }}
        >
          I enjoy building responsive web applications, AI-powered systems, and
          scalable backend solutions using React, Flask, and MongoDB.
        </motion.p>

        <div className="about-cards">
          <motion.div
            className="about-card"
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8 }}
            viewport={{ once: true }}
          >
            <h3>Frontend</h3>

            <p>React, HTML, CSS, JavaScript</p>
          </motion.div>

          <motion.div
            className="about-card"
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: 1 }}
            viewport={{ once: true }}
          >
            <h3>Backend</h3>

            <p>Python, Flask, APIs</p>
          </motion.div>

          <motion.div
            className="about-card"
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: 1.2 }}
            viewport={{ once: true }}
          >
            <h3>Database</h3>

            <p>MongoDB, Data Management</p>
          </motion.div>
        </div>
      </div>
    </motion.section>
  );
}
