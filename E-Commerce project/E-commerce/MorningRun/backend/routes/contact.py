from flask import Blueprint, request, jsonify

from services.email_service import send_contact_email
 
contact_bp = Blueprint("contact", __name__)
 
@contact_bp.route("/contact", methods=["POST"])

def contact():
 
    data = request.get_json()
 
    name = data.get("name")

    email = data.get("email")

    subject = data.get("subject")

    message = data.get("message")
 
    send_contact_email(

        name,

        email,

        subject,

        message

    )
 
    return jsonify({

        "message": "Message sent successfully"

    }), 200
 