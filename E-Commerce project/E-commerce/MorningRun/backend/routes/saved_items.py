from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import SavedItem, Product, db
 
def create_saved_items_blueprint():
    saved_items_bp = Blueprint("saved_items", __name__)
 
    @saved_items_bp.route("/saved-items/<int:product_id>", methods=["POST"])
    @jwt_required()
    def save_item(product_id):
        user_id = int(get_jwt_identity())
 
        product = db.session.get(Product, product_id)
 
        if not product:
            return {"message": "Product not found."}, 404
 
        existing_item = SavedItem.query.filter_by(
            user_id=user_id,
            product_id=product_id
        ).first()
 
        if existing_item:
            return {
                "message": "Product is already in your saved items."
            }, 409
 
        saved_item = SavedItem(
            user_id=user_id,
            product_id=product_id
        )
 
        db.session.add(saved_item)
        db.session.commit()
 
        return {
            "message": "Product saved successfully!"
        }, 201
 
    @saved_items_bp.route("/saved-items", methods=["GET"])
    @jwt_required()
    def get_saved_items():
        user_id = int(get_jwt_identity())
 
        items = SavedItem.query.filter_by(
            user_id=user_id
        ).all()
 
        saved_items = []
 
        for item in items:
            product = item.product
 
            saved_items.append({
                "id": item.id,
                "product_id": product.id,
                "name": product.name,
                "description": product.description,
                "price": float(product.price),
                "category": product.category,
                "brand": product.brand,
                "image": (
                    f"/products/{product.id}/image"
                    if product.image
                    else None
                ),
                "stock": product.stock
            })
 
        return {
            "items": saved_items
        }, 200
 
    @saved_items_bp.route("/saved-items/<int:product_id>", methods=["DELETE"])
    @jwt_required()
    def remove_saved_item(product_id):
        user_id = int(get_jwt_identity())
 
        saved_item = SavedItem.query.filter_by(
            user_id=user_id,
            product_id=product_id
        ).first()
 
        if not saved_item:
            return {
                "message": "Product is not in your saved items."
            }, 404
 
        db.session.delete(saved_item)
        db.session.commit()
 
        return {
            "message": "Product removed from saved items successfully!"
        }, 200
 
    return saved_items_bp