from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, HiddenField
from wtforms.validators import InputRequired


class EditForm(FlaskForm):
    rating = DecimalField(label="Your Rating Out of 10 e.g 7.5", places=2, rounding=None, validators=[InputRequired()],
                          render_kw={"autocomplete": "off"})
    review = StringField(label="Your Review", validators=[InputRequired()], render_kw={"autocomplete": "off"})
    hidden_id = HiddenField()
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[InputRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField(label="Submit")
