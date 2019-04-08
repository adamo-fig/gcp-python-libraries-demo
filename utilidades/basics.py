# 1) HOLA MUNDO
print("Hola mundo")

# 2) Variables
#   * No se declaran, simplemente se asignan
#   * Las variables booleanas van con mayusculas 

var_string =""
var_bool = True
var_int = 1
var_float= 3.192

print(type(var_string), type(var_bool) , type(var_int), type(var_float))

# 3)  LISTAS 
#   * Pueden guardar elementos de tipos diferentes
#   * Sumar una lista concatene los elementos
lista1 = [1, 2 , 5]
lista2 = [ "elemento" , 0 , False , 9.0001]

print( lista2)
print( lista2[0:2])

# 4) Ciclos 
#   * for itera sobre elementos iterables, lo mas comun es el range()

for i in range(10):
    print(i)

for a in "cadena de python":
    print(a)

for b in [2,4,8,9]:
    print(b)

#   * While
i=0
while i < 10:
    print(i)
    i += 1

# 5) condicional operadores https://www.w3schools.com/python/python_operators.asp
#   * No  hay ++ los operadores logicos and or not

def esVerdad():
    if( 1==1 and 2==2):
        print("Es verdad")

esVerdad()

# 6) Tuplas

tuple = (1,2,3,4)

print(tuple[2])
tuple[2] = 4

# 6) Dicionarios


