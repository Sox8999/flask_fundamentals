from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def home_name():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   print request.form
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) # run our server
