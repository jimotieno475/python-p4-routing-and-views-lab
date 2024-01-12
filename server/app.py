#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    parameter=parameter-1
    numbers=range(0,parameter+1)
    result='\n'.join(map(str,numbers))
    return f'{result}\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1,operation,num2):
    result=None
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
    else:
        return 'invalid operation'
    if result is None:
        return 'invalid operation'
    else: 
        return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
