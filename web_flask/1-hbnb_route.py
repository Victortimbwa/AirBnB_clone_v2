#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display 'HBNB'."""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)