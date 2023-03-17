from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()], render_kw={"autocomplete": "off"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    name = StringField("Name", validators=[InputRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()], render_kw={"autocomplete": "off"})
    password = PasswordField("Password", validators=[InputRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField("Login")


class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[InputRequired(), Length(min=1)], render_kw={"autocomplete": "off"})
    submit = SubmitField("Submit Comment")
