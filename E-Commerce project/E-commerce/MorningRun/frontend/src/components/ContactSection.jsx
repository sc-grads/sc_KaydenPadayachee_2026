import { useState } from "react";
function ContactSection() {
const [formData, setFormData] = useState({
name: "",
email: "",
subject: "",
message: "",
});
const [status, setStatus] = useState("");
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
setStatus("");
try {
  const response = await fetch("http://127.0.0.1:5000/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  });
  const data = await response.json();
  if (response.ok) {
    setStatus("Message sent successfully!");
    setFormData({
      name: "",
      email: "",
      subject: "",
      message: "",
    });
  } else {
    setStatus(data.message || "Something went wrong.");
  }
} catch (error) {
  console.error("Contact form error:", error);
  setStatus("Unable to send message. Please try again.");
} finally {
  setLoading(false);
}
};
return (
<section id="contact" className="contact-section">
<div className="contact-content">
<p className="section-kicker">Get in touch</p>
    <h2>Have any queries?</h2>
    <p>Contact us and we will be happy to help.</p>
    <div className="contact-details">
      <a href="tel:08345872" className="contact-detail">
        <span>Phone</span>
        <strong>08345872</strong>
      </a>
      <a href="mailto:FixUs@gmail.com" className="contact-detail">
        <span>Email</span>
        <strong>FixUs@gmail.com</strong>
      </a>
    </div>
    <form onSubmit={handleSubmit} className="contact-form">
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
      <input
        type="text"
        name="subject"
        placeholder="Subject"
        value={formData.subject}
        onChange={handleChange}
        required
      />
      <textarea
        name="message"
        placeholder="Your Message"
        value={formData.message}
        onChange={handleChange}
        rows="6"
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? "Sending..." : "Send Message"}
      </button>
      {status && <p className="contact-status">{status}</p>}
    </form>
  </div>
</section>
);
}
export default ContactSection;