from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form


@app.route('/')
def index():
    session['count'] += 1
    return render_template("index.html")

@app.route('/two', methods=['POST'])
def two():
   session['count'] += 1
   return redirect("/")


@app.route('/reset', methods=['POST'])
def reset():
     session['count'] = 0
     return redirect("/")

app.run(debug=True) # run our server
