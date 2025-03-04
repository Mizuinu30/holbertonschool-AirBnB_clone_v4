#!/usr/bin/python3
"""Script to start the API"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(app_views)


# Create a CORS instance with permissive settings (for demonstration purposes)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(exception):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(exception):
    """404 error"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """Main"""
    app.run(host='0.0.0.0', port=5001)
