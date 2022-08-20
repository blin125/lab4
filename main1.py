"""
The code is written for COMPSCI235 Lab 4 Flask and Jinja. 
Author: Bruno Lino
Date: 19/08/2022
"""
from math import factorial
from flask import Flask, render_template
from markupsafe import escape
from template.factorial import compute_factorial 
from template.grades import grade

app = Flask(__name__,template_folder='template')

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/user/<username>')
def uer_name(username):
    return render_template('user_name_code.html', input = username.capitalize())


@app.route('/fac/<int:inp_fac>')
def show_factorial(inp_fac):
    '''Pass a variable to the template.'''
    # We implemented this function in Lab1.
    factorial = compute_factorial(inp_fac)
    return render_template('factorial.html',
        input=inp_fac, 
        factorial=factorial)

@app.route('/results/<int:number>')
def show_result(number):
    result = grade(number)
    return render_template('grades.html', input = result)



if __name__ == '__main__':
    app.run(debug=True, port=8000)