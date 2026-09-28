from flask import Blueprint, request, Response

from flask_jwt_extended import get_jwt_identity, jwt_required

from models import Product, User, db
from logger import logger


def product_response(product):
    return {
        "id": str(product.id),
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
        "stock": product.stock,
    }


def create_products_blueprint():

    products_bp = Blueprint("products", __name__)

    # ---------------------------------------------------------
    # ADD PRODUCT
    # ---------------------------------------------------------

    @products_bp.route("/products", methods=["POST"])
    @jwt_required()
    def add_product():

        user = db.session.get(
            User,
            int(get_jwt_identity())
        )

        if not user:
            return {
                "message": "User not found."
            }, 404

        if user.role != "admin":
            return {
                "message": "Admin access required."
            }, 403

        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        category = request.form.get("category")
        brand = request.form.get("brand")
        stock = request.form.get("stock")
        image = request.files.get("image")

        if not name or price is None or stock is None:
            return {
                "message": "Name, price and stock are required."
            }, 400

        image_data = None
        image_type = None

        if image:
            image_data = image.read()
            image_type = image.mimetype

        product = Product(
            name=name,
            description=description,
            price=price,
            category=category,
            brand=brand,
            image=image_data,
            image_type=image_type,
            stock=stock,
        )

        db.session.add(product)
        db.session.commit()
        logger.info("Product added: %s", product.name)

        return {
            "message": "Product added successfully!",
            "product_id": str(product.id),
            "product": product_response(product)
        }, 201

    # ---------------------------------------------------------
    # GET ALL PRODUCTS
    # ---------------------------------------------------------

    @products_bp.route("/products", methods=["GET"])
    def get_products():

        return [
            product_response(product)
            for product in Product.query.all()
        ], 200

    # ---------------------------------------------------------
    # GET SINGLE PRODUCT
    # ---------------------------------------------------------

    @products_bp.route(
        "/products/<int:product_id>",
        methods=["GET"]
    )
    def get_product(product_id):

        product = db.session.get(
            Product,
            product_id
        )

        if not product:
            return {
                "message": "Product not found."
            }, 404

        return product_response(product), 200

    # ---------------------------------------------------------
    # GET PRODUCT IMAGE
    # ---------------------------------------------------------

    @products_bp.route(
        "/products/<int:product_id>/image",
        methods=["GET"]
    )
    def get_product_image(product_id):

        product = db.session.get(
            Product,
            product_id
        )

        if not product or not product.image:
            return {
                "message": "Image not found."
            }, 404

        return Response(
            product.image,
            mimetype=product.image_type or "image/jpeg"
        )

    # ---------------------------------------------------------
    # UPDATE PRODUCT
    # ---------------------------------------------------------

    @products_bp.route(
        "/products/<int:product_id>",
        methods=["PUT"]
    )
    @jwt_required()
    def update_product(product_id):

        user = db.session.get(
            User,
            int(get_jwt_identity())
        )

        if not user:
            return {
                "message": "User not found."
            }, 404

        if user.role != "admin":
            return {
                "message": "Admin access required."
            }, 403

        product = db.session.get(
            Product,
            product_id
        )

        if not product:
            return {
                "message": "Product not found."
            }, 404

        data = request.get_json() or {}

        if "name" in data:
            product.name = data["name"]

        if "description" in data:
            product.description = data["description"]

        if "price" in data:
            product.price = data["price"]

        if "category" in data:
            product.category = data["category"]

        if "brand" in data:
            product.brand = data["brand"]

        if "stock" in data:
            product.stock = data["stock"]

        db.session.commit()

        return {
            "message": "Product updated successfully!",
            "product": product_response(product)
        }, 200

    # ---------------------------------------------------------
    # UPDATE PRODUCT IMAGE
    # ---------------------------------------------------------

    @products_bp.route(
        "/products/<int:product_id>/image",
        methods=["PUT"]
    )
    @jwt_required()
    def update_product_image(product_id):

        user = db.session.get(
            User,
            int(get_jwt_identity())
        )

        if not user:
            return {
                "message": "User not found."
            }, 404

        if user.role != "admin":
            return {
                "message": "Admin access required."
            }, 403

        product = db.session.get(
            Product,
            product_id
        )

        if not product:
            return {
                "message": "Product not found."
            }, 404

        image = request.files.get("image")

        if not image:
            return {
                "message": "Image is required."
            }, 400

        product.image = image.read()
        product.image_type = image.mimetype

        db.session.commit()

        return {
            "message": "Product image updated successfully!",
            "image": f"/products/{product.id}/image"
        }, 200

    # ---------------------------------------------------------
    # DELETE PRODUCT
    # ---------------------------------------------------------

    @products_bp.route(
        "/products/<int:product_id>",
        methods=["DELETE"]
    )
    @jwt_required()
    def delete_product(product_id):

        user = db.session.get(
            User,
            int(get_jwt_identity())
        )

        if not user:
            return {
                "message": "User not found."
            }, 404

        if user.role != "admin":
            return {
                "message": "Admin access required."
            }, 403

        product = db.session.get(
            Product,
            product_id
        )

        if not product:
            return {
                "message": "Product not found."
            }, 404

        db.session.delete(product)
        db.session.commit()

        return {
            "message": "Product deleted successfully!"
        }, 200

    return products_bp