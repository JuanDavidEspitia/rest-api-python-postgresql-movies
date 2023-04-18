from flask import Blueprint, jsonify, request
import uuid

# Entities
from src.models.entities.Movie import Movie

# Models
from src.models.MovieModel import MovieModel

main = Blueprint("movie_blueprint", __name__)


@main.route("/")
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie is not None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_movie():
    try:
        # print(request.json)
        # Como buena practica se deben colocar validaciones de los valores
        # Formatos, cantidad de caracteres, tipos de datos, espacios en blanco, etc
        title = request.json["title"]
        duration = int(request.json["duration"])
        released = request.json["released"]
        id = uuid.uuid4()
        movie = Movie(str(id), title, duration, released)

        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({"message": "Error on insert"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
