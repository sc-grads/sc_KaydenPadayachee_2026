import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from sqlalchemy import inspect, text
from logger import configure_logging
from models import db
from routes.auth import create_auth_blueprint
from routes.cart import create_cart_blueprint
from routes.products import create_products_blueprint
from routes.saved_items import create_saved_items_blueprint
from routes.orders import create_orders_blueprint
from routes.payfast import create_payfast_blueprint
from routes.contact import contact_bp



load_dotenv()


app = Flask(__name__)
configure_logging(app)
 
app.logger.info("APPLICATION_STARTED | MorningRun backend started")
 


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///morningrun.db",
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY",
    "change-this-secret"
)


CORS(app)


db.init_app(app)

JWTManager(app)


with app.app_context():
    db.create_all()
    inspector = inspect(db.engine)
    if "estimated_delivery" not in {
        column["name"] for column in inspector.get_columns("orders")
    }:
        with db.engine.begin() as connection:
            connection.execute(
                text("ALTER TABLE orders ADD COLUMN estimated_delivery DATE")
            )
    user_columns = {column["name"] for column in inspector.get_columns("users")}
    missing_user_columns = {
        "phone": "VARCHAR(30)",
        "address": "VARCHAR(255)",
        "suburb": "VARCHAR(100)",
        "city": "VARCHAR(100)",
        "province": "VARCHAR(100)",
        "postal_code": "VARCHAR(20)",
    }
    with db.engine.begin() as connection:
        for column_name, column_type in missing_user_columns.items():
            if column_name not in user_columns:
                connection.execute(
                    text(
                        f"ALTER TABLE users ADD COLUMN {column_name} {column_type}"
                    )
                )
    with db.engine.begin() as connection:
        connection.execute(
            text(
                "UPDATE orders SET status = 'Processing' "
                "WHERE status IN ('pending', 'processing')"
            )
        )


app.register_blueprint(create_auth_blueprint())

app.register_blueprint(create_products_blueprint())

app.register_blueprint(create_cart_blueprint())

app.register_blueprint(create_saved_items_blueprint())

app.register_blueprint(create_orders_blueprint())

app.register_blueprint(create_payfast_blueprint())

app.register_blueprint(contact_bp)

@app.route("/")
def home():
    return "MorningRun backend is running!"


if __name__ == "__main__":
    app.run(debug=True)