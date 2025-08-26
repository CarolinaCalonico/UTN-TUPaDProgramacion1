# TP 1 Estructuras Secuenciales: Carolina Calonico

# Ejercicio 1
# La siguiente línea imprime el mensaje "Hola, Mundo!" en la pantalla.

print("Hola Mundo!")

# Ejercicio 2
# Ingresamos el nombre y almacenamos su respuesta en la variable "nombre"
nombre = input("Por favor, ingrese su nombre: ")

# Imprimimos el saludo utilizando printf
print(f"Hola {nombre}!")

# Ejercicio 3
# Pedimos al usuario que se ingresen sus datos y se almacenan en las variables nombre, apellido, edad, lugar_de_residencia
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")

# Imprimimos la oración utilizando printf
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# Ejercicio 4
# Importamos la librería math ya que la necesitaremos para utilizar el número pi
import math

# Ingresamos el radio del circulo y almacenamos su respuesta en la variable "radio_circulo"
# Hacemos la conversion del dato ingresado a float (decimal) ya que usaremos el radio para cálculos matemáticos.
radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))

# Realizamos el cálculo del área del círculo
area_circulo = math.pi * (radio_circulo)**2

# Realizamos el cálculo del perímetro del círculo
perimetro_circulo = 2 * math.pi * radio_circulo

# Imprimimos ambos resultados por pantalla
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

# Ejercicio 5
# Empezamos pidiendo al usuario que ingrese la cantidad de segundos y almacenando su respuesta en la variable "cantidad_segundos"
# Hacemos la conversión del dato ingresado a "float" (decimal).
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))

# Realizamos la conversión de segundos a horas, sabiendo que una hora equivale a 3600 segundos
cantidad_horas = round(cantidad_segundos / 3600, 2)

# Imprimimos el resultado por pantalla
print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")

# Ejercicio 6
# Empezamos pidiendo al usuario que ingrese un número entero y almacenando su respuesta en la variable "numero_a_multiplicar"
# Como usaremos numero_a_multiplicar para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato int, por lo que hacemos la conversión al declarar la variable
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))

# Realizamos las multiplicaciones correspondientes
numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9

# Imprimimos el resultado por pantalla. En este caso hacemos una impresión de varias líneas por lo que usamos comillas triples
print(f"""
{numero_a_multiplicar} x 0 = {numero_por_0}
{numero_a_multiplicar} x 1 = {numero_por_1}
{numero_a_multiplicar} x 2 = {numero_por_2}
{numero_a_multiplicar} x 3 = {numero_por_3}
{numero_a_multiplicar} x 4 = {numero_por_4}
{numero_a_multiplicar} x 5 = {numero_por_5}
{numero_a_multiplicar} x 6 = {numero_por_6}
{numero_a_multiplicar} x 7 = {numero_por_7}
{numero_a_multiplicar} x 8 = {numero_por_8}
{numero_a_multiplicar} x 9 = {numero_por_9}
""")

# Ejercicio 7
# Empezamos pidiendo al usuario que ingrese dos números y almacenando sus respuestas en variables
# Como usaremos dichas variables para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato float, por lo que hacemos la conversión al declarar la variable
numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))

# Realizamos la suma y la almacenamos en la variable suma_a_b
suma_a_b = numero_a + numero_b

# Realizamos la división y la almacenamos en la variable division_a_b. Redondeamos a 2 decimales.
division_a_b = round(numero_a / numero_b, 2)

# Realizamos la multiplicación y la almacenamos en la variable multiplicacion_a_b
multiplicacion_a_b = numero_a * numero_b

# Realizamos la resta y la almacenamos en la variable resta_a_b
resta_a_b = numero_a - numero_b

# Imprimimos el resultado por pantalla. En este caso hacemos una impresión de varias líneas por lo que usamos comillas triples
print(f"""
Resultado de la suma: {suma_a_b}
Resultado de la división: {division_a_b}
Resultado de la multiplicación: {multiplicacion_a_b}
Resultado de la resta: {resta_a_b}
""")

# Ejercicio 8
# Empezamos pidiendo al usuario que ingrese su peso y su altura y almacenando sus respuestas en variables
# Como usaremos dichas variables para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato float, por lo que hacemos la conversión al declarar la variable
peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

# Realizamos el cálculo del IMC y los almacenamos en la variable imc. Redondeamos a 2 decimales
imc = round(peso / altura**2, 2)

# Imprimimos por pantalla el resultado
print(f"Su IMC es de: {imc}.")

# Ejercicio 9
# Empezamos pidiendo al usuario que ingrese la temperatura en grados Celsius y almacenando su valor en la variable temperatura_celsius
# Como usaremos dicha variable para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato float, por lo que hacemos la conversión al declarar la variable
temperatura_celsius = float(input("Por favor, una temperatura en °C: "))

# Realizamos la conversión de grados Celsius a grados Fahrenheit y almacenamos el resultado en la variable temperatura_fahrenheit. Redondeamos a 2 decimales
temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)

# Imprimimos por pantalla el resultado
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")

# Ejercicio 10
# Empezamos pidiendo al usuario que ingrese 3 números y almacenando sus respuestas en variables
# Como usaremos dichas variables para cálculos matemáticos necesitamos que el valor ingresado sea un tipo de dato float, por lo que hacemos la conversión al declarar la variable
numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))

# Realizamos la suma y la almacenamos en la variable suma_a_b_c
suma_a_b_c = numero_a + numero_b + numero_c

# Calculamos el promeido y lo almacenamos en la variable promedio_a_b_c. Redondeamos a 2 decimales.
promedio_a_b_c = round(suma_a_b_c/3, 2)

# Imprimimos por pantalla el resultado
print(f"El promedio de los números ingresados es {promedio_a_b_c}.")