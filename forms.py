
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddCupcakeForm(FlaskForm):
    """Add a cupcake to the database and front page list."""

    flavor = StringField(
        "Cupcake Flavor",
        validators=[InputRequired()]
    )

    size = StringField(
        "Cupcake Size",
        validators=[InputRequired()]
    )

    rating = IntegerField(
        "Cupcake Rating",
        validators=[InputRequired()]
    )

    image = StringField(
        "Cupcake Image",
        validators=[Optional(), URL()]
    )
