#!/usr/bin/env python3
""" Module of Session Auth views
"""
from flask import jsonify, abort, request, session, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv
import json


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sessionLogin() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the status of the API
    """
    email = request.form.get('email')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for item in users:
        if item.is_valid_password(password):
            from api.v1.app import auth
            resp = jsonify(item.to_json())
            SESSION_NAME = getenv('SESSION_NAME')
            resp.set_cookie(SESSION_NAME, auth.create_session(item.id))
            return resp
        else:
            return jsonify({"error": "wrong password"}), 404
