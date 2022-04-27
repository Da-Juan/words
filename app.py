import os

from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

from words import solve

from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Length, NumberRange

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)


class WordsForm(FlaskForm):
    letters = StringField("Letters", [InputRequired(), Length(min=2)])
    length = IntegerField("Length", [InputRequired(), NumberRange(min=1)])


@app.route("/", methods=["GET", "POST"])
def hello_world():
    form = WordsForm(request.form)
    words = []
    if request.method == "POST" and form.validate():
        words = solve(form.letters.data, form.length.data)
    return render_template("template.html", form=form, words=words)
