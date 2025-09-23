from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Set up logging configuration
set_logging(log_file='users_service.log')

app = Flask(__name__)

USERS_FILE = "./exercises/microservices/users_services/users.json"
USERS_HTML = "users.html"

with open(USERS_FILE, "r") as f:
    users = json.load(f)

@app.route('/users', methods=['GET'])
def get_users():
    return render_template(USERS_HTML, users=users)

@app.route('/users/create', methods=['GET'])
def create_user_form():
    return render_template("create_user.html")

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get("name")
    if not name:
        return "El nombre del usuario es requerido", 400

    user = {
        'id': len(users) + 1,
        'name': name
    }
    users.append(user)

    # Guardar en archivo
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return redirect(url_for('get_users'))

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(port=5001)
