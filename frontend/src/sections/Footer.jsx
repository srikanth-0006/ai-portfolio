import "../styles/footer.css";

import { FaGithub, FaLinkedin, FaInstagram } from "react-icons/fa";

export default function Footer() {
  return (
    <footer className="footer">
      <h3>© 2026 Srikanth. All Rights Reserved.</h3>

      <p>Designed and Developed by Srikanth</p>

      <div className="footer-icons">
        <a
          href="https://github.com/srikanth-0006"
          target="_blank"
          rel="noreferrer"
        >
          <FaGithub />
        </a>

        <a
          href="https://www.linkedin.com/in/srikanth-k-139990330?utm_source=share_via&utm_content=profile&utm_medium=member_android"
          target="_blank"
          rel="noreferrer"
        >
          <FaLinkedin />
        </a>

        <a
          href="https://www.instagram.com/_s_r_i_k_a_n_t_h_755?igsh=MW1haDR6N3l1eDdoNA=="
          target="_blank"
          rel="noreferrer"
        >
          <FaInstagram />
        </a>
      </div>
    </footer>
  );
}
