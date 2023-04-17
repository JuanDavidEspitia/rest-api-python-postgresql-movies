from flask import Flask, jsonify
from config import config

app = Flask(__name__)


# Mensaje de Bienvenida
@app.route("/", methods=["GET"])
def index():
    return jsonify({"Mensaje": "Bienvenido al curso de API Rest Python con PostgreSQL"})


def page_not_found(error):
    return "<h1>" "*** Not found page in ***" "</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
