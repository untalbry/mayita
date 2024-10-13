import csv  
import os

class User:
    def __init__(self, user_id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, curp):
        self.user_id = user_id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp

    @staticmethod
    def get_next_id(archivo_csv):
        if not os.path.exists(archivo_csv):
            return 1 
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:
                last_id = int(rows[-1][0])
                return last_id + 1
            else:
                return 1  
