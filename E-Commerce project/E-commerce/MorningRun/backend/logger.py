import logging
import os

from logging.handlers import RotatingFileHandler


logger = logging.getLogger("morningrun")
logger.setLevel(logging.INFO)
logger.propagate = False


def configure_logging(app):
    os.makedirs("logs", exist_ok=True)

    file_handler = RotatingFileHandler(
        "logs/morningrun.log",
        maxBytes=10240,
        backupCount=10,
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
    )
    file_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)