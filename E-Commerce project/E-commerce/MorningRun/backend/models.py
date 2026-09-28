from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(30),
        nullable=False,
        default="customer"
    )

    security_question = db.Column(
        db.String(255),
        nullable=False,
        default=""
    )

    security_answer = db.Column(
        db.String(255),
        nullable=False,
        default=""
    )

    phone = db.Column(db.String(30), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    suburb = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    province = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.String(20), nullable=True)


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(160),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    price = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    category = db.Column(
        db.String(120)
    )

    brand = db.Column(
        db.String(120)
    )

    # Store product image as binary data
    image = db.Column(
        db.LargeBinary
    )

    # Example: image/jpeg, image/png, image/webp
    image_type = db.Column(
        db.String(50)
    )

    stock = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )


class CartItem(db.Model):

    __tablename__ = "cart_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "cart_items",
            cascade="all, delete-orphan"
        )
    )

    product = db.relationship(
        "Product"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "product_id"
        ),
    )


class SavedItem(db.Model):

    __tablename__ = "saved_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "saved_items",
            cascade="all, delete-orphan"
        )
    )

    product = db.relationship(
        "Product"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "product_id"
        ),
    )


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    total_amount = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Processing"
    )

    estimated_delivery = db.Column(
        db.Date,
        nullable=True
    )

    payment_status = db.Column(
        db.String(30),
        nullable=False,
        default="pending"
    )

    payment_reference = db.Column(
        db.String(255),
        nullable=True
    )

    shipping_first_name = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_last_name = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_phone = db.Column(
        db.String(30),
        nullable=False
    )

    shipping_address = db.Column(
        db.String(255),
        nullable=False
    )

    shipping_suburb = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_city = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_province = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_postal_code = db.Column(
        db.String(20),
        nullable=False
    )

    payment_account_holder = db.Column(
        db.String(150),
        nullable=False
    )

    payment_account_number = db.Column(
        db.String(50),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "orders",
            cascade="all, delete-orphan"
        )
    )

    items = db.relationship(
        "OrderItem",
        backref="order",
        cascade="all, delete-orphan"
    )


class OrderItem(db.Model):

    __tablename__ = "order_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "orders.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "products.id",
            ondelete="SET NULL"
        ),
        nullable=True
    )

    product_name = db.Column(
        db.String(160),
        nullable=False
    )

    price = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    subtotal = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    product = db.relationship(
        "Product"
    )


class PasswordResetToken(db.Model):

    __tablename__ = "password_reset_tokens"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    token = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        index=True
    )

    expires_at = db.Column(
        db.DateTime,
        nullable=False
    )

    used = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "password_reset_tokens",
            cascade="all, delete-orphan"
        )
    )