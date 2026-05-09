# Proyecto Módulo 2: Validación y operaciones de datos

## Descripción

Este proyecto corresponde al Módulo 2 de Fundamentos de Python.

El objetivo principal es practicar el uso de estructuras de control, variables, entrada de datos, validaciones, conversión de datos y colecciones básicas en Python.

El programa contiene dos retos independientes:

1. Validar la longitud de una palabra.
2. Identificar el cuadrante de un punto en el plano cartesiano.

Aunque los dos retos no están relacionados directamente entre sí, ambos sirven para practicar lógica condicional usando `if`, `elif` y `else`.

---

## Reto 1: Longitud de una palabra

En este primer reto, el programa solicita al usuario que ingrese una palabra.

Después, el programa cuenta cuántos caracteres tiene la palabra usando la función `len()` y valida si la longitud se encuentra dentro del rango solicitado.

La palabra debe tener entre 4 y 8 letras para ser considerada correcta.

### Reglas del reto 1

- Si la palabra tiene entre 4 y 8 letras, el programa muestra el mensaje:

```text
La palabra es correcta
```

- Si la palabra tiene menos de 4 letras, el programa muestra el mensaje:

```text
Hacen falta letras. Solo tiene N letras
```

- Si la palabra tiene más de 8 letras, el programa muestra el mensaje:

```text
Sobran letras. Tiene N letras
```

En los mensajes anteriores, `N` representa la cantidad de letras que tiene la palabra ingresada.

### Cómo funciona el reto 1

Primero se pide una palabra al usuario con `input()`:

```python
palabra = input("Ingresa una palabra: ")
```

Después se cuenta la cantidad de caracteres usando `len()`:

```python
longitud = len(palabra)
```

Luego se usan condicionales para revisar si la palabra cumple con el rango solicitado:

```python
if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras")
else:
    print(f"Sobran letras. Tiene {longitud} letras")
```

### Ejemplos del reto 1

#### Ejemplo 1: palabra correcta

En este ejemplo, la palabra tiene 4 letras, por lo tanto está dentro del rango permitido.

```text
Ingresa una palabra: casa
La palabra es correcta
```

#### Ejemplo 2: palabra con menos de 4 letras

En este ejemplo, la palabra tiene 3 letras, por lo tanto el programa indica que hacen falta letras.

```text
Ingresa una palabra: sol
Hacen falta letras. Solo tiene 3 letras
```

#### Ejemplo 3: palabra con más de 8 letras

En este ejemplo, la palabra tiene más de 8 letras, por lo tanto el programa indica que sobran letras.

```text
Ingresa una palabra: computadora
Sobran letras. Tiene 11 letras
```

#### Ejemplo 4: otra palabra correcta

En este ejemplo, la palabra tiene 6 letras, así que también está dentro del rango solicitado.

```text
Ingresa una palabra: python
La palabra es correcta
```

### Tabla de pruebas del reto 1

| Palabra ingresada | Número de letras | Resultado esperado |
|---|---:|---|
| sol | 3 | Hacen falta letras. Solo tiene 3 letras |
| casa | 4 | La palabra es correcta |
| python | 6 | La palabra es correcta |
| programa | 8 | La palabra es correcta |
| computadora | 11 | Sobran letras. Tiene 11 letras |

---

## Reto 2: Encuentra el cuadrante

En el segundo reto, el programa solicita al usuario dos números:

- Coordenada X
- Coordenada Y

Estas coordenadas representan un punto dentro del plano cartesiano.

El objetivo del programa es identificar en cuál de los cuatro cuadrantes se encuentra el punto, dependiendo de si las coordenadas son positivas o negativas.

### Qué es un cuadrante

Un cuadrante es una de las cuatro partes en las que se divide el plano cartesiano.

El plano cartesiano se divide usando dos ejes:

- Eje X: línea horizontal.
- Eje Y: línea vertical.

Dependiendo de los signos de X y Y, el punto puede estar en uno de los cuatro cuadrantes.

### Reglas del reto 2

El programa usa las siguientes reglas para identificar el cuadrante:

| Coordenada X | Coordenada Y | Cuadrante |
|---|---|---|
| Positiva | Positiva | Cuadrante I |
| Negativa | Positiva | Cuadrante II |
| Negativa | Negativa | Cuadrante III |
| Positiva | Negativa | Cuadrante IV |

También se debe validar que ninguna coordenada sea 0.

Si X o Y es igual a 0, el programa muestra un mensaje de error, porque el punto no pertenece a ningún cuadrante.

### Cómo funciona el reto 2

Primero, el programa pide al usuario que ingrese los valores de X y Y.

Como los datos ingresados con `input()` se reciben como texto, se usa `int()` para convertirlos a números enteros.

```python
x = int(input("Ingrese X: "))
y = int(input("Ingrese Y: "))
```

Después, las coordenadas se guardan en una lista llamada `coordenadas`.

```python
coordenadas = [x, y]
```

Esto permite practicar el uso de colecciones de datos en Python.

Luego se toman los valores desde la lista:

```python
x = coordenadas[0]
y = coordenadas[1]
```

Después, el programa revisa si alguna coordenada es igual a 0.

```python
if x == 0 or y == 0:
    print("Error: ninguna coordenada puede ser 0")
```

Si ninguna coordenada es 0, el programa usa condiciones para identificar el cuadrante correspondiente.

```python
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")
else:
    print("El punto se encuentra en el cuadrante IV")
```

### Ejemplos del reto 2

#### Ejemplo 1: cuadrante I

```text
Ingrese X: 3
Ingrese Y: 5
El punto se encuentra en el cuadrante I
```

#### Ejemplo 2: cuadrante II

```text
Ingrese X: -3
Ingrese Y: 2
El punto se encuentra en el cuadrante II
```

#### Ejemplo 3: cuadrante III

```text
Ingrese X: -4
Ingrese Y: -7
El punto se encuentra en el cuadrante III
```

#### Ejemplo 4: cuadrante IV

```text
Ingrese X: 4
Ingrese Y: -5
El punto se encuentra en el cuadrante IV
```

#### Ejemplo 5: coordenada igual a 0

```text
Ingrese X: 0
Ingrese Y: 5
Error: ninguna coordenada puede ser 0
```

### Tabla de pruebas del reto 2

| X | Y | Resultado esperado |
|---:|---:|---|
| 3 | 5 | El punto se encuentra en el cuadrante I |
| -3 | 2 | El punto se encuentra en el cuadrante II |
| -4 | -7 | El punto se encuentra en el cuadrante III |
| 4 | -5 | El punto se encuentra en el cuadrante IV |
| 0 | 5 | Error: ninguna coordenada puede ser 0 |
| 8 | 0 | Error: ninguna coordenada puede ser 0 |

---

## Cómo hice el programa

Primero dividí el proyecto en dos partes, ya que cada reto resuelve un problema diferente.

En el primer reto usé una variable llamada `palabra` para guardar el texto ingresado por el usuario. Después utilicé la función `len()` para obtener la cantidad de caracteres de la palabra. Ese valor lo guardé en una variable llamada `longitud`.

Después usé estructuras condicionales para validar la longitud:

- Con `if` revisé si la palabra tenía entre 4 y 8 letras.
- Con `elif` revisé si tenía menos de 4 letras.
- Con `else` cubrí el caso donde la palabra tenía más de 8 letras.

En el segundo reto usé `input()` para pedir las coordenadas `X` y `Y`. Como los datos que se ingresan con `input()` llegan como texto, utilicé `int()` para convertirlos a números enteros.

También guardé las coordenadas en una lista llamada `coordenadas`, para practicar el uso de colecciones de datos en Python.

Después tomé los valores de esa lista y usé condicionales para determinar el cuadrante:

- Si alguna coordenada era 0, el programa mostraba un error.
- Si las dos coordenadas eran positivas, el punto estaba en el cuadrante I.
- Si X era negativa y Y positiva, el punto estaba en el cuadrante II.
- Si las dos coordenadas eran negativas, el punto estaba en el cuadrante III.
- Si X era positiva y Y negativa, el punto estaba en el cuadrante IV.

---

## Archivo principal

El archivo principal del proyecto es:

```text
Angel_Hernandez_proyectoM2.py
```

Este archivo contiene la solución de ambos retos y comentarios que explican el funcionamiento de las partes principales del programa.

---

## Cómo ejecutar el programa

Para ejecutar el programa se necesita tener Python instalado en la computadora.

Primero se debe abrir una terminal en la carpeta donde se encuentra el archivo del proyecto.

Después se puede ejecutar el programa con el siguiente comando:

```bash
python Angel_Hernandez_proyectoM2.py
```

En algunos sistemas también se puede ejecutar con:

```bash
python3 Angel_Hernandez_proyectoM2.py
```

---

## Estructura del proyecto

```text
.
├── Angel_Hernandez_proyectoM2.py
└── README.md
```

---

## Tecnologías utilizadas

- Python 3
- Git
- GitHub

---

## Conceptos utilizados

En este proyecto utilicé los siguientes conceptos de Python:

- Variables
- Entrada de datos con `input()`
- Conversión de datos con `int()`
- Función `len()`
- Estructuras condicionales `if`, `elif` y `else`
- Operadores de comparación
- Operadores lógicos `and` y `or`
- Listas como colección de datos
- Comentarios dentro del código

---

## Aprendizajes

Con este proyecto practiqué el uso de estructuras de control como `if`, `elif` y `else`.

También reforcé el uso de variables, entrada de datos con `input()`, conversión de datos con `int()` y validaciones usando operadores lógicos.

Además, utilicé una lista para guardar las coordenadas del punto, lo cual me ayudó a practicar el uso básico de colecciones de datos en Python.

Este proyecto me ayudó a entender mejor cómo analizar un problema paso a paso y cómo convertir una serie de reglas en código.

---

## Reflexión del bootcamp

Hasta ahora, el bootcamp me ha ayudado a mejorar mi lógica de programación.

He aprendido que antes de escribir código es importante entender bien el problema, identificar qué datos se necesitan y pensar en las condiciones que se deben cumplir.

También me di cuenta de que probar el programa con diferentes entradas es importante para asegurarme de que funcione correctamente en varios casos.

Aunque estos ejercicios son sencillos, me ayudaron a reforzar conceptos importantes de Python y a tener más confianza al momento de resolver problemas usando código.
