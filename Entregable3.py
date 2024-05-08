contador = 0

usuarios = []
usuario = []

while len(usuarios) < 5:

    nombre = input("Agregue un nombre: ")
    usuario.append(nombre)

    apellido = input("Agregue un apellido: ")
    usuario.append(apellido)

    telefono = input("Agregue un telefono: ")
    usuario.append(telefono)

    correo = input("Agregue un correo: ")
    usuario.append(correo)

    clave = input("Agregue una clave: ")
    usuario.append(clave)

    usuarios.append(usuario)
    

for i in usuarios[0]:
    print(i, "\n")
    
