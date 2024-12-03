import os
import platform

mi_variable = os.environ.get("USERNAME") # Puedes cambiar esto por un valor dinámico si lo necesitas.

if platform.system() == 'Windows':
    print("###############################")
    print("Usuario:", mi_variable)
    print("O.S.:", os.name)
    print("Sistema Operativo:", platform.system())
    print("###############################")
else:
    print("###############################")
    print("Usuario:", mi_variable)
    print("O.S.:", os.name)
    print("Sistema Operativo:", platform.system())
    print("###############################")

for variable, valor in os.environ.items():
    print(f"{variable}: {valor}")