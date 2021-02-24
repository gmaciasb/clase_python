# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicación
a = 5
b = 2
c = a * b
print(c)

# División
a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# Potencia
a = 5
b = 2
c = a ** b
print(c)

# Raiz cuadrada
a = 16
b = a ** (1/2)
print(b) 

# import math
# raiz = math.sqrt(16)
# print(raiz)

# Tipos de datos

# String str

a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Gabriel"'

print(a)
print(b)
print(c)

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero
a = '3'
y = int(a)
print(y)
print(type(y))

# Convertir de x a decimal
a = '3'
y = float(a)
print(y)
print(type(y))

# Convertir de x a decimal
a = '3'
y = str(a)
print(y)
print(type(y))

# Concatenaciones

a = 'Hola'
b = 'mundo'
c = a + ' ' + b
print(c)

a = 'Hola'
b = a * 6
print(b)


# Capturar por pantalla

# nombre = input('Digite su nombre: ')
# print('Hola', nombre)

# print('Digite su nombre: ')
# nombre = input()
# print('Hola', nombre)

# Haga una suma de dos numeros e imprima su resultado
# numero_uno = int(input('Digite el numero uno: '))
# numero_dos = int(input('Digite el numero dos: '))
# suma = numero_uno + numero_dos
# print(suma)
# print(f'la suma es: {suma}')

# Haga lea un número y lo eleve al cuadrado
# numero = int(input('Digite el numero: '))
# cuadrado = numero ** 2
# print(f'el resultado de elevar {numero} al cuadrado es:{cuadrado}')

# Haga un algoritmo que tome el valor del producto, le aplique 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado

vproducto = float(input('Digite el valor del producto: $'))
descuento = vproducto * 0.2
vfinal = vproducto - descuento
print(f'El valor inicial del producto es: ${vproducto: ,}')
print(f'El valor del descuento es: ${descuento: ,}')
print(f'El valor ahorrado es: ${descuento: ,}')


# Condicionales

# Tabla de verdad

# Tabla del and
# v and v = v
# v and f = f
# f and f = f
# f and v = f

# Tabla de verdad de or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

# Tabla del and
print(True and True)
print(True and False)
print(False and False)
print(False and True)

# Tabla del or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negación
print(not True)
print(not False)

# Jerarquía de operaciones
# 1. Parentesis y llaves
# 2. Potencia y Raise
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquia para operaciones booleanas
# 1. Parentesis y llaves
# 2. Tabla de verdad

# Mas de dons condicionales al mismo tiempo
print(True and False and True or False or True or True)
print(True and (False and True) or False or (True or True))

# Estructura if
# if (x > 0):
#    print('1')
# else:
#    print('2')    
# print('3')   

# Haga que dada la edad de una persona indique si es mayor 
# o es menos de edad
edad = int(input('Digite la edad de la persona: '))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')    


# Mas de de dos condicionales al mismo tiempo
#print(True and False and True or False or True or True)
#print() 

# Haga un algoritmo para saber si una persona paso la nota
# nota = float(input('Digite la nota de la asignatura'))
# if nota >= 3:
#    print(f'Aprobó la asignaruta con una nota de {nota}.')
# else:
#    print(f'Reprobo la asignaruta con una nota de {nota}.')
    
# Haga un algoritmo para saber si una persona paso la nota
nota = float(input('Digite la nota de la asignatura'))
if nota < 0 or nota > 5:
    print(f'No es una nota valida')
elif nota >= 3: 
    print(f'Aprobó la asignatura con una nota de {nota}.')
else:
    print(f'Reprobo la asignaruta con una nota de {nota}.')   
   
# HUA que dado un número n diga si es negativo, positivo
# o cero.   

n = int(input('Digite el valor de n :'))
if n > 0:
    print(f'{n} es positivo')
elif n < 0:
    print(f'{n} es negativo')
else:
    print('El numero es cero')
    
    
    
    