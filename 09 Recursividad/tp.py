# 1) Factorial recursivo + mostrar factoriales desde 1 hasta n
def factorial(n):
    if n == 0 or n == 1:   # Caso base
        return 1
    else:                  # Caso recursivo
        return n * factorial(n - 1)

# Programa principal
num = int(input("Ingresá un número: "))

print(f"Factoriales desde 1 hasta {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Fibonacci recursivo + mostrar la serie completa hasta n
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Programa principal
n = int(input("Mostrar serie Fibonacci hasta la posición: "))

print("Serie Fibonacci:")
for i in range(n + 1):
    print(fibonacci(i), end=" ")
print()

# 3) Potencia recursiva (n^m)
def potencia(n, m):
    if m == 0:        # Caso base
        return 1
    else:
        return n * potencia(n, m - 1)

# Programa principal
base = int(input("Base: "))
exp = int(input("Exponente: "))

print(f"{base}^{exp} = {potencia(base, exp)}")

# 4) Conversión recursiva de decimal a binario (string)
def decimal_a_binario(n):
    if n == 0:  # Caso base
        return "0"
    if n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
num = int(input("Número decimal a convertir: "))
print(f"Binario: {decimal_a_binario(num)}")

# 5) es_palindromo(palabra) – recursivo sin usar [::-1]
def es_palindromo(palabra):
    if len(palabra) <= 1:   # Caso base
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Programa principal
p = input("Ingresá una palabra sin espacios: ").lower()
print("¿Es palíndromo?", es_palindromo(p))

# 6) suma_digitos(n) sin convertir a string
def suma_digitos(n):
    if n < 10:     # Caso base
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Programa principal
num = int(input("Número para sumar sus dígitos: "))
print(f"Suma de dígitos: {suma_digitos(num)}")

# 7) contar_bloques(n) – Pirámide
def contar_bloques(n):
    if n == 1:      # Caso base
        return 1
    else:
        return n + contar_bloques(n - 1)

# Programa principal
niveles = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(niveles)}")

# 8) contar_digito(numero, digito)
def contar_digito(numero, digito):
    if numero == 0:   # Caso base
        return 0
    ultimo = numero % 10
    suma = contar_digito(numero // 10, digito)
    if ultimo == digito:
        return 1 + suma
    else:
        return suma

# Programa principal
num = int(input("Número: "))
d = int(input("Dígito a buscar: "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")