from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import CartItem, Product, User, db


def create_cart_blueprint():
    cart_bp = Blueprint("cart", __name__)

    def require_customer(user_id):
        user = db.session.get(User, user_id)
        if not user or user.role != "customer":
            return None
        return user

    @cart_bp.route("/cart", methods=["POST"])
    @jwt_required()
    def add_to_cart():
        user_id = int(get_jwt_identity())
        if require_customer(user_id) is None:
            return {"message": "Customer access required."}, 403

        data = request.get_json() or {}
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)
 
        if not product_id:
            return {"message": "Product ID is required."}, 400
 
        if not isinstance(quantity, int) or quantity < 1:
            return {"message": "Quantity must be a positive whole number."}, 400
 
        product = db.session.get(Product, product_id)
 
        if not product:
            return {"message": "Product not found."}, 404
 
        item = CartItem.query.filter_by(
            user_id=user_id,
            product_id=product.id
        ).first()
 
        new_quantity = quantity + (item.quantity if item else 0)
 
        if new_quantity > product.stock:
            return {"message": "Not enough stock available."}, 400
 
        if item:
            item.quantity = new_quantity
        else:
            db.session.add(
                CartItem(
                    user_id=user_id,
                    product_id=product.id,
                    quantity=quantity
                )
            )
 
        db.session.commit()
 
        return {
            "message": "Product added to cart successfully!"
        }, 200
 
    @cart_bp.route("/cart", methods=["GET"])
    @jwt_required()
    def get_cart():
        user_id = int(get_jwt_identity())
        if require_customer(user_id) is None:
            return {"message": "Customer access required."}, 403

        items = CartItem.query.filter_by(
            user_id=user_id
        ).all()
 
        cart_items = []
        cart_total = 0
 
        for item in items:
            product = item.product
 
            subtotal = float(product.price) * item.quantity
 
            cart_items.append({
                "product_id": str(product.id),
                "name": product.name,
                "price": float(product.price),
                "quantity": item.quantity,
                "subtotal": subtotal,
                "image": (
                    f"/products/{product.id}/image"
                    if product.image
                    else None
                ),
                "stock": product.stock,
            })
 
            cart_total += subtotal
 
        return {
            "items": cart_items,
            "total": cart_total
        }, 200
 
    @cart_bp.route("/cart/<int:product_id>", methods=["DELETE"])
    @jwt_required()
    def remove_from_cart(product_id):
        user_id = int(get_jwt_identity())
        if require_customer(user_id) is None:
            return {"message": "Customer access required."}, 403

        item = CartItem.query.filter_by(
            user_id=user_id,
            product_id=product_id
        ).first()
 
        if not item:
            return {"message": "Product is not in your cart."}, 404
 
        db.session.delete(item)
        db.session.commit()
 
        return {
            "message": "Product removed from cart successfully!"
        }, 200
 
    @cart_bp.route("/cart/<int:product_id>", methods=["PUT"])
    @jwt_required()
    def update_cart_quantity(product_id):
        user_id = int(get_jwt_identity())
        if require_customer(user_id) is None:
            return {"message": "Customer access required."}, 403

        data = request.get_json() or {}
        quantity = data.get("quantity")
 
        if not isinstance(quantity, int) or quantity < 1:
            return {
                "message": "Quantity must be a positive whole number."
            }, 400
 
        product = db.session.get(Product, product_id)
 
        if not product:
            return {"message": "Product not found."}, 404
 
        if quantity > product.stock:
            return {"message": "Not enough stock available."}, 400
 
        item = CartItem.query.filter_by(
            user_id=int(get_jwt_identity()),
            product_id=product_id
        ).first()
 
        if not item:
            return {
                "message": "Product is not in your cart."
            }, 404
 
        item.quantity = quantity
        db.session.commit()
 
        return {
            "message": "Cart quantity updated successfully!"
        }, 200
 
    return cart_bp