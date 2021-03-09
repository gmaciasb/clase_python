# Ciclos

for valor in range(10):
    print(valor)
for valor in range(1, 11):
    print(valor)   
for valor in range(2, 100, 2):
    print(valor)  
for valor in range(2, 100, 2):
    print(valor)
    print("hola")
    
for i in range (1, 10):
    for j in range (1, 11):
        print(i, j)
    
# Ciclo while

while True:
    print('Hola')
    break
    
i = 2    
while i <= 10:
    print(i)
    # i = i + 2
    i += 2

# HUA que imprima el ganador de una elección 
# de dos cantidatos
cant_uno = 0
cant_dos = 0
num_votos = int(input('Digite la cantidad de personas a votar: '))
for n in range(1, num_votos+1):
    voto = int(input(f'Digite el voto {n} Candidato uno [1] o candidato dos [2] :')) 
    if voto == 1:
        cant_uno += 1
    else:
        cant_dos += 1
if(cant_uno > cant_dos):
    print(f'El ganador es Candidato Uno con {cant_uno} votos')
    print(f'El candidato dos obtuvo solo {cant_dos} votos')
elif(cant_dos > cant_uno):
    print(f'El ganador es Candidato Dos con {cant_dos} votos')
    print(f'El candidato uno obtuvo solo {cant_uno} votos')
else:
    print(f'Se presentó un empate con {cant_uno} votos para cada uno')   


# HUA que de las n notas de un estudiante calcule el promedio académico final  
suma = 0
n_notas = int(input('Digite el numero de notas del estudiante: '))
for n in range(1, n_notas+1):
    while True:
        notas = float(input(f'Digite la nota {n}: '))
        if notas >= 0 and notas <=5:
            break
    suma += notas
prom = suma / n_notas
prom = round(prom, 2)
print(f'El promedio de las {n_notas} notas es: {prom}')    

   
# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [True, False], ['Hola','Mundo'],[2.6, 4.5]]
for valor in a:
    print(valor)
    
for valor in b:
    print(valor)

for valor in c:
    print(valor)    
    
a[0] = 7
a = [2, 3, 4]
a.append(5) # Agrega el elemento al final de la lista
a.remove(3) # Elimina de la lista un elemento por su valor
a.pop() # Elimina el ultimo elemento del vector
a.pop(1) # Elimina un elemento por posición
a.clear() # Elimina todos los elementos del vector
# del a
4 in a # Busca el elemento 4 dentro de a
len(a) # Cantidad de elementos de la lista
b = a # Asigne de b en el mismo espacio de memoria de a
id(a) # Convierte en decimal la dirección en memoria de un objeto
b = a[:] # Copia de los elementos de a
c = b [0:3]
c = b[:3]
c = b[2:]

#Tuplas
## Tipo de datos inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'hola', True, 4.5)
a = (1, ['hola', 'Mundo'], True, 4.5)
a = (1,  ['hola', 'Mundo'], (True, False), 4.5)
b = a[:2]
4 in a

# Diccionario
# Mutable pero no ordenado

a = {'Nombre': 'Gabriel', 'apellido': 'Macias'}
a = {'1': 'Gabriel', '2': 'Macias'}
a['nombre']
a['nombre'] = 'Antonio'

# Funciones
def nombre_funcion():
    pass

def hola_mundo():
    print('Hola mundo')


def saludo(nombre='Mundo'):
    print(f'Hola {nombre}')
    
def suma(num1,num2):
   return num1 + num2

def operaciones(num1,num2):
   suma = num1 + num2
   rest = num1 - num2
   multip = num1 * num2
   div = round(num1 / num2, 2)
   return suma, resta, multip, div

resultados = operaciones (4, 5)
suma, resta, multip, div = resultados
_, _, _, div = resultados
_, _, _, div = operaciones (4,5)
    

    


    