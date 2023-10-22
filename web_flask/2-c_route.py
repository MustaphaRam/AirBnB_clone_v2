#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'BNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)