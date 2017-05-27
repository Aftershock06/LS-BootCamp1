from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def  index ():
    return render_template('home.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')

@app.route('/post/<postnum>')
def posts(postnum):
    return 'this is post ' + postnum

@app.route('/birthday')
def birthday():
    return 'August 20th, 1987'

@app.route('/greeting/<name>')
def name(name):
    return "Hello " + name
