#!/usr/bin/env python3
from flask import Flask, request, jsonify
from auth import Auth
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Return a welcome message."""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

app = Flask(__name__)
AUTH = Auth()

@app.route('/users', methods=['POST'])
def register_user():
    """Endpoint for registering a new user."""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False