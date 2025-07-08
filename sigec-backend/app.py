from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Configuración de CORS
CORS(app) 

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sigec_db'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    genero = db.Column(db.String(10))
    numero_identificacion = db.Column(db.String(50), unique=True)

# Crear las tablas
with app.app_context():
    db.create_all()

# GET /pacientes
@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{
        'id': p.id,
        'nombre': p.nombre,
        'apellido': p.apellido,
        'fecha_nacimiento': p.fecha_nacimiento.isoformat() if p.fecha_nacimiento else None,
        'genero': p.genero,
        'numero_identificacion': p.numero_identificacion
    } for p in pacientes])

# POST /pacientes
@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    data = request.json
    paciente = Paciente(
        nombre=data['nombre'],
        apellido=data['apellido'],
        fecha_nacimiento=data.get('fecha_nacimiento'),
        genero=data.get('genero'),
        numero_identificacion=data['numero_identificacion']
    )
    db.session.add(paciente)
    db.session.commit()
    return jsonify({'id': paciente.id}), 201

# GET /pacientes/<id>
@app.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    return jsonify({
        'id': paciente.id,
        'nombre': paciente.nombre,
        'apellido': paciente.apellido,
        'fecha_nacimiento': paciente.fecha_nacimiento.isoformat() if paciente.fecha_nacimiento else None,
        'genero': paciente.genero,
        'numero_identificacion': paciente.numero_identificacion
    })

if __name__ == '__main__':
    app.run(debug=True)

# Nota: Asegúrate de instalar las dependencias necesarias: 
# pip install Flask Flask-SQLAlchemy pymysql  # Para MySQL
# Asegúrate de tener la base de datos creada y las credenciales correctas.
# También, asegúrate de que el servidor de la base de datos esté en funcionamiento.
# Puedes probar la API usando herramientas como Postman.
