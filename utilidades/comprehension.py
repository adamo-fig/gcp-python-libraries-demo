animales = ["perro","gato","cotorro","charal"]

resultadoMapeo = [ animal.upper() + "1" for animal in animales]

print(resultadoMapeo)

resFiltro = [ animal for animal in animales if animal.startswith("c")]

print(resFiltro)

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

        
# [0, 1, 2, 3, 4]
resultCmp = [ [ i for i in range(5)] for i in range(5) ]


print(resultCmp)


for i in range (10):
    for j in range (10):
        print(i*j)


comprensionMultiplicar = [ [i*j  for j in range (10) ] for i in range (10) ]

print(comprensionMultiplicar)