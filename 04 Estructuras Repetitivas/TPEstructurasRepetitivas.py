# 1
for i in range(0, 101):
    print(i)

# 2
n = int(input("Ingresá un número entero: "))
x = abs(n)
if x == 0:
    print("Cantidad de dígitos: 1")
else:
    cont = 0
    while x > 0:
        cont += 1
        x //= 10
    print("Cantidad de dígitos:", cont)

# 3
a = int(input("Ingresá el primer entero: "))
b = int(input("Ingresá el segundo entero: "))

menor, mayor = (a, b) if a < b else (b, a)
acum = 0
for i in range(menor + 1, mayor):
    acum += i
print("Suma (excluyendo extremos):", acum)

# 4
acum = 0
while True:
    n = int(input("Ingresá un entero (0 para terminar): "))
    if n == 0:
        break
    acum += n
print("Total acumulado:", acum)

# 5
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adiviná el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Acertaste! Intentos: {intentos}")
        break
    else:
        print("No es ese. Probá de nuevo.")

# 6
for i in range(100, -1, -2):
    print(i)

# 7
n = int(input("Ingresá un entero positivo N: "))
while n < 0:
    n = int(input("Debe ser N ≥ 0. Ingresá de nuevo: "))

acum = 0
for i in range(0, n + 1):
    acum += i
print(f"Suma de 0 a {n}:", acum)

# 8
N = 100 # Cambiamos este valor para probar
pares = impares = positivos = negativos = 0

for _ in range(N):
    n = int(input("Ingresá un entero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    # si n == 0 no suma a positivos/negativos

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9
N = 100  # Cambiamos este valor para probar
acum = 0

for _ in range(N):
    n = float(input("Ingresá un número: "))
    acum += n

media = acum / N if N > 0 else 0.0
print("Media:", media)

#10
n = int(input("Ingresá un entero: "))
signo = -1 if n < 0 else 1
x = abs(n)

if x == 0:
    invertido = 0
else:
    invertido = 0
    while x > 0:
        ultimo = x % 10
        invertido = invertido * 10 + ultimo
        x //= 10

print("Invertido:", signo * invertido)


