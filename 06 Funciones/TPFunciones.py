# 1. imprimir_hola_mundo
def imprimir_hola_mundo():
    """Imprime un saludo básico en pantalla."""
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# 2. saludar_usuario(nombre)
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3. informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    """Muestra información personal del usuario."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4. calcular_area_circulo y calcular_perimetro_circulo
import math

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro de un círculo dado su radio."""
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5. segundos_a_horas
def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

# 6. tabla_multiplicar
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número recibido."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# 7. operaciones_basicas
def operaciones_basicas(a, b):
    """Devuelve una tupla con suma, resta, multiplicación y división."""
    return a + b, a - b, a * b, a / b

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div:.2f}")

# 8. calcular_imc
def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")

# 9. celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en °C: "))
print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}°F")

# 10. calcular_promedio
def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números."""
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")