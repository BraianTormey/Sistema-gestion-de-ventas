import os
from datetime import datetime

# ===================== CLASES =====================

class Cliente:
    """Representa un cliente."""
    def __init__(self, id_cliente, nombre="", apellido="", direccion="", localidad="", codigo_postal="", dni=""):
        self.id = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.dni = dni

class Producto:
    """Representa un producto."""
    def __init__(self, id_producto, codigo="", descripcion="", stock=0, precio=0.0):
        self.id = id_producto
        self.codigo = codigo
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio

class Venta:
    """Representa una venta."""
    def __init__(self, id_venta, comprobante, fecha, importe_total, codigo_cliente, codigo_producto, cantidad, nombre, apellido):
        self.id = id_venta
        self.comprobante = comprobante
        self.fecha = fecha
        self.importe_total = importe_total
        self.codigo_cliente = codigo_cliente
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.nombre = nombre
        self.apellido = apellido

# ===================== LISTAS =====================

clientes = []
productos = []
ventas = []

# ===================== FUNCIONES GENERALES =====================

def clear_console():
    """Limpia la consola."""
    os.system("cls" if os.name == "nt" else "clear")

def display_formatted_table(title, data, headers):
    """Muestra una tabla formateada."""
    if not data:
        print("\nNo hay datos para mostrar.")
        return

    # Calcular anchos de columnas
    anchos = []
    for i in range(len(headers)):
        max_ancho = len(headers[i])
        for fila in data:
            if i < len(fila):
                max_ancho = max(max_ancho, len(str(fila[i])))
        anchos.append(max_ancho + 2)

    # Crear separador
    separador = "+" + "+".join("-" * ancho for ancho in anchos) + "+"

    # Imprimir tabla
    print("+" + "-" * (len(separador) - 2) + "+")
    if title:
        print(f"| {title.center(len(separador) - 4)} |")
    print(separador)

    # Encabezados
    encabezado = "|"
    for i, enc in enumerate(headers):
        encabezado += f" {enc.center(anchos[i] - 2)} |"
    print(encabezado)
    print(separador)

    # Datos
    for fila in data:
        linea = "|"
        for i, celda in enumerate(fila):
            linea += f" {str(celda).center(anchos[i] - 2)} |"
        print(linea)
    print(separador)

# ===================== MENÚ CLIENTES =====================

def menu_clientes():
    """Menú de gestión de clientes."""
    for _ in range(1000): 
        clear_console()
        print("Menú de Clientes:")
        print("+-------------------+")
        print("| 1. Alta           |")
        print("|-------------------|")
        print("| 2. Modificación   |")
        print("|-------------------|")
        print("| 3. Consulta       |")
        print("|-------------------|")
        print("| 4. Baja           |")
        print("|-------------------|")
        print("| 5. Atrás          |")
        print("+-------------------+")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_cliente()
        elif opcion == "2":
            modificacion_cliente()
        elif opcion == "3":
            consulta_clientes()
        elif opcion == "4":
            eliminacion_cliente()
        elif opcion == "5":
            break
        else:
            print("\n*ERROR* Opción inválida, presiona Enter para volver a intentarlo.")

def alta_cliente():
    """Registra un nuevo cliente."""
    clear_console()
    print("+---------------+")
    print("|Alta de Cliente|")
    print("+---------------+")
    print()

    # Validación del ID
    while True:
        try:
            id_cliente = int(input("ID: "))
            if id_cliente <= 0:
                print("ERROR: El ID debe ser positivo.")
                continue
            if any(c.id == id_cliente for c in clientes):
                print("ERROR: Ya existe un cliente con ese ID.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    localidad = input("Localidad: ")
    
    # Validación del código postal
    while True:
        codigo_postal = input("Código Postal: ")
        if not codigo_postal.isdigit():
            print("ERROR: Código postal inválido. Debe ser solo números.")
            continue
        break

    # Validación del DNI
    while True:
        dni = input("DNI: ")
        if not dni.isdigit() or len(dni) not in (7, 8):
            print("ERROR: DNI inválido. Debe tener 7 u 8 dígitos numéricos.")
            continue
        break

    clientes.append(Cliente(id_cliente, nombre, apellido, direccion, localidad, codigo_postal, dni))
    print("\nCliente añadido exitosamente.")
    input("Presiona Enter para continuar...")

def modificacion_cliente():
    """Modifica un cliente existente."""
    clear_console()
    print("+-----------------------+")
    print("|Modificación de Cliente|")
    print("+-----------------------+")
    print()

    # Buscar cliente
    while True:
        try:
            id_cliente = int(input("ID del Cliente a modificar: "))
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            if not cliente:
                print("ERROR: Cliente no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    print(f"Modificando cliente: {cliente.nombre} {cliente.apellido}")
    print()

    nuevo_nombre = input("Nuevo Nombre: ")
    nuevo_apellido = input("Nuevo Apellido: ")
    nueva_direccion = input("Nueva Dirección: ")
    nueva_localidad = input("Nueva Localidad: ")
    
    # Validación del código postal
    while True:
        nuevo_codigo_postal = input("Nuevo Código Postal: ")
        if not nuevo_codigo_postal.isdigit():
            print("ERROR: Código postal inválido. Debe ser solo números.")
            continue
        break

    # Validación del DNI
    while True:
        nuevo_dni = input("Nuevo DNI: ")
        if not nuevo_dni.isdigit() or len(nuevo_dni) not in (7, 8):
            print("ERROR: DNI inválido. Debe tener 7 u 8 dígitos numéricos.")
            continue
        break

    # Asigno solo si todo es válido
    cliente.nombre = nuevo_nombre
    cliente.apellido = nuevo_apellido
    cliente.direccion = nueva_direccion
    cliente.localidad = nueva_localidad
    cliente.codigo_postal = nuevo_codigo_postal
    cliente.dni = nuevo_dni
    print("\nCliente modificado exitosamente.")
    input("Presiona Enter para continuar...")

def consulta_clientes():
    """Muestra todos los clientes."""
    clear_console()
    data = [[c.id, c.nombre, c.apellido, c.direccion, c.localidad, c.codigo_postal, c.dni]
            for c in clientes]
    if data:
        display_formatted_table("Consulta de Clientes", data,
                               ["ID", "Nombre", "Apellido", "Dirección", "Localidad", "Código Postal", "DNI"])
    else:
        print("No hay clientes registrados.")
    input("Presione una tecla para continuar.")

def eliminacion_cliente():
    """Elimina un cliente."""
    clear_console()
    print("+---------------+")
    print("|Baja de Cliente|")
    print("+---------------+")
    print()

    # Buscar cliente
    while True:
        try:
            id_cliente = int(input("ID del Cliente a eliminar: "))
            cliente = next((c for c in clientes if c.id == id_cliente), None)
            if not cliente:
                print("ERROR: Cliente no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    print(f"Cliente a eliminar: {cliente.nombre} {cliente.apellido}")
    confirmacion = input("¿Está seguro que desea eliminar este cliente? (s/n): ").lower()

    if confirmacion == 's':
        clientes.remove(cliente)
        print("\nCliente eliminado exitosamente.")
        input("Presiona Enter para continuar...")
    else:
        print("\nEliminación cancelada.")
        input("Presiona Enter para continuar...")

# ===================== MENÚ PRODUCTOS =====================

def menu_productos():
    """Menú de gestión de productos."""
    while True:
        clear_console()
        print("Menú de Productos:")
        print("+-------------------+")
        print("| 1. Alta           |")
        print("|-------------------|")
        print("| 2. Modificación   |")
        print("|-------------------|")
        print("| 3. Consulta       |")
        print("|-------------------|")
        print("| 4. Baja           |")
        print("|-------------------|")
        print("| 5. Atrás          |")
        print("+-------------------+")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_producto()
        elif opcion == "2":
            modificacion_producto()
        elif opcion == "3":
            consulta_productos()
        elif opcion == "4":
            eliminacion_producto()
        elif opcion == "5":
            break
        else:
            print("\n*ERROR* Opción inválida, presiona Enter para volver a intentarlo.")
            input()

def alta_producto():
    """Registra un nuevo producto."""
    clear_console()
    print("+----------------+")
    print("|Alta de Producto|")
    print("+----------------+")
    print()

    # Validación del ID
    while True:
        try:
            id_producto = int(input("ID: "))
            if id_producto <= 0:
                print("ERROR: El ID debe ser positivo.")
                continue
            if any(p.id == id_producto for p in productos):
                print("ERROR: Ya existe un producto con ese ID.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    codigo = input("Código: ")
    descripcion = input("Descripción: ")

    # Validación del stock
    while True:
        try:
            stock = int(input("Stock: "))
            if stock < 0:
                print("ERROR: El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("ERROR: Stock inválido. Debe ser un número entero.")

    # Validación del precio
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("ERROR: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("ERROR: Precio inválido. Debe ser un número decimal.")

    productos.append(Producto(id_producto, codigo, descripcion, stock, precio))
    print("\nProducto añadido exitosamente.")
    input("Presiona Enter para continuar...")

def modificacion_producto():
    """Modifica un producto existente."""
    clear_console()
    print("+------------------------+")
    print("|Modificación de Producto|")
    print("+------------------------+")
    print()

    # Buscar producto
    while True:
        try:
            id_producto = int(input("ID del Producto a modificar: "))
            producto = next((p for p in productos if p.id == id_producto), None)
            if not producto:
                print("ERROR: Producto no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    print(f"Modificando producto: {producto.descripcion}")
    print()

    nuevo_codigo = input("Nuevo Código: ")
    nueva_descripcion = input("Nueva Descripción: ")

    # Validación del stock
    while True:
        try:
            nuevo_stock = int(input("Nuevo Stock: "))
            if nuevo_stock < 0:
                print("ERROR: El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("ERROR: Stock inválido. Debe ser un número entero.")

    # Validación del precio
    while True:
        try:
            nuevo_precio = float(input("Nuevo Precio: "))
            if nuevo_precio < 0:
                print("ERROR: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("ERROR: Precio inválido. Debe ser un número decimal.")

    # Asigno solo si todo es válido
    producto.codigo = nuevo_codigo
    producto.descripcion = nueva_descripcion
    producto.stock = nuevo_stock
    producto.precio = nuevo_precio
    print("\nProducto modificado exitosamente.")
    input("Presiona Enter para continuar...")

def consulta_productos():
    """Muestra todos los productos."""
    clear_console()
    data = [[p.id, p.codigo, p.descripcion, p.stock, f"{p.precio:.2f}"]
            for p in productos]
    if data:
        display_formatted_table("Consulta de Productos", data,
                               ["ID", "Código", "Descripción", "Stock", "Precio"])
    else:
        print("No hay productos registrados.")
    input("Presione una tecla para continuar.")

def eliminacion_producto():
    """Elimina un producto."""
    clear_console()
    print("+----------------+")
    print("|Baja de Producto|")
    print("+----------------+")
    print()

    # Buscar producto
    while True:
        try:
            id_producto = int(input("ID del Producto a eliminar: "))
            producto = next((p for p in productos if p.id == id_producto), None)
            if not producto:
                print("ERROR: Producto no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    print(f"Producto a eliminar: {producto.descripcion}")
    confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()

    if confirmacion == 's':
        productos.remove(producto)
        print("\nProducto eliminado exitosamente.")
        input("Presiona Enter para continuar...")
    else:
        print("\nEliminación cancelada.")
        input("Presiona Enter para continuar...")

# ===================== MENÚ VENTAS =====================

def menu_ventas():
    """Menú de gestión de ventas."""
    while True:
        clear_console()
        print("Menú de Ventas:")
        print("+-------------------+")
        print("| 1. Alta           |")
        print("|-------------------|")
        print("| 2. Modificación   |")
        print("|-------------------|")
        print("| 3. Consulta       |")
        print("|-------------------|")
        print("| 4. Atrás          |")
        print("+-------------------+")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            modificacion_venta()
        elif opcion == "3":
            consulta_ventas()
        elif opcion == "4":
            break
        else:
            print("\n*ERROR* Opción inválida, presiona Enter para volver a intentarlo.")
            input()

def registrar_venta():
    """Registra una nueva venta."""
    clear_console()
    print("+-------------+")
    print("|Alta de Venta|")
    print("+-------------+")
    print()

    # Validación del ID de venta
    while True:
        try:
            id_venta = int(input("ID Venta: "))
            if id_venta <= 0:
                print("ERROR: El ID debe ser positivo.")
                continue
            if any(v.id == id_venta for v in ventas):
                print("ERROR: Ya existe una venta con ese ID.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    comprobante = input("Comprobante: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Validación del cliente
    while True:
        try:
            codigo_cliente = int(input("ID Cliente: "))
            cliente = next((c for c in clientes if c.id == codigo_cliente), None)
            if not cliente:
                print("ERROR: Cliente no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID de cliente inválido. Debe ser un número entero.")

    # Validación del producto
    while True:
        try:
            codigo_producto = int(input("ID Producto: "))
            producto = next((p for p in productos if p.id == codigo_producto), None)
            if not producto:
                print("ERROR: Producto no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID de producto inválido. Debe ser un número entero.")

    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("ERROR: La cantidad debe ser mayor a cero.")
                continue
            if producto.stock < cantidad:
                print(f"ERROR: Stock insuficiente. Disponible: {producto.stock}")
                continue
            break
        except ValueError:
            print("ERROR: Cantidad inválida. Debe ser un número entero.")

    importe_total = producto.precio * cantidad
    producto.stock -= cantidad
    ventas.append(Venta(id_venta, comprobante, fecha, importe_total,
                       codigo_cliente, codigo_producto, cantidad,
                       cliente.nombre, cliente.apellido))
    print(f"\nVenta registrada exitosamente. Importe total: ${importe_total:.2f}.")
    input("Presiona Enter para continuar...")

def modificacion_venta():
    """Modifica una venta existente."""
    clear_console()
    print("+---------------------+")
    print("|Modificación de Venta|")
    print("+---------------------+")
    print()

    # Buscar venta
    while True:
        try:
            id_venta = int(input("ID de la Venta a modificar: "))
            venta = next((v for v in ventas if v.id == id_venta), None)
            if not venta:
                print("ERROR: Venta no encontrada.")
                continue
            break
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número entero.")

    print(f"Modificando venta ID: {venta.id}")
    print()

    nuevo_comprobante = input("Nuevo Comprobante: ")

    # Validación del cliente
    while True:
        try:
            nuevo_codigo_cliente = int(input("Nuevo ID Cliente: "))
            cliente = next((c for c in clientes if c.id == nuevo_codigo_cliente), None)
            if not cliente:
                print("ERROR: Cliente no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID de cliente inválido. Debe ser un número entero.")

    # Validación del producto
    while True:
        try:
            nuevo_codigo_producto = int(input("Nuevo ID Producto: "))
            producto = next((p for p in productos if p.id == nuevo_codigo_producto), None)
            if not producto:
                print("ERROR: Producto no encontrado.")
                continue
            break
        except ValueError:
            print("ERROR: ID de producto inválido. Debe ser un número entero.")

    # Validación de la cantidad
    while True:
        try:
            nueva_cantidad = int(input("Nueva Cantidad: "))
            if nueva_cantidad <= 0:
                print("ERROR: La cantidad debe ser mayor a cero.")
                continue
            if producto.stock < nueva_cantidad:
                print(f"ERROR: Stock insuficiente. Disponible: {producto.stock}")
                continue
            break
        except ValueError:
            print("ERROR: Cantidad inválida. Debe ser un número entero.")

    # Actualizar venta
    venta.comprobante = nuevo_comprobante
    venta.codigo_cliente = nuevo_codigo_cliente
    venta.codigo_producto = nuevo_codigo_producto
    venta.cantidad = nueva_cantidad
    venta.importe_total = producto.precio * nueva_cantidad
    venta.nombre = cliente.nombre
    venta.apellido = cliente.apellido

    print("\nVenta modificada exitosamente.")
    input("Presiona Enter para continuar...")

def consulta_ventas():
    """Muestra todas las ventas."""
    clear_console()
    print("+------------------+")
    print("|Consulta de Ventas|")
    print("+------------------+")
    print()

    data = [[v.id, v.comprobante, v.fecha, f"{v.importe_total:.2f}",
             v.codigo_cliente, v.codigo_producto, v.cantidad, v.nombre, v.apellido]
            for v in ventas]
    if data:
        display_formatted_table("Consulta de Ventas", data,
                               ["ID", "Comprobante", "Fecha", "Importe Total",
                                "Cliente ID", "Producto ID", "Cantidad", "Nombre", "Apellido"])
    else:
        print("No hay ventas registradas.")
    input("Presiona Enter para continuar...")

# ===================== MENÚ PRINCIPAL =====================

def menu():
    """Muestra el menú principal."""
    clear_console()
    print("Menú Principal:")
    print("+----------------+")
    print("| 1. Clientes    |")
    print("|----------------|")
    print("| 2. Productos   |")
    print("|----------------|")
    print("| 3. Ventas      |")
    print("|----------------|")
    print("| 4. Salir       |")
    print("+----------------+")
    print()
    return input("Seleccione una opción: ")

def main():
    """Función principal del sistema."""
    while True:
        opcion = menu()
        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_ventas()
        elif opcion == "4":
            clear_console()
            print("Saliendo del sistema...")
            print("Presiona Enter para salir del sistema")
            input()
            break
        else:
            print("\n*ERROR* Opción inválida, presiona Enter para volver a intentarlo.")
            input()

if __name__ == "__main__":
    main()
