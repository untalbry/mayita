import csv
from flask import jsonify, request
from .models.user_model import User
import os

def register_routes(app):
    @app.route("/")
    def home():
        return jsonify({
            "Message": "app up and running successfully"
        })

    @app.route('/create_user', methods=['POST'])
    def create_user():
        # Ruta del archivo CSV
        user_csv = os.path.join(os.getcwd(), 'data/users.csv')
        data = request.json
        
        # Validar que todos los campos necesarios están presentes
        required_fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'curp']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos requeridos'}), 400
        
        user_id = User.get_next_id(user_csv)

        user = User(
            user_id=user_id,
            nombre=data['nombre'],
            apellido_paterno=data['apellido_paterno'],
            apellido_materno=data['apellido_materno'],
            fecha_nacimiento=data['fecha_nacimiento'],
            curp=data['curp']
        )
        
        # Si el archivo CSV no existe, crearlo y escribir los encabezados
        if not os.path.exists(user_csv):
            with open(user_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['user_id', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'curp'])

        # Guardar el usuario en el archivo CSV
        with open(user_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user.user_id, user.nombre, user.apellido_paterno, user.apellido_materno, user.fecha_nacimiento, user.curp])

        return jsonify({'message': 'Usuario creado exitosamente', 'user_id': user.user_id}), 201
