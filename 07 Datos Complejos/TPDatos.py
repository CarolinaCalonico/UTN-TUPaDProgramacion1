#1 Diccionario de frutas – agregar nuevos elementos
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#2 Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#3 Lista solo con las frutas (sin precios)
frutas = list(precios_frutas.keys())
print(frutas)

#4 Agenda telefónica (diccionario con búsqueda)
agenda = {}

for i in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número telefónico: ")
    agenda[nombre] = numero

consulta = input("Ingresá el nombre a consultar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("No se encontró ese contacto.")

#5 Frase – palabras únicas y cantidad de repeticiones
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()

# Palabras únicas
unicas = set(palabras)
print("Palabras únicas:", unicas)

# Cantidad de apariciones
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Frecuencia de palabras:", conteo)

#6 Notas de alumnos con tuplas y promedio
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Promedio: {promedio:.2f}")

#7 Sets de estudiantes (operaciones entre conjuntos)
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

#8 Diccionario de stock de productos
stock = {"Leche": 20, "Pan": 15, "Huevos": 30}

producto = input("Ingresá un producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá su stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

#9 Agenda con claves como tuplas (día, hora)
agenda = {
    ("Lunes", "10:00"): "Reunión de trabajo",
    ("Martes", "15:00"): "Clase de Python",
    ("Viernes", "20:00"): "Cine con amigos"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (HH:MM): ")

if (dia, hora) in agenda:
    print("Actividad:", agenda[(dia, hora)])
else:
    print("No hay actividad programada.")

#10 Diccionario invertido (capitales ↔ países)
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"
}

capitales = {capital: pais for pais, capital in paises.items()}

print(capitales)