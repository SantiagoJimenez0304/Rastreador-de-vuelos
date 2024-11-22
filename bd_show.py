import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('database.db')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejecutar una consulta para ver los datos en la tabla "User"
cursor.execute("SELECT * FROM user")

# Obtener los resultados
rows = cursor.fetchall()

# Mostrar los resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
