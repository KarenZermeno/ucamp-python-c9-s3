
while True:
    try:
        nombre = str(input("Escriba su nombre: "))
        if nombre != "":
            break
        else: 
            print("Este campo no puede quedar vacio, intente de nuevo!")
    except ValueError:
        print("Error: ingrese un nombre valido.")

while True:
    try:
        apellido1 = str(input("Escriba su apellido paterno: "))
        if apellido1 != "":
            break
        else: 
            print("Este campo no puede quedar vacio, intente de nuevo!")
    except ValueError:
        print("Error: ingrese un apellido valido.")

while True:
    try:
        apellido2 = str(input("Escriba su apellido materno: "))
        if apellido2 != "":
            break
        else: 
            print("Este campo no puede quedar vacio, intente de nuevo!")
    except ValueError:
        print("Error: ingrese un apellido valido.")


while True:
    try:
        edad = int(input("Escriba su edad en años: "))
        break
    except ValueError:
        print("Este campo no puede quedar vacio o no fue un número válido, intente de nuevo!")

while True:
    try:
        peso = float(input("Escriba su peso en kilos: "))
        break
    except ValueError:
        print("Este campo no puede quedar vacio o no fue un número válido, intente de nuevo!")

while True:
    try:
        estatura = float(input("Escriba su estatura en metros: "))
        break
    except ValueError:
        print("Este campo no puede quedar vacio o no fue un número válido, intente de nuevo!")

    
imc = peso / estatura ** 2

print("Nombre: " + (nombre))
print("Apellido paterno: " + (apellido1))
print("Apellido materno: " + (apellido2))
print("Edad: " + str (edad))
print("Peso: " + str (peso))
print("Estatura: " + str (estatura))

print("Su Índice de Masa Corporal es: " + str (imc))