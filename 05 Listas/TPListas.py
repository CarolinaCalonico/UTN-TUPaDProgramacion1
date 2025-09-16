# 1) Notas de 10 estudiantes
notas = [7, 8, 6, 9, 10, 4, 5, 8, 6, 7]  # podés reemplazar por input

# Mostrar la lista con bucle
print("Notas:")
for n in notas:
    print(n)

# Promedio
prom = sum(notas) / len(notas)
print("Promedio:", round(prom, 2))

# Máxima y mínima
mayor = max(notas)
menor = min(notas)
print("Nota más alta:", mayor)
print("Nota más baja:", menor)

# 2) Productos
productos = []
for i in range(5):
    prod = input(f"Ingresá el producto #{i+1}: ")
    productos.append(prod)

# Mostrar ordenados alfabéticamente (sorted no modifica la lista original)
ordenados = sorted(productos)
print("Productos ordenados:")
for p in ordenados:
    print(p)

# Eliminar uno elegido por el usuario
a_borrar = input("¿Qué producto querés eliminar?: ")
if a_borrar in productos:
    productos.remove(a_borrar)

print("Lista actualizada:")
for p in productos:
    print(p)

import random

# 3) Aleatorios
nums = [random.randint(1, 100) for _ in range(15)]

pares = []
impares = []
for x in nums:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print("Original:")
for x in nums:
    print(x)
print("Pares (", len(pares), "):")
for x in pares:
    print(x)
print("Impares (", len(impares), "):")
for x in impares:
    print(x)

# 4) Quitar repetidos 
valores = [3, 5, 3, 2, 5, 8, 2, 9, 9, 1]

sin_repetidos = []
for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)

print("Original:")
for v in valores:
    print(v)
print("Sin repetidos:")
for v in sin_repetidos:
    print(v)

# 5) Estudiantes
alumnos = []
for i in range(8):
    alumnos.append(input(f"Ingresá el nombre del estudiante #{i+1}: "))

accion = input("¿Querés 'agregar' o 'eliminar' un estudiante?: ").strip().lower()

if accion == "agregar":
    nuevo = input("Nombre a agregar: ")
    alumnos.append(nuevo)
elif accion == "eliminar":
    viejo = input("Nombre a eliminar: ")
    if viejo in alumnos:
        alumnos.remove(viejo)

print("Lista final:")
for a in alumnos:
    print(a)

# 6) Rotación derecha
nums = [10, 20, 30, 40, 50, 60, 70]  # ejemplo
# última al frente:
ultimo = nums.pop()     # saca el último
nums.insert(0, ultimo)  # lo pone al principio

print("Rotados a la derecha:")
for x in nums:
    print(x)

# 7) Temperaturas mínimas y máximas (7 días)
# Formato: [ [min, max], ..., 7 filas ]
temps = [
    [10, 18],
    [9, 20],
    [11, 17],
    [8, 22],
    [7, 19],
    [12, 21],
    [10, 16],
]

# Promedio de mínimas y de máximas
suma_min = 0
suma_max = 0
for par in temps:
    suma_min += par[0]
    suma_max += par[1]
prom_min = suma_min / len(temps)
prom_max = suma_max / len(temps)

print("Promedio mínimas:", round(prom_min, 2))
print("Promedio máximas:", round(prom_max, 2))

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
may_amp = None
dia_may = None
for i in range(len(temps)):
    amp = temps[i][1] - temps[i][0]
    if (may_amp is None) or (amp > may_amp):
        may_amp = amp
        dia_may = i

print("Mayor amplitud:", may_amp, "en", dias[dia_may])

# 8) Notas 5x3
# filas = estudiantes, columnas = materias
notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [8, 7, 9],
]

# Promedio de cada estudiante (fila)
print("Promedio por estudiante:")
for i in range(len(notas)):
    fila = notas[i]
    prom = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {round(prom, 2)}")

# Promedio de cada materia (columna)
print("Promedio por materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    prom = suma / len(notas)
    print(f"Materia {j+1}: {round(prom, 2)}")

# 9) Ta-Te-Ti
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        # mostrar con bucle elementos
        linea = ""
        for c in fila:
            linea += c + " "
        print(linea.strip())
    print()

turno = "X"
for jugada in range(9):  # hasta completar el tablero
    mostrar_tablero(tablero)
    print(f"Turno de {turno}")
    f = int(input("Fila (0-2): "))
    c = int(input("Columna (0-2): "))
    if 0 <= f < 3 and 0 <= c < 3 and tablero[f][c] == "-":
        tablero[f][c] = turno
        turno = "O" if turno == "X" else "X"
    else:
        print("Movimiento inválido, perdés el turno.")

# mostrar tablero final
print("Tablero final:")
mostrar_tablero(tablero)

# 10) Ventas
# filas = productos 1..4, columnas = días 1..7
ventas = [
    [5, 6, 4, 3, 7, 8, 6],
    [2, 3, 5, 4, 3, 2, 1],
    [9, 8, 7, 6, 5, 9, 10],
    [1, 2, 1, 3, 2, 4, 2],
]

# Total vendido por cada producto (fila)
print("Total por producto:")
totales_prod = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_prod.append(total)
    print(f"Producto {i+1}: {total}")

# Día con mayores ventas totales (sumar por columna)
totales_dia = []
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    totales_dia.append(suma)

dia_max = 0
for d in range(1, 7):
    if totales_dia[d] > totales_dia[dia_max]:
        dia_max = d

print("Día con mayores ventas totales: Día", dia_max + 1, "con", totales_dia[dia_max])

# Producto más vendido en la semana
prod_max = 0
for i in range(1, 4):
    if totales_prod[i] > totales_prod[prod_max]:
        prod_max = i

print("Producto más vendido en la semana: Producto", prod_max + 1, "con", totales_prod[prod_max])

