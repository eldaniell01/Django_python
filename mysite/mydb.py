import pymysql




conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password= '123'
)
cursor = conexion.cursor()
cursor.execute('CREATE DATABASE cliente')
print('completado')