from flask import render_template, redirect, url_for
from Portfolio import app

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.errorhandler(404)
def error_404(error):
    return render_template("error_page_404.html"), 404

@app.errorhandler(500)
def error_500(error):
    return render_template("error_page_500.html"), 500