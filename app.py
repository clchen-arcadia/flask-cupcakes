"""Flask app for Cupcakes"""

from flask import (
    Flask,
    redirect,
    render_template
)

from flask_debugtoolbar import DebugToolbarExtension

from models import (
    db,
    connect_db,
    Cupcake
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "DON'T EVER DO THIS IN PRACTICE!!"

# If you don't want intercepted redirects uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
