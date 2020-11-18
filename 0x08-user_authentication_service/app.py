#!/usr/bin/env python3
"""Module: Basic Flask App"""
from flask import Flask, jsonify, request, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Function: set up a basic Flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Function: End Point /users to register a user"""

    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        dt = {"email": "{}".format(new_user.email), "message": "user created"}
        return jsonify(dt)
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def sessions():
    """Function: LOGIN a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    dt = {"email": email, "message": "logged in"}
    resp = jsonify(dt)
    session_id = AUTH.create_session(email)
    resp.set_cookie('session_id', session_id)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
