from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Set up logging configuration
set_logging(log_file='products_service.log')

app = Flask(__name__)

PRODUCTS_FILE = "./exercises/microservices/products_services/products.json"
PRODUCTS_HTML = "products.html"

with open(PRODUCTS_FILE, "r") as f:
    products = json.load(f)

@app.route('/products', methods=['GET'])
def get_products():
    return render_template(PRODUCTS_HTML, products=products)

@app.route('/products/create', methods=['GET'])
def create_product_form():
    return render_template("create_product.html")

@app.route('/products', methods=['POST'])
def create_product():
    name = request.form.get("name")
    if not name:
        return "El nombre del producto es requerido", 400

    product = {
        'id': len(products) + 1,
        'name': name
    }
    products.append(product)

    # Guardar en archivo
    with open(PRODUCTS_FILE, "w") as f:
        json.dump(products, f, indent=4)

    return redirect(url_for('get_products'))

@app.route('/api/products', methods=['GET'])
def api_get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5002)
