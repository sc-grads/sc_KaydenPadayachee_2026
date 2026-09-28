from flask import Blueprint, request
 
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
 
from werkzeug.security import (
    check_password_hash,
    generate_password_hash,
)
 
from models import User, PasswordResetToken, db
from datetime import datetime, timedelta
import secrets
 
from logger import logger
from services.email_service import send_profile_visit_email
 
 
def create_auth_blueprint():
 
    auth_bp = Blueprint("auth", __name__)
 
    # ---------------------------------------------------------
    # REGISTER
    # ---------------------------------------------------------
 
    @auth_bp.route("/register", methods=["POST"])
    def register():
 
        data = request.get_json() or {}
 
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        security_question = data.get("security_question")
        security_answer = data.get("security_answer")
 
        if not first_name or not last_name or not email or not password:
            return {
                "message": "First name, last name, email and password are required."
            }, 400
 
        if not security_question or not security_answer:
            return {
                "message": "Security question and answer are required."
            }, 400
 
        if User.query.filter_by(email=email).first():
            return {
                "message": "A user with this email already exists."
            }, 409
 
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=generate_password_hash(password),
            role="customer",
            security_question=security_question,
            security_answer=security_answer.strip().lower(),
        )
 
        db.session.add(user)
        db.session.commit()
 
        logger.info(
            "USER_REGISTERED | Email: %s | Role: %s",
            user.email,
            user.role
        )
 
        return {
            "message": "Registration successful!",
            "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email,
                "role": user.role,
            },
        }, 201
 
    # ---------------------------------------------------------
    # LOGIN
    # ---------------------------------------------------------
 
    @auth_bp.route("/login", methods=["POST"])
    def login():
 
        data = request.get_json() or {}
 
        email = data.get("email")
        password = data.get("password")
 
        if not email or not password:
            return {
                "message": "Email and password are required."
            }, 400
 
        user = User.query.filter_by(email=email).first()
 
        if not user or not check_password_hash(
            user.password,
            password
        ):
            logger.warning(
                "USER_LOGIN_FAILED | Email: %s",
                email or "unknown"
            )
 
            return {
                "message": "Invalid email or password."
            }, 401
 
        access_token = create_access_token(
            identity=str(user.id)
        )
 
        logger.info(
            "USER_LOGIN | Email: %s | Role: %s",
            user.email,
            user.role
        )
 
        return {
            "message": "Login successful!",
            "access_token": access_token,
            "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email,
                "role": user.role,
            },
        }, 200
 
    # ---------------------------------------------------------
    # PROFILE
    # ---------------------------------------------------------
 
    @auth_bp.route("/profile", methods=["GET"])
    @jwt_required()
    def profile():
 
        user = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "full_name": f"{user.first_name} {user.last_name}",
            "email": user.email,
            "role": user.role,
            "phone": user.phone,
            "address": user.address,
            "suburb": user.suburb,
            "city": user.city,
            "province": user.province,
            "postal_code": user.postal_code,
        }, 200
 
    @auth_bp.route("/profile/visit", methods=["POST"])
    @jwt_required()
    def profile_visit():
 
        user = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        try:
            send_profile_visit_email(
                f"{user.first_name} {user.last_name}",
                user.email,
            )
 
        except Exception:
            logger.exception(
                "PROFILE_VISIT_EMAIL_FAILED | Email: %s",
                user.email
            )
 
            return {
                "message": "Profile loaded, but the email could not be sent."
            }, 502
 
        logger.info(
            "PROFILE_VISIT_EMAIL_SENT | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "Profile visit email sent successfully."
        }, 200
 
    @auth_bp.route("/profile", methods=["PUT"])
    @jwt_required()
    def update_profile():
 
        user = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        data = request.get_json() or {}
 
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
 
        if not first_name or not last_name or not email:
            return {
                "message": "First name, last name and email are required."
            }, 400
 
        existing_user = User.query.filter(
            User.email == email,
            User.id != user.id
        ).first()
 
        if existing_user:
            return {
                "message": "That email address is already being used."
            }, 409
 
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = data.get("phone")
        user.address = data.get("address")
        user.suburb = data.get("suburb")
        user.city = data.get("city")
        user.province = data.get("province")
        user.postal_code = data.get("postal_code")
 
        db.session.commit()
 
        logger.info(
            "PROFILE_UPDATED | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "Profile updated successfully!",
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "full_name": f"{user.first_name} {user.last_name}",
                "email": user.email,
                "role": user.role,
                "phone": user.phone,
                "address": user.address,
                "suburb": user.suburb,
                "city": user.city,
                "province": user.province,
                "postal_code": user.postal_code,
            },
        }, 200
 
    @auth_bp.route("/profile/password", methods=["PUT"])
    @jwt_required()
    def update_password():
 
        user = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        data = request.get_json() or {}
 
        current_password = data.get("current_password")
        new_password = data.get("new_password")
 
        if not current_password or not new_password:
            return {
                "message": "Current and new passwords are required."
            }, 400
 
        if not check_password_hash(
            user.password,
            current_password
        ):
            return {
                "message": "Current password is incorrect."
            }, 400
 
        if len(new_password) < 8:
            return {
                "message": "New password must be at least 8 characters."
            }, 400
 
        user.password = generate_password_hash(new_password)
 
        db.session.commit()
 
        logger.info(
            "PASSWORD_CHANGED | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "Password changed successfully."
        }, 200
 
    # ---------------------------------------------------------
    # ADMIN CUSTOMERS
    # ---------------------------------------------------------
 
    @auth_bp.route("/admin/customers", methods=["GET"])
    @jwt_required()
    def get_customers():
 
        admin = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not admin:
            return {
                "message": "User not found."
            }, 404
 
        if admin.role != "admin":
            return {
                "message": "Admin access required."
            }, 403
 
        customers = User.query.filter_by(
            role="customer"
        ).order_by(
            User.id.desc()
        ).all()
 
        return {
            "customers": [
                {
                    "id": customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "full_name": f"{customer.first_name} {customer.last_name}",
                    "email": customer.email,
                    "role": customer.role,
                }
                for customer in customers
            ]
        }, 200
 
    @auth_bp.route("/admin/customers/<int:user_id>", methods=["DELETE"])
    @jwt_required()
    def delete_customer(user_id):
 
        admin = db.session.get(
            User,
            int(get_jwt_identity())
        )
 
        if not admin:
            return {
                "message": "User not found."
            }, 404
 
        if admin.role != "admin":
            return {
                "message": "Admin access required."
            }, 403
 
        customer = db.session.get(
            User,
            user_id
        )
 
        if not customer:
            return {
                "message": "Customer not found."
            }, 404
 
        if customer.role != "customer":
            return {
                "message": "Only customer accounts can be deleted here."
            }, 400
 
        customer_id = customer.id
        customer_email = customer.email
 
        db.session.delete(customer)
        db.session.commit()
 
        logger.info(
            "CUSTOMER_DELETED | Customer ID: %s | Email: %s | Admin ID: %s",
            customer_id,
            customer_email,
            admin.id
        )
 
        return {
            "message": "Customer account deleted successfully!"
        }, 200
 
    # ---------------------------------------------------------
    # FORGOT PASSWORD
    # ---------------------------------------------------------
 
    @auth_bp.route("/forgot-password/question", methods=["POST"])
    def get_security_question():
 
        data = request.get_json() or {}
        email = data.get("email")
 
        if not email:
            return {
                "message": "Email is required."
            }, 400
 
        user = User.query.filter_by(
            email=email
        ).first()
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        logger.info(
            "SECURITY_QUESTION_REQUESTED | Email: %s",
            email
        )
 
        return {
            "user_id": user.id,
            "security_question": user.security_question,
        }, 200
 
    @auth_bp.route("/forgot-password/verify", methods=["POST"])
    def verify_security_answer():
 
        data = request.get_json() or {}
 
        user_id = data.get("user_id")
        answer = data.get("security_answer")
 
        if not user_id or not answer:
            return {
                "message": "User ID and security answer are required."
            }, 400
 
        user = db.session.get(
            User,
            user_id
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        if user.security_answer.strip().lower() != answer.strip().lower():
 
            logger.warning(
                "SECURITY_ANSWER_FAILED | User ID: %s",
                user.id
            )
 
            return {
                "message": "Incorrect answer."
            }, 400
 
        logger.info(
            "SECURITY_ANSWER_VERIFIED | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "Verified"
        }, 200
 
    @auth_bp.route("/forgot-password/reset", methods=["POST"])
    def reset_password_with_security_answer():
 
        data = request.get_json() or {}
 
        user_id = data.get("user_id")
        new_password = data.get("new_password")
 
        if not user_id or not new_password:
            return {
                "message": "User ID and new password are required."
            }, 400
 
        user = db.session.get(
            User,
            user_id
        )
 
        if not user:
            return {
                "message": "User not found."
            }, 404
 
        user.password = generate_password_hash(
            new_password
        )
 
        db.session.commit()
 
        logger.info(
            "PASSWORD_RESET_SECURITY | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "Password changed successfully."
        }, 200
 
    @auth_bp.route("/forgot-password", methods=["POST"])
    def forgot_password():
 
        data = request.get_json() or {}
        email = data.get("email")
 
        if not email:
            return {
                "message": "Email is required."
            }, 400
 
        user = User.query.filter_by(
            email=email
        ).first()
 
        # We return the same message whether the email exists
        # or not. This prevents people from checking which
        # emails are registered in the system.
 
        if not user:
 
            logger.info(
                "PASSWORD_RESET_REQUESTED | Email not found: %s",
                email
            )
 
            return {
                "message": "If an account with that email exists, a password reset link has been sent."
            }, 200
 
        # Invalidate any previous unused reset tokens
 
        old_tokens = PasswordResetToken.query.filter_by(
            user_id=user.id,
            used=False
        ).all()
 
        for old_token in old_tokens:
            old_token.used = True
 
        # Generate a secure random token
 
        reset_token = secrets.token_urlsafe(32)
 
        # Token expires after 30 minutes
 
        expires_at = datetime.utcnow() + timedelta(
            minutes=30
        )
 
        password_reset = PasswordResetToken(
            user_id=user.id,
            token=reset_token,
            expires_at=expires_at,
            used=False
        )
 
        db.session.add(password_reset)
        db.session.commit()
 
        logger.info(
            "PASSWORD_RESET_REQUESTED | User ID: %s | Email: %s",
            user.id,
            user.email
        )
 
        return {
            "message": "If an account with that email exists, a password reset link has been sent.",
            "reset_token": reset_token
        }, 200
 
    # ---------------------------------------------------------
    # RESET PASSWORD
    # ---------------------------------------------------------
 
    @auth_bp.route(
        "/reset-password/<token>",
        methods=["POST"]
    )
    def reset_password_token(token):
 
        data = request.get_json() or {}
        new_password = data.get("password")
 
        if not new_password:
            return {
                "message": "New password is required."
            }, 400
 
        reset_record = PasswordResetToken.query.filter_by(
            token=token,
            used=False
        ).first()
 
        if not reset_record:
            return {
                "message": "Invalid or expired reset token."
            }, 400
 
        # Check whether the token has expired
 
        if datetime.utcnow() > reset_record.expires_at:
 
            reset_record.used = True
            db.session.commit()
 
            logger.warning(
                "PASSWORD_RESET_EXPIRED | Token expired"
            )
 
            return {
                "message": "Password reset successful. You can now log in with your new password."
            }, 200
 
    return auth_bp