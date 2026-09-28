import hashlib
import os
from urllib.parse import quote_plus

from flask import Blueprint, redirect, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import CartItem, Order, User, db
from logger import logger


def create_payfast_blueprint():
    payfast_bp = Blueprint("payfast", __name__)

    @payfast_bp.route(
        "/payfast/payment/<int:order_id>",
        methods=["GET"]
    )
    @jwt_required()
    def create_payment(order_id):
        user_id = int(get_jwt_identity())

        order = Order.query.filter_by(
            id=order_id,
            user_id=user_id
        ).first()

        if not order:
            logger.warning("Payment failed for order %s: order not found", order_id)
            return {
                "message": "Order not found."
            }, 404

        if order.payment_status == "paid":
            logger.warning("Payment failed for order %s: already paid", order_id)
            return {
                "message": "This order has already been paid."
            }, 400

        user = db.session.get(User, user_id)

        if not user:
            return {
                "message": "User not found."
            }, 404

        merchant_id = os.getenv("PAYFAST_MERCHANT_ID")
        merchant_key = os.getenv("PAYFAST_MERCHANT_KEY")
        return_url = (
            f"{os.getenv('PAYFAST_RETURN_URL')}"
            f"?order_id={order.id}"
        )
        cancel_url = os.getenv("PAYFAST_CANCEL_URL")
        notify_url = os.getenv("PAYFAST_NOTIFY_URL")
        amount = f"{float(order.total_amount):.2f}"

        # Keep this order exactly as PayFast expects for custom signing.
        payment_data = {
            "merchant_id": merchant_id,
            "merchant_key": merchant_key,
            "return_url": return_url,
            "cancel_url": cancel_url,
            "notify_url": notify_url,
            "name_first": order.shipping_first_name,
            "name_last": order.shipping_last_name,
            "email_address": user.email,
            "m_payment_id": str(order.id),
            "amount": amount,
            "item_name": f"MorningRun Order #{order.id}",
        }

        payment_data = {
            key: value
            for key, value in payment_data.items()
            if value is not None and str(value).strip() != ""
        }

        parameter_string = "&".join(
            f"{key}={quote_plus(str(value).strip())}"
            for key, value in payment_data.items()
        )

        passphrase = os.getenv("PAYFAST_PASSPHRASE")

        if passphrase:
            parameter_string += (
                f"&passphrase={quote_plus(passphrase.strip())}"
            )

        signature = hashlib.md5(
            parameter_string.encode("utf-8")
        ).hexdigest()

        payment_data["signature"] = signature

        return {
            "payment_url": os.getenv("PAYFAST_SANDBOX_URL"),
            "payment_data": payment_data,
        }, 200

    @payfast_bp.route("/payfast/success")
    def payfast_success():
        order_id = request.args.get("order_id")

        if not order_id:
            return {
                "message": "Order ID missing"
            }, 400

        try:
            order_id = int(order_id)
        except (TypeError, ValueError):
            return {
                "message": "Invalid order ID"
            }, 400

        order = db.session.get(Order, order_id)

        if not order:
            return {
                "message": "Order not found"
            }, 404

        if order.payment_status != "paid":
            order.payment_status = "paid"
            order.status = "Processing"

            cart_items = CartItem.query.filter_by(
                user_id=order.user_id
            ).all()

            for item in cart_items:
                if item.product:
                    item.product.stock -= item.quantity

                db.session.delete(item)

            db.session.commit()
            logger.info("Payment successful for order %s", order.id)

        return redirect(
            "http://localhost:5173/payment-success"
        )

    return payfast_bp
