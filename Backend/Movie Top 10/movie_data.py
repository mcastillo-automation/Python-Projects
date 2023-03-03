class MovieData:

    def __init__(self, title, year, description, img_url):
        self.title = title
        self.year = year.split("-")[0]
        self.description = description
        self.img_url = f"https://image.tmdb.org/t/p/original/{img_url}"
