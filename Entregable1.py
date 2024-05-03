id = input("Ingrese el id: ")
Nombre = input("Ingrese el nombre del producto: ")
Descripcion = input("Ingrese la descripción de este: ")
Costo = int(input("Ingrese el costo: "))
pv = Costo/(1 - 0.3)
Precio = pv
Cantidad = int(input("Ingrese la cantidad de producto: "))
Estado = input("Ingrese de este (True or False): ")

print(f"id: {id}\n Producto: {Nombre}\n Cantidad: {Cantidad}\n Descripción: {Descripcion}\n Precio total: {pv}\n Estado: {Estado}")