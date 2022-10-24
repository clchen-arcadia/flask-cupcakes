"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE_IMG_URL = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    flavor = db.Column(
        db.String(100),
        nullable=False
    )

    size = db.Column(
        db.String(50),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    image = db.Column(
        db.String(500),
        nullable=False,
        default=DEFAULT_CUPCAKE_IMG_URL
    )
