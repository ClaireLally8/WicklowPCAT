from flask import Flask, render_template, session, request, redirect

app= Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about-me')
def about_me():
  return render_template('about_me.html')

@app.route('/about-the-arts')
def arts_about():
  return render_template('about_arts.html')

    