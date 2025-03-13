from flask import Flask
from routes import movie_bp

app = Flask(__name__)
app.register_blueprint(movie_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
