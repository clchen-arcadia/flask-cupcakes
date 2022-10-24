"""Flask app for Cupcakes"""

from flask import (
    Flask,
    redirect,
    request,
    render_template,
    jsonify
)

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


@app.get("/api/cupcakes")
def get_cupcakes_data():
    """Get data about all cupcakes.
    Return JSON {cupcakes: [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def get_single_cupcake_data(cupcake_id):
    """Get data about a single cupcake.
    Return JSON {cupcakes: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post("/api/cupcakes")
def create_cupcake():
    """Create cupcake from form data and return it.
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Update cupcake which already exists in database.
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json.get("flavor")
    size = request.json.get("size")
    rating = request.json.get("rating")
    image = request.json.get("image")

    if flavor is not None:
        cupcake.flavor = flavor

    if size is not None:
        cupcake.size = size

    if rating is not None:
        cupcake.rating = rating

    if image is not None:
        cupcake.image = image

    db.session.add(cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)
