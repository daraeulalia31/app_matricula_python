"""
- registrar alumnos.
- generar fichas de matricula.
- mostrar la lista de todos los matriculados
- filtar matriculados por programa de estudio
"""
lista_alumnos=[]

def mensaje_menu():
    menu_opciones=input("""
        ````````Bienvenidos al sistema`````````
           `````Registra tu alumno```
1. Escribe (s) si deseas agregar un nuevo alumno
2. Escribe (n) si deseas salir del sistema
Escribe la accion que deseas realizar: """)
    return menu_opciones

def ingresar_datos_alumnos():
 id=len(lista_alumnos)+1
 cui=int(input("ingrese el numero de su dni:"))
 nombre=input("ingrese el nombre de su alumno:")
 apellido=input("ingrese el apellido de su alumno:")
 numero_celular=int(input("ingrese su numero de celular:"))
 programa_estudio=input("ingrese el programa de estudio:")
 ciclo_academico=input("ingrese su ciclo academico:")
 email=input("ingrese su correo electronico:")

 guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno{
        "id":id,
        "cui":cui,
        "nombre":nombre,
        "apellido":apellido,
        "numero_celular":numero_celular,
        "programa_estudio":programa_estudio,
        "ciclo_academico":ciclo_academico,
        "email":email,
    }

    lista_alumnos.append(alumno)


while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower() == "n":
        print("saliendo del sistema")
        break
    elif menu_opciones.lower() == "s":
       ingresar_datos_alumnos()
    else:
        print("opcion erronea")


print(lista_alumnos)


    
#inicio de problema
#necesito poder agregar mas alumnos sin necesidad de crear tantas varias variables
#posible solucion cre o encerrar el codigo en un ciclo while

nombre=input("Ingrese el nombre del alumno: ")
apellido=input("ingrese el apellido del alumno: ")
nombre2=input("Ingrese el nombre del alumno: ")
apellido2=input("ingrese el apellido del alumno: ")
lista_alumnos.append(nombre)
lista_alumnos.append(apellido)
lista_alumnos.append(nombre2)
lista_alumnos.append(apellido2)
alumno={
    "nombre":nombre,
    "apellido":apellido
}
alumno2={
    "nombre":nombre2,
    "apellido":apellido2
}
lista_alumnos.append(alumno)
lista_alumnos.append(alumno2)
#fin del problema

#deseo mostrar un menu con las opciones de agregar un nuevo alumno y salir del programa

print(lista_alumnos)
