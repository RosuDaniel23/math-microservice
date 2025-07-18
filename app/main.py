import os
import logging

from flask import Flask
from dotenv import load_dotenv
from app.views import math_bp
from app.database import init_db

# încarca .env
load_dotenv()

# configurare logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config["ENV"] = os.getenv("FLASK_ENV", "production")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.register_blueprint(math_bp)
    init_db()

    logger.info("Application started in %s mode", app.config["ENV"])
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
