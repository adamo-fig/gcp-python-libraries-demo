# FUNCIONES DE ALTO ORDEN
#   * Son aquellas funciones que reciben una función como parametro y pueden regresar una función o un valor 
#   * Las más utiles son map, filter y reduce

animales = ["perro","gato","charal","cotorro"]

def mapeoAnimales(animal):
    return animal.upper()

def filtroAnimales(animal):
    return animal.startswith("p")

# map() recibe una función de mapeo y el iterable a mapear
resultadoMapeo = map(mapeoAnimales, animales )
# filter() recibe una fución de filtro y el iterable a filtrar
resultadoFiltro = filter(filtroAnimales, animales )

print(list(resultadoMapeo))
print(list(resultadoFiltro))

#   Es posible utilizar notación lambda para craer la funciones
resultadoMapeo = map(lambda i: i.upper(), animales )
resultadoFiltro = filter(lambda i: i.startswith("c"), animales )

print(list(resultadoMapeo))
print(list(resultadoFiltro))

# REDUCE
#   * reduce no viene nativamente en python pero si en una librería nativa
#   * el resultado de reducir un iterable es una cadena

from functools import reduce

def reduceAnimales(valAnimalAnterior, valAnimalActual):
    if(valAnimalActual.startswith("c")):
        return valAnimalAnterior + "|" + valAnimalActual
    else:
        return ""
# Prueba de escritorio
# ["perro","gato","charal","cotorro"]

# perro
# perro|gato
# perro|gato|charal 
# perro|gato|charal|cotorro


stringAnimales = reduce(reduceAnimales ,animales)
print("Cadena reducida: ",stringAnimales)
