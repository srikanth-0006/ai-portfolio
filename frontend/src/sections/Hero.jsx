import "../styles/hero.css";

import { motion } from "framer-motion";

import profile from "../assets/profile.jpeg";

export default function Hero() {
  return (
    <motion.section
      className="hero"
      id="home"
      initial={{ opacity: 0, y: 100 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 1 }}
    >
      <div className="hero-left">
        <motion.h1>Srikanth</motion.h1>

        <motion.h2>AIML Student | Full Stack Developer</motion.h2>

        <motion.p>
          I build modern and intelligent web applications using AI, React,
          Flask, and scalable full stack technologies.
        </motion.p>

        <div className="hero-buttons">
          <a href="#projects">
            <button>View Projects</button>
          </a>

          <a href="#contact">
            <button>Contact Me</button>
          </a>
        </div>
      </div>

      <motion.div
        className="hero-right"
        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 1 }}
      >
        <div className="profile-container">
          <img src={profile} alt="Profile" className="profile-image" />

          <p>Profile</p>
        </div>
      </motion.div>
    </motion.section>
  );
}
