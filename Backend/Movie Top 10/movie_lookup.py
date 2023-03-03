import requests
from movie_data import MovieData
import config

MOVIE_DB_URL = "https://api.themoviedb.org/3"
API_KEY = config.movie_db_api


class MovieDB:

    def search_movie(self, movie_name):
        params = {
            'api_key': API_KEY,
            'query': movie_name
        }
        db_response = requests.get(url=f"{MOVIE_DB_URL}/search/movie", params=params)

        try:
            response_json = db_response.json()['results'][0]

        except IndexError:
            return None

        else:
            movie_data = MovieData(
                title=response_json['title'],
                description=response_json['overview'],
                year=response_json['release_date'],
                img_url=response_json['poster_path']
            )
            return movie_data
