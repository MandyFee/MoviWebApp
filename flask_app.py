from flask import Flask, render_template, request, redirect, send_from_directory
from data_manager import DataManager
from models import db
import os

app = Flask(__name__)

# Datenbank konfigurieren
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviweb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

data_manager = DataManager()

# Route für favicon.ico hinzufügen
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Startseite: Nutzerliste
@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)

# Neuen Nutzer hinzufügen
@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    data_manager.create_user(name)
    return redirect('/')

# Lieblingsfilme eines Nutzers anzeigen
@app.route('/users/<int:user_id>/movies', methods=['GET'])
def show_movies(user_id):
    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id)

# Lieblingsfilm hinzufügen
@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    title = request.form['title']
    import requests
    api_key = "fa3f2c93" # <--- PRÜFE DAS HIER SEHR SORGFÄLTIG!
    response = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={api_key}").json()

    # FÜGE HIER EIN PRINT STATEMENT EIN, UM DIE ROHEN API-DATEN ZU SEHEN
    print(f"OMDB API Response for '{title}': {response}")

    # Stelle sicher, dass "Year" ein gültiger Integer ist, bevor du ihn konvertierst
    year = 0
    if response.get("Year") and response.get("Year").isdigit(): # Prüft, ob 'Year' existiert und nur Ziffern enthält
        year = int(response.get("Year"))
    elif response.get("Year") and isinstance(response.get("Year"), str) and len(response.get("Year")) > 4:
         # Manchmal kann 'Year' auch "1994–1998" sein. Dann nehmen wir den ersten Teil.
         try:
             year = int(response.get("Year").split('–')[0])
         except ValueError:
             year = 0


    movie = {
        "name": response.get("Title", title),
        "director": response.get("Director", "Unknown"),
        "year": year, # Verwende die sicher konvertierte Jahreszahl
        "poster_url": response.get("Poster", ""),
        "user_id": user_id
    }
    data_manager.add_movie(**movie)
    return redirect(f'/users/{user_id}/movies')

# Film aktualisieren
@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    new_title = request.form['title']
    data_manager.update_movie(movie_id, new_title=new_title)
    return redirect(f'/users/{user_id}/movies')

# Film löschen
@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(f'/users/{user_id}/movies')

# 404-Fehlerseite
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Generische Fehlerseite für 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    # Logge den Fehler für Debugging-Zwecke
    app.logger.error(f"Internal Server Error: {e}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)