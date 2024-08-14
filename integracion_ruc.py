import cx_Oracle
from datetime import datetime
from tu_ruc_python_client import get_contribuyente_by_search

# Configuración de conexión a la base de datos Oracle
config_db = {
    'user': 'usuario',
    'password': 'contrasena',
    'dsn': 'base_de_datos',
    'host': 'host',
    'port': 'puerto',
    'service_name': 'servicio'
}

# Cadena de conexión
dsn = cx_Oracle.makedsn(config_db['host'], config_db['port'], service_name=config_db['service_name'])

# Conectar a la base de datos Oracle
connection = cx_Oracle.connect(user=config_db['user'], password=config_db['password'], dsn=dsn)
cursor = connection.cursor()

# Limpiar datos existentes en la tabla
try:
    cursor.execute("DELETE FROM SCHEMA.TABLA")
    connection.commit()
except cx_Oracle.DatabaseError as e:
    print(f"Error al limpiar la tabla: {e}")
    connection.rollback()

# Consulta de inserción para SCHEMA.TABLA
insert_query = """
INSERT INTO SCHEMA.TABLA (CEDULA, NOMBRE, DIGITO_VERIFICADOR, RUC, ESTADO, FECHA_ACTUALIZACION)
VALUES (:cedula, :nombre, :dv, :ruc, :estado, TO_DATE(:fecha_actualizacion, 'YYYY-MM-DD'))
"""

# Conjunto para rastrear entradas únicas
unique_entries = set()

# Función para insertar datos en la tabla
def insert_data(cedula, nombre, dv, ruc, estado):
    fecha_actualizacion = datetime.today().strftime('%Y-%m-%d')
    entry = (cedula, nombre, dv, ruc, estado)
    if entry not in unique_entries:
        try:
            cursor.execute(insert_query, {
                'cedula': cedula,
                'nombre': nombre,
                'dv': dv,
                'ruc': ruc,
                'estado': estado,
                'fecha_actualizacion': fecha_actualizacion
            })
            connection.commit()
            unique_entries.add(entry)
            print(f"Insertado: {cedula}, {nombre}, {dv}, {ruc}, {estado}")
        except cx_Oracle.IntegrityError as e:
            print(f"Entrada duplicada o error al insertar datos: {e}")
        except cx_Oracle.DatabaseError as e:
            print(f"Error en la base de datos: {e}")

# Generar dinámicamente y buscar valores de RUC
for number in range(100, 100000001): #Editar los valores según sea necesario
    contribuyente_info = get_contribuyente_by_search(str(number))
        
    # Si la búsqueda devuelve datos, extraer la información relevante
    if 'contribuyentes' in contribuyente_info:
        for contribuyente in contribuyente_info['contribuyentes']:
                
            # Extraer los valores y guardarlos en variables
            doc = contribuyente.get('doc', None)
            nombre = contribuyente.get('razonSocial', None)
            dv = contribuyente.get('dv', None)
            ruc = contribuyente.get('ruc', None)
            estado = contribuyente.get('estado', None)
                
            # Insertar los datos en la base de datos
            insert_data(doc, nombre, dv, ruc, estado)

# Cerrar la conexión
cursor.close()
connection.close()
