from flask import Flask, jsonify, render_template
import requests
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Set up logging configuration
set_logging(log_file='gateway.log')

app = Flask(__name__)

USER_SERVICE_URL = "http://localhost:5001"
PRODUCT_SERVICE_URL = "http://localhost:5002"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/all')
def get_all():
    try:
        users_resp = requests.get(f"{USER_SERVICE_URL}/api/users")
        products_resp = requests.get(f"{PRODUCT_SERVICE_URL}/api/products")

        users = users_resp.json()
        products = products_resp.json()

        return render_template("all.html", users=users, products=products)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error comunicando con microservicios", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
