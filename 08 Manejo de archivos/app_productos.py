ARCHIVO = "productos.txt"


def inicializar_si_no_existe():
    """Crea el archivo con datos iniciales si no existe (modo 'x')."""
    try:
        with open(ARCHIVO, "x", encoding="utf-8") as f:
            f.write("Lapicera,120.5,30\nCuaderno,850.0,12\nRegla,200.0,50\n")
    except FileExistsError:
        # Si ya existe, no hace nada
        pass


def leer_productos():
    """Lee el archivo y devuelve una lista de diccionarios."""
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue  # condicional
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) != 3:
                    continue
                nombre, precio, cantidad = partes
                try:
                    prod = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad),
                    }
                    productos.append(prod)  # lista de dicts
                except ValueError:
                    # Si hay una línea mal formateada, la salto
                    continue
    except FileNotFoundError:
        productos = []
    return productos


def mostrar_productos(productos):
    """Muestra todos los productos en el formato pedido."""
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:  # repetitiva
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def pedir_producto():
    """Pide datos por teclado y devuelve un diccionario o None si se cancela."""
    print("\nIngrese un nuevo producto (enter en nombre para cancelar):")
    nombre = input("Nombre: ").strip()
    if not nombre:
        return None
    try:
        precio = float(input("Precio: ").strip().replace(",", "."))
        cantidad = int(input("Cantidad: ").strip())
        if precio < 0 or cantidad < 0:
            print("Precio y cantidad deben ser no negativos.")
            return None
        return {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    except ValueError:
        print("Datos inválidos.")
        return None


def buscar_por_nombre(productos, nombre):
    """Busca coincidencia exacta por nombre (insensible a mayúsculas)."""
    buscado = nombre.strip().lower()
    for p in productos:  # búsqueda lineal
        if p["nombre"].strip().lower() == buscado:
            return p
    return None


def guardar_todos(productos):
    """Sobrescribe el archivo con el contenido actualizado (modo 'w')."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)


def main():
    # 1) Crear archivo inicial si no existe
    inicializar_si_no_existe()

    # 2) Leer y mostrar
    productos = leer_productos()
    print("\n=== LISTA DE PRODUCTOS (ARCHIVO) ===")
    mostrar_productos(productos)

    # 3) Agregar uno o más productos desde teclado
    while True:
        nuevo = pedir_producto()
        if nuevo:
            productos.append(nuevo)
            seguir = input("¿Agregar otro? (s/n): ").strip().lower()
            if seguir != "s":
                break
        else:
            break

    # 4) Mostrar resultado final
    print("\n=== LISTA ACTUALIZADA ===")
    mostrar_productos(productos)

    # 5) Búsqueda opcional por nombre
    q = input("\nBuscar por nombre (enter para saltar): ").strip()
    if q:
        encontrado = buscar_por_nombre(productos, q)
        if encontrado:
            print("Encontrado ->", encontrado)
        else:
            print("No se encontró ese producto.")

    # 6) Guardar TODOS los productos (sobrescribir archivo)
    guardar_todos(productos)
    print("\nCambios guardados en productos.txt. ¡Listo!")


if __name__ == "__main__":
    main()

