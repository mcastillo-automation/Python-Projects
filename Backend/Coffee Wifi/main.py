from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
import config

app = Flask(__name__)
app.config["SECRET_KEY"] = config.key
Bootstrap5(app)

coffee_rating = ["☕️", "☕️"*2, "☕️"*3, "☕️"*4, "☕️"*5]
wifi_rating = ["💪", "💪"*2, "💪"*3, "💪"*4, "💪"*5]
power_rating = ["🔌", "🔌"*2, "🔌"*3, "🔌"*4, "🔌"*5]


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = StringField("Location", validators=[DataRequired(), URL()])
    open_time = StringField("Open Time", validators=[DataRequired()])
    close_time = StringField("Close Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=coffee_rating, validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating", choices=wifi_rating, validators=[DataRequired()])
    power_outlet = SelectField("Power Socket Available", choices=power_rating, validators=[DataRequired()])
    submit = SubmitField("Submit")

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        data = [form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data, form.coffee_rating.data, form. wifi_rating.data, form.power_outlet.data]
        with open(file="cafe-data.csv", newline="", mode="a+") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
    return render_template("add.html", cafe_form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
