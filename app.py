import os

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError, CSRFProtect

from words import solve

from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Length, NumberRange

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)


class WordsForm(FlaskForm):
    """HTML form definition."""

    letters = StringField(
        label="Letters list",
        validators=[InputRequired(), Length(min=2)],
        render_kw={"placeholder": "abcd"},
    )
    length = IntegerField(
        label="Word length",
        validators=[InputRequired(), NumberRange(min=1)],
        render_kw={"placeholder": "0"},
    )


@app.errorhandler(CSRFError)
def handle_csrf_error(_):
    """Redirect to index on CSRF Error."""
    return redirect(url_for("index"))


@app.route("/favicon.svg")
def favicon():
    """Send favicon."""
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.svg", mimetype="image/svg+xml"
    )


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page."""
    form = WordsForm(request.form)
    words = []
    if request.method == "POST" and form.validate():
        words = solve(form.letters.data, form.length.data)
    return render_template("template.html", form=form, words=words)
