"""
- registrar alumnos.
- generar fichas de matricula.
- mostrar la lista de todos los matriculados
- filtar matriculados por programa de estudio
"""
lista_alumnos=[]
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
