# Todo tipo de erroes pueden ocurrir en python, la mas facil de comprobar es 

try:
    div = 10/0
except Exception as e: 
    print("Ocurrio un problema en la divisin", e)

finally: 
    print("Okey acabo el proceso")