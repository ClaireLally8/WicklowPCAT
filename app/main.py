from flask import Flask, render_template, redirect

from .helpers import faq, resources

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

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/theraputic-space')
def the_space():
  return render_template('the_space.html')

@app.route('/resources-and-faq')
def FAQ():
  return render_template('FAQ.html', faq = faq, resources = resources)

@app.route('/contact')
def contact():
  return render_template('contact.html')

    