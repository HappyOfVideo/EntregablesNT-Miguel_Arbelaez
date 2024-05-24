usuarios = {}
productos = {}
ventas = {}

#Registro de usuarios, productos y ventas
clientes = {}
productos = {}
ventas = {}

# Función para agregar
def agregar_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    clave = input("Ingrese la clave del cliente: ")
    clientes[id_cliente] = {"nombre": nombre, "correo": correo, "clave": clave}
    print("Cliente agregado con éxito!")

def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    estado = "Disponible"
    productos[id_producto] = {"nombre": nombre, "precio": precio, "cantidad": cantidad, "estado": estado}
    print("Producto agregado con éxito!")

def agregar_venta(cliente_id, producto_id, cantidad):
    if cliente_id in clientes and producto_id in productos:
        if productos[producto_id]["estado"] == "Disponible" and productos[producto_id]["cantidad"] >= cantidad:
            ventas[len(ventas)] = {"cliente": cliente_id, "producto": producto_id, "cantidad": cantidad}
            productos[producto_id]["cantidad"] -= cantidad
            print("Venta agregada con éxito!")
        else:
            print("No hay suficiente stock del producto")
    else:
        print("Cliente o producto no encontrado")

# Función para consultar
def consultar_clientes():
    for key, value in clientes.items():
        print(f"ID: {key}, Nombre: {value['nombre']}, Correo: {value['correo']}")

def consultar_productos():
    for key, value in productos.items():
        print(f"ID: {key}, Nombre: {value['nombre']}, Precio: {value['precio']}, Cantidad: {value['cantidad']}, Estado: {value['estado']}")

def consultar_ventas():
    for key, value in ventas.items():
        print(f"Venta {key}: Cliente {value['cliente']}, Producto {value['producto']}, Cantidad {value['cantidad']}")

# Función para modificar 
def modificar_cliente(id_cliente):
    if id_cliente in clientes:
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        correo = input("Ingrese el nuevo correo del cliente: ")
        clave = input("Ingrese la nueva clave del cliente: ")
        clientes[id_cliente]["nombre"] = nombre
        clientes[id_cliente]["correo"] = correo
        clientes[id_cliente]["clave"] = clave
        print("Cliente modificado con éxito!")
    else:
        print("Cliente no encontrado")

def modificar_producto(id_producto):
    if id_producto in productos:
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        estado = input("Ingrese el nuevo estado del producto (Disponible o No disponible): ")
        productos[id_producto]["nombre"] = nombre
        productos[id_producto]["precio"] = precio
        productos[id_producto]["cantidad"] = cantidad
        productos[id_producto]["estado"] = estado
        print("Producto modificado con éxito!")
    else:
        print("Producto no encontrado")

# Función para eliminar
def eliminar_cliente(id_cliente):
    if id_cliente in clientes:
        del clientes[id_cliente]
        print("Cliente eliminado con éxito!")
    else:
        print("Cliente no encontrado")

def eliminar_producto(id_producto):
    if id_producto in productos:
        del productos[id_producto]
        print("Producto eliminado con éxito!")
    else:
        print("Producto no encontrado")

def eliminar_venta(id_venta):
    if id_venta in ventas:
        del ventas[id_venta]
        print("Venta eliminada con éxito!")
    else:
        print("Venta no encontrada")

#Iniciar sesión
def iniciar_sesion():
    correo_o_id = input("Ingrese su correo o ID: ")
    clave = input("Ingrese su clave: ")
    for key, value in clientes.items():
        if value["correo"] == correo_o_id or key == correo_o_id:
            if value["clave"] == clave:
                print("Inicio de sesión exitoso!")
                return key
            else:
                print("Clave incorrecta")
                return None
    print("Correo o ID no encontrado")
    return None

#Menús
def menu_inicio():
    while True:
        print("Menú de inicio")
        print("1. Iniciar sesión")
        print("2. Agregar nuevo cliente")
        print("3. Consultar clientes")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            cliente_id = iniciar_sesion()
            if cliente_id:
                menu_compra(cliente_id)
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            consultar_clientes()
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def menu_compra(cliente_id):
    while True:
        print("Menú de opciones de compra")
        print("1. Consultar productos")
        print("2. Agregar nuevo producto")
        print("3. Comprar producto")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            consultar_productos()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            producto_id = input("Ingrese el ID del producto que desea comprar: ")
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            agregar_venta(cliente_id, producto_id, cantidad)
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

menu_inicio()