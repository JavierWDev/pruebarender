from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configura la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ocupacion = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Crear la base de datos y las tablas si no existen
with app.app_context():
    db.create_all()

# Ruta principal que renderiza el formulario
@app.route('/')
def index():
    return render_template('form.html')

# Ruta para guardar los datos ingresados
@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        # Obtener datos del formulario
        ocupacion = request.form['ocupacion']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        correo = request.form['correo']
        password = request.form['password']
        
        # Crear un nuevo usuario
        nuevo_usuario = Usuario(ocupacion=ocupacion, nombre=nombre, apellido=apellido, 
                                edad=edad, correo=correo, password=password)

        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Redirigir a la página de inicio después de guardar
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error al guardar los datos: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)
