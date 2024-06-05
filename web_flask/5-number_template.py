#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Display "Hello HBNB!" on the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """Display "HBNB" on /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>')
def display_c_text(text):
    """Display 'C ' followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
def display_python_text(text):
    """Display 'Python ' followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def display_number(n):
    """Display 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def display_number_template(n):
    """Display an HTML page if n is an integer."""
    return render_template('number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
