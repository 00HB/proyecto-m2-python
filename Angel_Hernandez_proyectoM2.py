# Proyecto Módulo 2 - Fundamentos de Python
# Autor: Angel Hernandez
#
# Este archivo contiene dos ejercicios independientes:
# 1. Validar la longitud de una palabra.
# 2. Encontrar el cuadrante de un punto usando coordenadas X y Y.


print("===== RETO 1: LONGITUD DE UNA PALABRA =====")

# Pido una palabra al usuario.
palabra = input("Ingresa una palabra: ")

# Uso len() para saber cuántos caracteres tiene la palabra.
longitud = len(palabra)

# Reviso si la palabra tiene entre 4 y 8 letras.
if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta")

# Si tiene menos de 4 letras, muestro cuántas letras tiene.
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")

# Si no cumple las condiciones anteriores, entonces tiene más de 8 letras.
else:
    print(f"Sobran letras. Tiene {longitud} letras")


print("\n===== RETO 2: ENCUENTRA EL CUADRANTE =====")

# Pido las coordenadas al usuario.
# Uso int() porque input() recibe los datos como texto.
x = int(input("Ingrese X: "))
y = int(input("Ingrese Y: "))

# Guardo las coordenadas en una lista para usar una colección de datos.
coordenadas = [x, y]

# Tomo los valores desde la lista.
x = coordenadas[0]
y = coordenadas[1]

# Si alguna coordenada es 0, el punto no pertenece a ningún cuadrante.
if x == 0 or y == 0:
    print("Error: ninguna coordenada puede ser 0")

# X positiva y Y positiva: cuadrante I.
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")

# X negativa y Y positiva: cuadrante II.
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")

# X negativa y Y negativa: cuadrante III.
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")

# X positiva y Y negativa: cuadrante IV.
else:
    print("El punto se encuentra en el cuadrante IV")