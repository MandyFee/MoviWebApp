from models import db, User, Movie

class DataManager:
    def get_users(self):
        return User.query.all()

    def create_user(self, name):
        user = User(name=name)
        db.session.add(user)
        db.session.commit()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, **kwargs):
        movie = Movie(**kwargs)
        db.session.add(movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
