from flask import Blueprint, request

from flask_jwt_extended import get_jwt_identity, jwt_required

from models import CartItem, Order, OrderItem, User, db
from logger import logger


def create_orders_blueprint():

    orders_bp = Blueprint("orders", __name__)

    statuses = [
        "Processing",
        "Packed",
        "Ready for Dispatch",
        "Shipped",
        "Out for Delivery",
        "Delivered",
        "Cancelled",
    ]

    def require_admin():
        admin = db.session.get(User, int(get_jwt_identity()))
        return admin if admin and admin.role == "admin" else None

    @orders_bp.route("/orders/checkout", methods=["POST"])
    @jwt_required()
    def checkout():

        user_id = int(get_jwt_identity())

        data = request.get_json() or {}

        shipping_first_name = data.get("shipping_first_name")
        shipping_last_name = data.get("shipping_last_name")
        shipping_phone = data.get("shipping_phone")
        shipping_address = data.get("shipping_address")
        shipping_suburb = data.get("shipping_suburb")
        shipping_city = data.get("shipping_city")
        shipping_province = data.get("shipping_province")
        shipping_postal_code = data.get("shipping_postal_code")
        payment_account_holder = data.get("payment_account_holder")
        payment_account_number = data.get("payment_account_number")

        required_fields = [
            shipping_first_name,
            shipping_last_name,
            shipping_phone,
            shipping_address,
            shipping_suburb,
            shipping_city,
            shipping_province,
            shipping_postal_code,
            payment_account_holder,
            payment_account_number,
        ]

        if any(
            not field or not str(field).strip()
            for field in required_fields
        ):
            return {
                "message": "All checkout fields are required."
            }, 400

        cart_items = CartItem.query.filter_by(
            user_id=user_id
        ).all()

        if not cart_items:
            return {
                "message": "Cart is empty."
            }, 400

        total = 0

        for item in cart_items:
            if not item.product:
                return {
                    "message": "A product in your cart could not be found."
                }, 404

            if item.product.stock < item.quantity:
                return {
                    "message": f"Not enough stock for {item.product.name}."
                }, 400

            total += float(item.product.price) * item.quantity

        order = Order(
            user_id=user_id,
            total_amount=total,
            status="Processing",
            payment_status="pending",
            shipping_first_name=shipping_first_name,
            shipping_last_name=shipping_last_name,
            shipping_phone=shipping_phone,
            shipping_address=shipping_address,
            shipping_suburb=shipping_suburb,
            shipping_city=shipping_city,
            shipping_province=shipping_province,
            shipping_postal_code=shipping_postal_code,
            payment_account_holder=payment_account_holder,
            payment_account_number=payment_account_number
        )

        db.session.add(order)
        db.session.flush()

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product.id,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
                subtotal=float(item.product.price) * item.quantity
            )

            db.session.add(order_item)

        db.session.commit()
        logger.info("Order created: %s by user %s", order.id, user_id)

        return {
            "message": "Order created successfully.",
            "order_id": order.id,
            "total": total,
            "payment_status": order.payment_status
        }, 201

    @orders_bp.route("/orders", methods=["GET"])
    @jwt_required()
    def get_orders():

        user_id = int(get_jwt_identity())

        orders = Order.query.filter_by(
            user_id=user_id
        ).order_by(
            Order.created_at.desc()
        ).all()

        return [
            {
                "id": order.id,
                "total_amount": float(order.total_amount),
                "status": order.status,
                "payment_status": order.payment_status,
                "estimated_delivery": (
                    order.estimated_delivery.isoformat()
                    if order.estimated_delivery else None
                ),
                "shipping_address": order.shipping_address,
                "shipping_suburb": order.shipping_suburb,
                "shipping_city": order.shipping_city,
                "shipping_province": order.shipping_province,
                "shipping_postal_code": order.shipping_postal_code,
                "items": [
                    {
                        "product_name": item.product_name,
                        "price": float(item.price),
                        "quantity": item.quantity,
                        "subtotal": float(item.subtotal)
                    }
                    for item in order.items
                ],
                "created_at": order.created_at.isoformat()
            }
            for order in orders
        ], 200

    @orders_bp.route("/orders/<int:order_id>", methods=["GET"])
    @jwt_required()
    def get_order(order_id):

        user_id = int(get_jwt_identity())

        order = Order.query.filter_by(
            id=order_id,
            user_id=user_id
        ).first()

        if not order:
            return {
                "message": "Order not found."
            }, 404

        return {
            "id": order.id,
            "total_amount": float(order.total_amount),
            "status": order.status,
            "payment_status": order.payment_status,
            "estimated_delivery": (
                order.estimated_delivery.isoformat()
                if order.estimated_delivery else None
            ),
            "shipping_first_name": order.shipping_first_name,
            "shipping_last_name": order.shipping_last_name,
            "shipping_phone": order.shipping_phone,
            "shipping_address": order.shipping_address,
            "shipping_suburb": order.shipping_suburb,
            "shipping_city": order.shipping_city,
            "shipping_province": order.shipping_province,
            "shipping_postal_code": order.shipping_postal_code,
            "items": [
                {
                    "product_name": item.product_name,
                    "price": float(item.price),
                    "quantity": item.quantity,
                    "subtotal": float(item.subtotal)
                }
                for item in order.items
            ],
            "created_at": order.created_at.isoformat()
        }, 200

    @orders_bp.route("/admin/orders", methods=["GET"])
    @jwt_required()
    def get_all_orders():
        if require_admin() is None:
            return {"message": "Admin access required."}, 403

        orders = Order.query.order_by(Order.created_at.desc()).all()
        return [
            {
                "id": order.id,
                "customer": {
                    "name": f"{order.user.first_name} {order.user.last_name}",
                    "email": order.user.email,
                },
                "total_amount": float(order.total_amount),
                "status": order.status,
                "payment_status": order.payment_status,
                "estimated_delivery": (
                    order.estimated_delivery.isoformat()
                    if order.estimated_delivery else None
                ),
                "created_at": order.created_at.isoformat(),
                "items": [
                    {
                        "product_name": item.product_name,
                        "quantity": item.quantity,
                    }
                    for item in order.items
                ],
            }
            for order in orders
        ], 200

    @orders_bp.route("/admin/orders/<int:order_id>", methods=["PATCH"])
    @jwt_required()
    def update_order(order_id):
        if require_admin() is None:
            return {"message": "Admin access required."}, 403

        order = db.session.get(Order, order_id)
        if not order:
            return {"message": "Order not found."}, 404

        data = request.get_json() or {}
        status = data.get("status")
        estimated_delivery = data.get("estimated_delivery")

        if status not in statuses:
            return {"message": "Please choose a valid order status."}, 400

        if estimated_delivery:
            try:
                from datetime import date
                order.estimated_delivery = date.fromisoformat(estimated_delivery)
            except ValueError:
                return {"message": "Estimated delivery must be a valid date."}, 400
        else:
            order.estimated_delivery = None

        order.status = status
        db.session.commit()
        return {
            "message": "Order status updated successfully.",
            "order_id": order.id,
            "status": order.status,
            "estimated_delivery": (
                order.estimated_delivery.isoformat()
                if order.estimated_delivery else None
            ),
        }, 200

    return orders_bp
