from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# Whenver we go to the home page, we want to run the home function
@views.route('/')
@login_required
def home():
    return render_template("home.html")
    # return "<h1>Home</h1>"

