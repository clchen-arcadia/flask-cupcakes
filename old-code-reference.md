
<h2>Add a New Cupcake</h2>

  <form method="POST" id="cupcakes-form">

    {{ form.hidden_tag() }}

    {% for field in form
      if field.widget.input_type != 'hidden' %}

      <p>
        {{ field.label }}
        {{ field }}

        {% for error in field.errors %}
          {{ error }}
        {% endfor %}

      </p>

      {% endfor %}

    <button id="add-cupcake-button" type="submit">Add Cupcake</button>

  </form>



  ------------------------



  I like to use the flask.Response class:

from flask import Response


@app.route("/")
def index():
    return Response(
        "The response body goes here",
        status=400,
    )
