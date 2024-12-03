from actor_queries import get_actors, get_actor_films
from tabulate import tabulate

print("Los primeros 25 actores son: ")
actors = get_actors()
if actors:
  print(tabulate(actors, headers=["#","nombre","apellido"], tablefmt="fancy_grid"))
else:
  print("No se encontraron actores")

actor_id=10
films = get_actor_films(actor_id)
if films:
  print(tabulate(films, headers=[f"Pelculas del actor: {actor_id}"], tablefmt="fancy_grid"))
else:
  print("No se encontraron actores")