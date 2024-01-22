#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str_param>')
def print_string(str_param):
    print(str_param)
    return f'The string is: {str_param}'

@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(map(str, range(num)))
    return f'Numbers:\n{numbers}'
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    print(f"Route hit: /math/{num1}/{operation}/{num2}")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return f'Result of {num1} {operation} {num2} is: {result}'




if __name__ == '__main__':
    app.run(port=5555, debug=True)
