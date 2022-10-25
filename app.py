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
    Cupcake,
    DEFAULT_CUPCAKE_IMG_URL
)

from forms import AddCupcakeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "DON'T EVER DO THIS IN PRACTICE!!"

# If you don't want intercepted redirects uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



################ROUTES FOR API########################

@app.get("/api/cupcakes")
def get_cupcakes_data():
    """
    Get data about all cupcakes.
    Return JSON {cupcakes: [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get("/api/cupcakes/<int:cupcake_id>")
def get_single_cupcake_data(cupcake_id):
    """
    Get data about a single cupcake.
    Return JSON {cupcakes: {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post("/api/cupcakes")
def create_cupcake():
    """
    Create cupcake from form data and return it.
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
    """
    Update cupcake which already exists in database.
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get(
        "image", cupcake.image) or DEFAULT_CUPCAKE_IMG_URL

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """
    Delete cupcake in the database
    Returns JSON like {"deleted": cupcake-id}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    Cupcake.query.filter_by(id=cupcake_id).delete()

    db.session.commit()

    return jsonify(deleted=cupcake_id)


#################ROUTES FOR FRONTEND####################

# @app.get('/')
# def display_front_page():
#     """Display list of data and form for submitting new data to API"""

#     form = AddCupcakeForm()

#     return render_template("index.html", form=form)


@app.route("/", methods=["GET", "POST"])
def add_cupcake():
    """Form for adding a cupcake to the database."""

    form = AddCupcakeForm()

    if form.validate_on_submit():
        print("--------------YOU GOT HERE 1------------------")
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data

        new_cupcake = Cupcake(
            flavor=flavor,
            size=size,
            rating=rating,
            image=image,
        )

        db.session.add(new_cupcake)
        db.session.commit()
        return redirect('/')

    else:
        print("--------------YOU GOT HERE 2------------------")
        return render_template(
            "index.html", form=form)
