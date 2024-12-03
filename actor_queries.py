from db_config import connect_to_db

def get_actors():
  db = connect_to_db()
  try:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM actor LIMIT 25")
    actors = cursor.fetchall()
    return actors
  except Exception as e:
    print(f'Error: {e}')
    return None
  finally:
    cursor.close()
    db.close()

def get_actor_films(actor_id):
  db = connect_to_db()
  try:
    cursor = db.cursor()
    cursor.execute("""
      SELECT f.title 
      FROM film f
      JOIN film_actor fa ON f.film_id = fa.film_id
      WHERE fa.actor_id = %s
    """, (actor_id,))
    films = cursor.fetchall()
    return films
  except Exception as e:
    print(f'Error: {e}')
    return None
  finally:
    cursor.close()
    db.close()