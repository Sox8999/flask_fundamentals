from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninja():
    return render_template("ninja.html")

@app.route('/blue')
def blue():
    return render_template("blue.html")

@app.route('/orange')
def orange():
    return render_template("orange.html")

@app.route('/other')
def other():
    return render_template("other.html")

@app.route('/purple')
def purple():
    return render_template("purple.html")

@app.route('/red')
def red():
    return render_template("red.html")

app.run(debug=True)
