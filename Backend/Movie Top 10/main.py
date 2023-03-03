from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import EditForm, AddForm
from movie_lookup import MovieDB
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.token
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-ten-movies.db"
db.init_app(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(400), nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(400), nullable=True)
    img_url = db.Column(db.String(2083), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().all()
    for (idx, movie) in enumerate(movies):
        movie.ranking = len(movies) - idx
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm(hidden_id=request.args.get('id'))
    if request.method == "POST":
        movie_id = request.form.get('hidden_id')
        movie_to_edit = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
        movie_to_edit.rating = request.form.get('rating')
        movie_to_edit.review = request.form.get('review')
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
    return render_template("edit.html", edit=form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if request.method == 'POST':
        search_results = MovieDB().search_movie(request.form.get('movie_title'))
        movie_title = search_results.title
        movie_year = search_results.year
        movie_description = search_results.description
        movie_img_url = search_results.img_url
        movie_to_add = Movies(
            title=movie_title,
            year=movie_year,
            description=movie_description,
            img_url=movie_img_url
        )
        db.session.add(movie_to_add)
        db.session.commit()
        movie_added = db.session.execute(db.select(Movies).filter_by(title=movie_title)).scalar_one()
        movie_id = movie_added.id
        return redirect(url_for('edit', id=movie_id))
    return render_template("add.html", add=add_form)


if __name__ == "__main__":
    app.run(debug=True)
