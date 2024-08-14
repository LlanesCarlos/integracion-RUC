# integracion-RUC
Script de Python que se conecta a una base de datos Oracle, obtiene información de contribuyentes mediante una API de terceros e inserta registros únicos en una tabla especificada.

Requisitos

    Python 3.x
    Librerías:
        cx_Oracle
        tu_ruc_python_client (cliente API para obtener la información de los contribuyentes)
        datetime


Instalar las dependencias necesarias:


    pip install cx_Oracle tu_ruc_python_client

Configuración

Antes de ejecutar el script, actualiza los valores de conexión a la base de datos en la sección config_db del archivo integracion_ruc.py:


    config_db = {
        'user': 'usuario',            # Usuario de la base de datos
        'password': 'contrasena',     # Contraseña del usuario
        'dsn': 'base_de_datos',       # Nombre del Data Source Name
        'host': 'host',               # Dirección del servidor Oracle
        'port': 'puerto',             # Puerto del servicio Oracle
        'service_name': 'servicio'    # Nombre del servicio de Oracle
    }


Uso

Ejecuta el script para iniciar la extracción de información de contribuyentes y su inserción en la base de datos Oracle:

    python3 integracion_ruc.py


Funcionamiento

    Conexión a Oracle: El script se conecta a una base de datos Oracle utilizando cx_Oracle.
    Obtención de Datos: Se utilizan números consecutivos para buscar información de contribuyentes a través de la API externa.
    Inserción en la Base de Datos: Solo se insertan registros únicos en la tabla de la base de datos especificada.
    Manejo de Errores: El script maneja posibles errores de integridad y de base de datos durante la inserción de datos.

Agradecimientos

Expreso mi más sincero agradecimiento a Sebastián Álvarez por desarrollar la librería tu-ruc-python-client. Sin su valiosa contribución, este proyecto no habría sido posible. Su esfuerzo y dedicación han sido fundamentales para el éxito de esta iniciativa.
https://github.com/ithdev/tu-ruc-python-client
