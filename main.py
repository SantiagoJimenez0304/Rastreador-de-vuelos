from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import folium
from my_flight_api import FlightRadar24API



app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelo para la tabla de usuarios
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validar credenciales
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user"] = username  # Iniciar sesión
            return redirect(url_for("mapa_vuelos"))
        else:
            error = "Usuario o contraseña incorrectos. Por favor, intenta de nuevo."

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Verificar si el usuario ya existe
        if User.query.filter_by(username=username).first():
            message = "El usuario ya existe. Por favor, elige otro."
        else:
            # Crear nuevo usuario con contraseña hasheada
            hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            message = "Registro exitoso. ¡Ahora puedes iniciar sesión!"
            return redirect(url_for("login"))

    return render_template("register.html", message=message)

@app.route("/mapa")
def mapa_vuelos():
    if "user" not in session:
        return redirect(url_for("login"))

    # Crear instancia de la API y obtener los vuelos
    fr_api = FlightRadar24API()
    flights = fr_api.get_flights()

    # Crear el mapa usando Folium
    mapa = folium.Map(location=[20, 0], zoom_start=2)  # Ubicación inicial centrada en el mundo

    # Agregar marcadores para cada vuelo
    for flight in flights:
        if flight.latitude and flight.longitude:
            folium.Marker(
                location=[flight.latitude, flight.longitude],
                popup=f"Vuelo: {flight.callsign}\nAerolínea: {flight.airline_iata}",
                icon=folium.Icon(color="blue", icon="plane", prefix="fa")
            ).add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save("templates/mapa_vuelos.html")
    return render_template("mapa_vuelos.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
