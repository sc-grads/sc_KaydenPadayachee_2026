import os
from html import escape

import resend


def _send_email(params):
        api_key = os.getenv("RESEND_API_KEY")
        if not api_key:
                raise RuntimeError("RESEND_API_KEY is not configured")

        resend.api_key = api_key
        return resend.Emails.send(params)


def send_contact_email(name, email, subject, message):
        params = {
                "from": os.getenv("RESEND_FROM_EMAIL", "MorningRun <onboarding@resend.dev>"),
                "to": [os.getenv("SUPPORT_EMAIL")],
                "subject": f"Contact Form: {escape(subject)}",
                "html": f"""
<h2>New Contact Request</h2>
<p><strong>Name:</strong> {escape(name)}</p>
<p><strong>Email:</strong> {escape(email)}</p>
<p><strong>Message:</strong></p>
<p>{escape(message)}</p>
"""
        }

        return _send_email(params)


def send_profile_visit_email(name, email):
        params = {
                "from": os.getenv("RESEND_FROM_EMAIL", "MorningRun <onboarding@resend.dev>"),
                "to": [email],
                "subject": "Your MorningRun profile was opened",
                "html": f"""
<h2>Your MorningRun profile was opened</h2>
<p>Hi {escape(name)},</p>
<p>Your MorningRun profile was opened successfully.</p>
<p>If you did not do this, please change your password and contact support.</p>
"""
        }

        return _send_email(params)