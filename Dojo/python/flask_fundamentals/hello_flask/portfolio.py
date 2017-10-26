from flask import Flask, render_template #Import Flask to allow us to create app
app = Flask(__name__) # Global variable __name__ tells Flask whether we are running file

@app.route('/') #decorator and root route
def portfolio(): #function for root route
    return render_template('portfolio.html') # html page to show when root is accessed

@app.route('/projects') #decorator and root route
def project(): #function for root route
    return render_template('projects.html') # html page to show when root is accessed

@app.route('/aboutme') #decorator and root route
def about(): #function for root route
    return render_template('aboutme.html') # html page to show when root is accessed


app.run(debug=True) # Runs app in debug mode
