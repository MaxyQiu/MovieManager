from flask import Blueprint, request, jsonify
from services.movie_service import add_movie, get_movies, update_movie, delete_movie

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/movies', methods=['POST'])
def create_movie():
    data = request.json
    add_movie(data)
    return jsonify({"message": "Movie added successfully"}), 201

@movie_bp.route('/movies', methods=['GET'])
def list_movies():
    movies = get_movies()
    return jsonify(movies)

@movie_bp.route('/movies/<movie_id>', methods=['PUT'])
def edit_movie(movie_id):
    data = request.json
    update_movie(movie_id, data)
    return jsonify({"message": "Movie updated successfully"})

@movie_bp.route('/movies/<movie_id>', methods=['DELETE'])
def remove_movie(movie_id):
    delete_movie(movie_id)
    return jsonify({"message": "Movie deleted successfully"})
