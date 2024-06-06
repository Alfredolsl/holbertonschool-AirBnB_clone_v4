#!/usr/bin/python3
"""Script that starts a Flask app"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}}

@app.teardown_appcontext
def teardown(exception):
    """Closes session"""
    storage.close()


@app.errorhandler(404)
def errorhandler(error):
    """Returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = getenv("HBNB_API_PORT", 5000)
    app.run(host=API_HOST, port=API_PORT, threaded=True)
