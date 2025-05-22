# Listas globales
lista_nombres = []
lista_codigos = []
lista_especies = []
lista_razas = []
lista_edades = []
lista_sexos = []
lista_proximas_citas = []
lista_ultimas_citas = []
lista_vacunas = []
lista_enfermedades = []
lista_historial_citas = []


def mostrar_lista():
    print("\nLista actual:")
    if len(lista_codigos) == 0:
        print("La lista está vacía.")
    else:
        for i in range(len(lista_codigos)):
            print(f"{i+1}. Código: {lista_codigos[i]} | Nombre: {lista_nombres[i]}")
    print()


def agregar_animal():
    codigo = input("Ingresá el código del nuevo paciente: ")
    lista_codigos.append(codigo)

    nombre = input("Ingresá el nombre del nuevo paciente: ")
    lista_nombres.append(nombre)

    especie = input("Ingresá la especie del paciente (ej: perro, gato): ")
    lista_especies.append(especie)

    raza = input("Ingresá la raza del paciente: ")
    lista_razas.append(raza)

    edad = input("Ingresá la edad del paciente: ")
    lista_edades.append(edad)

    sexo = input("Ingresá el sexo del paciente (M/H): ")
    lista_sexos.append(sexo)

    proxima_cita = input("Ingresá la fecha de la próxima cita (dd/mm/aaaa): ")
    lista_proximas_citas.append(proxima_cita)

    ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
    lista_ultimas_citas.append(ultima_cita)

    vacunas = input("Ingresá las vacunas aplicadas (separadas por comas): ")
    lista_vacunas.append(vacunas.split(','))

    enfermedades = input("Ingresá las enfermedades conocidas (separadas por comas): ")
    lista_enfermedades.append(enfermedades.split(','))

    print(f"{nombre} fue agregado/a exitosamente a la base de datos.\n")


def buscar_animal():
    criterio = input("Buscar por código o nombre: ").lower()

    encontrado = False
    for i in range(len(lista_codigos)):
        if criterio == lista_codigos[i].lower() or criterio == lista_nombres[i].lower():
            print(f"\nPaciente encontrado ({i+1}):")
            print("Código:", lista_codigos[i])
            print("Nombre:", lista_nombres[i])
            print("Especie:", lista_especies[i])
            print("Raza:", lista_razas[i])
            print("Edad:", lista_edades[i])
            print("Sexo:", lista_sexos[i])
            print("Próxima cita:", lista_proximas_citas[i])
            print("Última cita:", lista_ultimas_citas[i])
            print("Vacunas:", ', '.join(lista_vacunas[i]))
            print("Enfermedades:", ', '.join(lista_enfermedades[i]))
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún paciente con ese nombre o código.")


def menu():
    opcion = 0
    while opcion != -1:
        print("\n--- MENÚ ---")
        print("1. Mostrar lista")
        print("2. Agregar paciente")
        print("3. Buscar paciente")
        print("-1. Salir")

        try:
            opcion = int(input("Elegí una opción: "))
        except ValueError:
            print("Ingresá un número válido.")
            continue

        if opcion == 1:
            mostrar_lista()
        elif opcion == 2:
            agregar_animal()
        elif opcion == 3:
            buscar_animal()
        elif opcion == -1:
            print("¡Chau!")
        else:
            print("Opción inválida.")

menu()