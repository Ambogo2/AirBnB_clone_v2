#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello():
    """defines the function hello"""
    return 'Hello HBNB!'
@app.route('/hbnb',strict_slashes=False)
def HBNB():
    """defines the HBNB"""
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def c_text(text):
    # displays C followed by text
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<text>',strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>',strict_slashes=False)
def number_n(n):
    return f'{n} is a number'

@app.route('/number_template/<n>',strict_slashes=False)
def number_template(n):
    try:
        # Try to convert `n` to an integer
        number = int(n)
    except ValueError:
        # If conversion fails, return a 404 error
        abort(404)

    # Render the template with the integer `number`
    return render_template('5-number.html', number=number)

@app.route('/number_odd_or_even/<n>',strict_slashes=False)
def number_odd_or_even(n):
    try:
        # Try to convert `n` to an integer
        number = int(n)
    except ValueError:
        # If conversion fails, return a 404 error
        abort(404)

    # Determine if the number is even or odd
    if number % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    # Render the template with the number and its even/odd status
    return render_template('5-odd_or_even.html', number=number, even_or_odd=even_or_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)