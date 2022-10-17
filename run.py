from flask import Flask
from flask import render_template, request, redirect, url_for
from form import SignupForm, UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
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
   form = UserForm()
   if slug:
      form.title.data = slug
   return render_template("admin/user_form.html", slug=slug, form=form)


@app.route('/sign-up/', methods=["GET", "POST"])
def show_sign_up():
   form = SignupForm()
   if form.validate_on_submit():
      name = form.name.data
      email = form.email.data
      password = form.password.data
      next = request.args.get('next', None)
      if next:
         return redirect(next)
      return redirect(url_for('index'))
   return render_template("signup_form.html", form=form)