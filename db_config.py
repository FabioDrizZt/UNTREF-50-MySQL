import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
def connect_to_db():
  try:
    connection = mysql.connector.connect(
      host=os.getenv("DB_HOST"),
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD"),
      database=os.getenv("DB_NAME"),
    )
    print('Conexión exitosa a la BD')
    return connection
  except mysql.connector.Error as err:
    print(f'Fallo la conexión a la BD: {err}')
    return None
    