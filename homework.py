def registrar_alumno():
    """Registra un nuevo alumno y guarda los datos en un archivo."""
    nombre = input("Ingrese el nombre del alumno: ")
    programa = input("Ingrese el programa de estudio: ")
    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"{nombre},{programa}\n")
    print("Alumno registrado correctamente.")

def mostrar_lista_matriculados():
    """Muestra la lista de todos los alumnos matriculados."""
    try:
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                nombre, programa = linea.strip().split(",")
                print("-" * 20)
                print(f"Nombre: {nombre}")
                print(f"Programa: {programa}")
                print("-" * 20)
    except FileNotFoundError:
        print("No hay alumnos matriculados.")

while True:
    print("\nMenú:")
    print("1. Registrar alumno")
    print("2. Mostrar lista de matriculados")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_alumno()
    elif opcion == "2":
        mostrar_lista_matriculados()
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")