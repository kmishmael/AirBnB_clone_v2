#!/usr/bin/python3
"""
Flask app
0.0.0.0:5000
route /
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays hello"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
