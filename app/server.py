from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Base de datos en memoria (simulada)
movies = {
    1: {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
    2: {"title": "The Matrix", "director": "The Wachowskis", "year": 1999},
}

# Página principal (HTML)
@app.route("/")
def home():
    return render_template("index.html", movies=movies)

# API: Crear una nueva película
@app.route("/api/movies", methods=["POST"])
def create_movie():
    data = request.get_json()
    new_id = max(movies.keys(), default=0) + 1
    movies[new_id] = data
    return jsonify({"message": "Movie added", "movie": movies[new_id]}), 201

# API: Leer todas las películas
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)

# API: Actualizar una película
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"message": "Movie not found"}), 404
    data = request.get_json()
    movies[movie_id].update(data)
    return jsonify({"message": "Movie updated", "movie": movies[movie_id]})

# API: Eliminar una película
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"message": "Movie not found"}), 404
    deleted_movie = movies.pop(movie_id)
    return jsonify({"message": "Movie deleted", "movie": deleted_movie})

if __name__ == "__main__":
    app.run(debug=True)
