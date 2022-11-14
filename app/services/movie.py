
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def get_all(self):
        return self.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        movie_id = data.get("id")
        movie = self.get_one(movie_id)

        movie.name = data.get("name")

        self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)
