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

@app.route('/english_words_1_3')
def english_words_1_3():
    return render_template('english_words_1_3.html')

@app.route('/Fundemantals_Ch_1_2')
def Fundemantals_Ch_1_2():
    return render_template('Fundemantals_Ch_1_2.html')

@app.route('/Module4_db')
def Module4_db():
    return render_template('Module4_db.html')

if __name__ == '__main__':    app.run(debug=True)
