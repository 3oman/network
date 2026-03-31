from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Module4')
def module4():
    return render_template('Module4.html')

@app.route('/Module3')
def module3():
    return render_template('Module3.html')

@app.route('/Module2')
def module2():
    return render_template('Module2.html')

if __name__ == '__main__':    app.run(debug=True)
