from flask import Flask
from flask import render_template
app = Flask(__name__)
users = []
@app.route('/')
def index():
     return render_template("index.html", num_posts=len(users))
@app.route('/u/<string:slug>/')
def show_user(slug):
   return render_template("user_view.html", slug_title=slug)
@app.route('/admin/user/')
@app.route('/admin/user/<string:slug>/')
def user_form(slug=None):
    return render_template("admin/user_form.html", slug=slug)