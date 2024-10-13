import csv
import random
from datetime import datetime

def generar_respuesta(opciones):
    return random.choice(opciones)

def generar_respuestas_multiples(opciones, max_selecciones):
    num_selecciones = random.randint(1, min(max_selecciones, len(opciones)))
    return random.sample(opciones, num_selecciones)

def generar_datos_usuario():
    datos = {
        "id_usuario": random.randint(1000, 9999),
        "fecha_encuesta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "edad": generar_respuesta(["18-25", "26-35", "36-45", "46-55", "56-65", "66+"]),
        "profesion": generar_respuesta(["Estudiante", "Empleado tiempo completo", "Empleado tiempo parcial", "Independiente", "Empresario", "Jubilado", "Desempleado", "Otro"]),
        "ingresos": ", ".join(generar_respuestas_multiples(["Salario fijo", "Freelance", "Rentas", "Dividendos", "Pensiones", "Negocios propios", "Comisiones", "Intereses", "Otro"], 3)),
        "gastos": ", ".join(generar_respuestas_multiples(["Vivienda", "Alimentación", "Transporte", "Servicios básicos", "Salud", "Educación", "Entretenimiento", "Deudas", "Ahorro", "Ropa", "Mantenimiento hogar", "Mascotas"], 3)),
        "emprendimiento": generar_respuesta(["No", "Sí"]),
        "tipo_emprendimiento": "",
        "casa": generar_respuesta(["No", "Sí, con hipoteca", "Sí, totalmente pagada", "Sí, heredada"]),
        "automovil": generar_respuesta(["No", "Sí, financiado", "Sí, totalmente pagado"]),
        "productos_financieros": ", ".join(generar_respuestas_multiples(["Cuenta de ahorros", "Cuenta corriente", "Tarjeta de crédito", "Préstamo personal", "Préstamo hipotecario", "Seguro de vida", "Seguro de automóvil", "Fondo de inversión", "Depósito a plazo fijo", "Cuenta de ahorro para el retiro", "Línea de crédito", "Crédito para negocio", "Ninguno"], 5)),
        "ingresos_mensuales": generar_respuesta(["Menos de $1,000", "$1,000 - $2,999", "$3,000 - $4,999", "$5,000 - $7,999", "$8,000 - $11,999", "$12,000 o más", "Prefiero no decir"]),
        "objetivo_financiero": generar_respuesta(["Ahorrar para emergencia", "Pagar deudas", "Comprar propiedad", "Iniciar negocio", "Ahorrar para educación", "Invertir en bolsa", "Comprar vehículo", "Otro"]),
        "conocimiento_financiero": generar_respuesta(["Principiante", "Intermedio", "Avanzado", "Experto"]),
        "frecuencia_transacciones": generar_respuesta(["Diariamente", "Semanalmente", "Mensualmente", "Raramente", "Nunca"])
    }
    
    if datos["emprendimiento"] == "Sí":
        datos["tipo_emprendimiento"] = generar_respuesta(["Comercio minorista", "Servicios profesionales", "Tecnología", "Gastronomía", "Turismo", "Educación", "Salud", "Artesanía", "Agricultura", "Construcción", "Otro"])
    
    return datos

def generar_csv(nombre_archivo, num_registros):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        campos = ["id_usuario", "fecha_encuesta", "edad", "profesion", "ingresos", "gastos", "emprendimiento", "tipo_emprendimiento", "casa", "automovil", "productos_financieros", "ingresos_mensuales", "objetivo_financiero", "conocimiento_financiero", "frecuencia_transacciones"]
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        
        escritor.writeheader()
        for _ in range(num_registros):
            escritor.writerow(generar_datos_usuario())

if __name__ == "__main__":
    nombre_archivo = "perfilamiento_bancario.csv"
    num_registros = 100  # Puedes ajustar este número según la cantidad de registros que desees generar
    generar_csv(nombre_archivo, num_registros)
    print(f"Se ha generado el archivo '{nombre_archivo}' con {num_registros} registros de perfilamiento bancario.")