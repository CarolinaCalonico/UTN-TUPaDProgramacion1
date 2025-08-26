# TP 3 Estructuras Condicionales: Carolina Calonico

# Ejercicio 1

edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Es mayor de edad")

# Ejercicio 2
nota = float(input("Ingresá tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingresá un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4

edad = int(input("Ingresá tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# Ejercicio 5
contrasena = input("Ingresá una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
import random
from statistics import mean, median, mode

# Generar la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
mu = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
mo = mode(numeros_aleatorios)

# Determinar el sesgo según la consigna
if mu == med == mo:
    sesgo = "Sin sesgo"
elif mu > med and med > mo:
    sesgo = "Sesgo positivo (a la derecha)"
elif mu < med and med < mo:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "No coincide exactamente con los tres casos"

# Mostrar resultados
print("Lista de números:", numeros_aleatorios)
print(f"Media: {mu:.2f}")
print(f"Mediana: {med}")
print(f"Moda: {mo}")
print("Resultado:", sesgo)

# Ejercicio 7
texto = input("Ingresá una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)

# Ejercicio 8
nombre = input("Ingresá tu nombre: ")
opcion = int(input("Elegí una opción (1 = mayúsculas, 2 = minúsculas, 3 = primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# Ejercicio 9
magnitud = float(input("Ingresá la magnitud (escala de Richter): "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  # magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"

print("Categoría:", categoria)

# Ejercicio 10
# Pedimos hemisferio, mes (1-12) y día (1-31)
hem = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresá el mes (1-12): "))
dia = int(input("Ingresá el día (1-31): "))

# Normalizamos una tupla (mes, día) para comparar con los intervalos "incluidos"
fecha = (mes, dia)

def en_rango(fecha, inicio, fin):
    """
    Devuelve True si 'fecha' está entre 'inicio' y 'fin' (ambos inclusive).
    Maneja rangos que cruzan fin de año (ej.: 21/12 a 20/03).
    Cada fecha es (mes, día).
    """
    if inicio <= fin:
        return inicio <= fecha <= fin
    else:
        # Cruza el año: es válido si (fecha >= inicio) o (fecha <= fin)
        return fecha >= inicio or fecha <= fin

# Rangos según la tabla (incluidos)
# 21/12–20/03, 21/03–20/06, 21/06–20/09, 21/09–20/12
r_invierno_norte = ( (12, 21), (3, 20) )
r_primavera_norte = ( (3, 21), (6, 20) )
r_verano_norte    = ( (6, 21), (9, 20) )
r_otono_norte     = ( (9, 21), (12, 20) )

if hem == "N":
    if en_rango(fecha, *r_invierno_norte):
        estacion = "Invierno"
    elif en_rango(fecha, *r_primavera_norte):
        estacion = "Primavera"
    elif en_rango(fecha, *r_verano_norte):
        estacion = "Verano"
    elif en_rango(fecha, *r_otono_norte):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hem == "S":
    # Sur es el espejo del norte según la tabla
    if en_rango(fecha, *r_invierno_norte):
        estacion = "Verano"
    elif en_rango(fecha, *r_primavera_norte):
        estacion = "Otoño"
    elif en_rango(fecha, *r_verano_norte):
        estacion = "Invierno"
    elif en_rango(fecha, *r_otono_norte):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido (usá N o S)."

print("Estación:", estacion)



