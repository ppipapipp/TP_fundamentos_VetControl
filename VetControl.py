"""busqueda binaria para buscar un animal en la lista"""
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

from datetime import datetime
import random 

def mostrar_lista():
    print("\nLista actual:")
    if len(lista_codigos) == 0:
        print("La lista está vacía.")
    else:
        for i in range(len(lista_codigos)):
            print(i+1, " Código: ", lista_codigos[i] , " | Nombre: " , lista_nombres[i])
    print()

def buscar_duplicados(ingreso, lista_codigos):
    ingreso = ingreso.strip().lower()
    coincidencias = []
    for lista in lista_codigos:
        for item in lista:
            if item.lower() == ingreso:
                coincidencias.append(item)
    return coincidencias

def agregar_animal():
    while True:
        codigo = str(random.randint(1000, 9999))
        resultado = buscar_duplicados(codigo, lista_codigos)
        if codigo not in lista_codigos:
            lista_codigos.append(codigo)
            break
        elif resultado:
             codigo = str(random.randint(1000, 9999))
    
    print("El codigo del paciente es:", codigo)

    nombre = input("Ingresá el nombre del nuevo paciente: ")
    lista_nombres.append(nombre)

    especie = str(input("Ingresá la especie del paciente (ej: perro, gato): "))
    lista_especies.append(especie)

    raza = str(input("Ingresá la raza del paciente: "))
    lista_razas.append(raza)

    edad = int(input("Ingresá la edad del paciente: "))
    lista_edades.append(edad)
    if edad < 0 or edad>100:
        print("Ingrese una edad correcta")
        edad=int(input("Ingresá la edad del paciente: "))
        lista_edades.append(edad)

    sexo = input("Ingresá el sexo del paciente (M/H): ")
    lista_sexos.append(sexo.lower())
    if sexo != "m" and sexo != "h":
        print("Ingrese un sexo correcto")
        sexo = input("Ingresá el sexo del paciente (M/H): ")
        lista_sexos.append(sexo)

    ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
    while True:
        try:
            fecha_ultima= datetime.strptime(ultima_cita, "%d/%m/%Y")
            hoy=datetime.now()
            if fecha_ultima > hoy:
                print("La fecha de la ultima cita no puede estar en el futuro, intente de nuevo.")
                ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
            else:
                break
        except ValueError:
            print("Formato de fecha incorrecto. Ingresá la fecha en formato dd/mm/aaaa.")
            ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
    lista_ultimas_citas.append(ultima_cita)

    proxima_cita = input("Ingresá la fecha de la próxima cita (dd/mm/aaaa): ")
    while True:
        try:
            fecha_proxima= datetime.strptime(proxima_cita, "%d/%m/%Y")
            hoy=datetime.now()
            if fecha_proxima < hoy:
                print("La fecha de la proxima cita no puede estar en el pasado, intente de nuevo.")
                proxima_cita = input("Ingresá la fecha de la proxima cita (dd/mm/aaaa): ")
            if fecha_proxima < fecha_ultima:
                print("La fecha de la próxima cita no puede ser anterior a la última cita.")
                proxima_cita = input("Ingresá la fecha de la próxima cita (dd/mm/aaaa): ")
            else:
                break
        except ValueError:
            print("Formato de fecha incorrecto. Ingresá la fecha en formato dd/mm/aaaa.")
            proxima_cita = input("Ingresá la fecha de la próxima cita (dd/mm/aaaa): ")
    lista_proximas_citas.append(proxima_cita)

    vacunas = input("Ingresá las vacunas aplicadas (separadas por comas): ")
    lista_vacunas.append(vacunas)

    enfermedades = input("Ingresá las enfermedades conocidas (separadas por comas): ")
    lista_enfermedades.append(enfermedades)

    print(nombre, " fue agregado/a exitosamente a la base de datos.\n")


def buscar_animal():
    criterio = input("Buscar por código o nombre: ").lower()

    encontrado = False
    for i in range(len(lista_codigos)):
        if criterio == lista_codigos[i].lower() or criterio == lista_nombres[i].lower():
            print("\nPaciente encontrado ",  (i+1), ":")
            print("Código:", lista_codigos[i])
            print("Nombre:", lista_nombres[i])
            print("Especie:", lista_especies[i])
            print("Raza:", lista_razas[i])
            print("Edad:", lista_edades[i])
            print("Sexo:", lista_sexos[i])
            print("Próxima cita:", lista_proximas_citas[i])
            print("Última cita:", lista_ultimas_citas[i])
            print("Vacunas:", lista_vacunas[i])
            print("Enfermedades:", lista_enfermedades[i])
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