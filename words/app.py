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

from wtforms import HiddenField, IntegerField, StringField
from wtforms.validators import AnyOf, InputRequired, Length, NumberRange

from .constants import DEFAULT_LANGUAGE, LANGUAGES
from .words import solve

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Strict"
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
    language = HiddenField(
        label="Language",
        validators=[InputRequired(), AnyOf(LANGUAGES)],
        default=DEFAULT_LANGUAGE,
    )


@app.errorhandler(CSRFError)
def handle_csrf_error(_):
    """Redirect to index on CSRF Error."""
    return redirect(url_for("index"))


@app.route("/favicon.svg")
def favicon():
    """Send favicon."""
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.svg", mimetype="image/svg+xml")


@app.route("/icons/<icon>")
def icons(icon):
    """Send icon."""
    return send_from_directory(os.path.join(app.root_path, "static"), icon, mimetype="image/png")


@app.route("/styles/<style>")
def styles(style):
    """Send CSS."""
    return send_from_directory(os.path.join(app.root_path, "static"), style, mimetype="text/css")


@app.route("/scripts/<script>")
def scripts(script):
    """Send script."""
    return send_from_directory(os.path.join(app.root_path, "static"), script, mimetype="text/javascript")


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page."""
    form = WordsForm(request.form)
    words = []
    if request.method == "POST" and form.validate():
        words = solve(form.letters.data, form.length.data, form.language.data)
    return render_template("template.html", form=form, words=words)


@app.after_request
def set_secure_headers(response):
    """Set all relevant security cookies."""
    response.headers["Content-Security-Policy"] = (
        "base-uri 'none';"
        "default-src 'none';"
        "frame-ancestors 'none';"
        "form-action 'self';"
        "img-src 'self';"
        "script-src 'self';"
        "style-src 'self';"
    )
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
