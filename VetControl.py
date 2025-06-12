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

""" imprime la lista actual"""
def mostrar_lista():
    print("\nLista actual:")
    if len(lista_codigos) == 0:
        print("La lista está vacía.")
    else:
        for i in range(len(lista_codigos)):
            print(i+1, " Código: ", lista_codigos[i] , " | Nombre: " , lista_nombres[i])
    print()

"""    verifica que no haya duplicidad en los códigos de los animales    """
def buscar_duplicados(ingreso, listas):
    ingreso = ingreso.strip().lower()
    coincidencias = []
    for lista in listas:
        for item in lista:
            if item.lower() == ingreso:
                coincidencias.append(item)
    return coincidencias

"""  Agregado de nuevo paciente"""
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
    """ Verificación"""
    while edad < 0 or edad>100:
        print("Ingrese una edad correcta")
        edad=int(input("Ingresá la edad del paciente: "))
    lista_edades.append(edad)

    sexo = input("Ingresá el sexo del paciente (M/H): ")
    lista_sexos.append(sexo.lower())
    """ Verificación"""
    while sexo != "m" and sexo != "h":
        print("Ingrese un sexo correcto")
        sexo = input("Ingresá el sexo del paciente (M/H): ")
    lista_sexos.append(sexo)

    ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
    while True:
        try:
            fecha_ultima= datetime.strptime(ultima_cita, "%d/%m/%Y")
            hoy=datetime.now()
            """ Verificación"""
            if fecha_ultima > hoy:
                print("La fecha de la ultima cita no puede estar en el futuro, intente de nuevo.")
                ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
            else:
                break
        except ValueError:
            print("Formato de fecha incorrecto. Ingresá la fecha en formato dd/mm/aaaa.")
            ultima_cita = input("Ingresá la fecha de la última cita (dd/mm/aaaa): ")
    lista_ultimas_citas.append(ultima_cita)


    while True:
        proxima_cita = input("Ingresá la fecha de la próxima cita (dd/mm/aaaa): ")
        try:
            fecha_proxima = datetime.strptime(proxima_cita, "%d/%m/%Y")
            hoy = datetime.now()
            """ Verificación"""
            if fecha_proxima < hoy:
                print("La fecha de la próxima cita no puede estar en el pasado. Intente de nuevo.")
                continue
            if fecha_proxima < fecha_ultima:
                print("La fecha de la próxima cita no puede ser anterior a la última cita.")
                continue

            lista_proximas_citas.append(proxima_cita)
            break

        except ValueError:
            print("Formato de fecha incorrecto. Ingresá la fecha en formato dd/mm/aaaa.")

    vacunas = input("Ingresá las vacunas aplicadas: ")
    lista_vacunas.append(vacunas)

    enfermedades = input("Ingresá las enfermedades conocidas: ")
    lista_enfermedades.append(enfermedades)

    print(nombre, " fue agregado/a exitosamente a la base de datos.\n")

""" modifica información de un paciente pre existente"""
def modificar_animal():
    codigo = input("Ingresá el código del paciente a modificar: ").strip()
    if codigo not in lista_codigos:
        print("No se encontró un paciente con ese código.")
        return

    indice = lista_codigos.index(codigo)

    print(f"\nPaciente actual:")
    print("1. Nombre:", lista_nombres[indice])
    print("2. Especie:", lista_especies[indice])
    print("3. Raza:", lista_razas[indice])
    print("4. Edad:", lista_edades[indice])
    print("5. Sexo:", lista_sexos[indice])
    print("6. Última cita:", lista_ultimas_citas[indice])
    print("7. Próxima cita:", lista_proximas_citas[indice])
    print("8. Vacunas:", lista_vacunas[indice])
    print("9. Enfermedades:", lista_enfermedades[indice])
    
    try:
        opcion = int(input("¿Qué campo querés modificar? (1-9): "))
    except ValueError:
        print("Opción inválida.")
        return

    if opcion == 1:
        lista_nombres[indice] = input("Nuevo nombre: ")
    elif opcion == 2:
        lista_especies[indice] = input("Nueva especie: ")
    elif opcion == 3:
        lista_razas[indice] = input("Nueva raza: ")
    elif opcion == 4:
        while True:
            try:
                nueva_edad = int(input("Nueva edad: "))
                if 0 <= nueva_edad <= 100:
                    lista_edades[indice] = nueva_edad
                    break
                else:
                    print("Edad fuera de rango.")
            except ValueError:
                print("Ingresá un número válido.")
    elif opcion == 5:
        sexo = input("Nuevo sexo (M/H): ").lower()
        while sexo not in ['m', 'h']:
            print("Sexo inválido.")
            sexo = input("Nuevo sexo (M/H): ").lower()
        lista_sexos[indice] = sexo
    elif opcion == 6:
        while True:
            nueva_fecha = input("Nueva fecha de última cita (dd/mm/aaaa): ")
            try:
                fecha = datetime.strptime(nueva_fecha, "%d/%m/%Y")
                if fecha <= datetime.now():
                    lista_ultimas_citas[indice] = nueva_fecha
                    break
                else:
                    print("No puede ser una fecha futura.")
            except ValueError:
                print("Formato inválido.")
    elif opcion == 7:
        while True:
            nueva_fecha = input("Nueva fecha de próxima cita (dd/mm/aaaa): ")
            try:
                fecha = datetime.strptime(nueva_fecha, "%d/%m/%Y")
                ultima = datetime.strptime(lista_ultimas_citas[indice], "%d/%m/%Y")
                if fecha >= datetime.now() and fecha >= ultima:
                    lista_proximas_citas[indice] = nueva_fecha
                    break
                else:
                    print("Debe ser una fecha futura y posterior a la última cita.")
            except ValueError:
                print("Formato inválido.")
    elif opcion == 8:
        lista_vacunas[indice] = input("Nuevas vacunas: ")
    elif opcion == 9:
        lista_enfermedades[indice] = input("Nuevas enfermedades: ")
    else:
        print("Opción fuera de rango.")
        return

    print("¡Paciente actualizado con éxito!")

""" búsqueda de paciente ya presente en la lista """
def buscar_animal():
    codigo = input("Buscar por código: ").lower()

    encontrado = False
    for i in range(len(lista_codigos)):
        if codigo == lista_codigos[i].lower():
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

suma_edades=0
cantidad_animales=0
def promedio_edad(lista_edades):
    suma_edades = sum(lista_edades)

    print(suma_edades)
    cantidad_animales = len(lista_edades)
    print(cantidad_animales)
    promedio_edad= suma_edades / cantidad_animales
    print (promedio_edad)

hembras=0
machos=0
total=0
porcentaje_h=0
porcentaje_m=0

""" promedio de edades y sexos """
def porcentaje_sexo(lista_sexos):
    hembras = lista_sexos.count("h")
    machos = lista_sexos.count("m")
    total = hembras + machos

    if total == 0:
        print("No hay datos para calcular porcentajes.")
        return

    porcentaje_h = (hembras * 100) / total
    porcentaje_m = (machos * 100) / total

    print("Porcentaje de hembras:", round(porcentaje_h, 2), "%")
    print("Porcentaje de machos:", round(porcentaje_m, 2), "%")



def ordenar_por_nombre():
    #ORDENAMIENTO POR BURBUJA
    n = len(lista_nombres)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_nombres[j].lower() > lista_nombres[j + 1].lower():
                # Intercambiar en todas las listas paralelas
                lista_nombres[j], lista_nombres[j + 1] = lista_nombres[j + 1], lista_nombres[j]
                lista_codigos[j], lista_codigos[j + 1] = lista_codigos[j + 1], lista_codigos[j]
                lista_especies[j], lista_especies[j + 1] = lista_especies[j + 1], lista_especies[j]
                lista_razas[j], lista_razas[j + 1] = lista_razas[j + 1], lista_razas[j]
                lista_edades[j], lista_edades[j + 1] = lista_edades[j + 1], lista_edades[j]
                lista_sexos[j], lista_sexos[j + 1] = lista_sexos[j + 1], lista_sexos[j]
                lista_proximas_citas[j], lista_proximas_citas[j + 1] = lista_proximas_citas[j + 1], lista_proximas_citas[j]
                lista_ultimas_citas[j], lista_ultimas_citas[j + 1] = lista_ultimas_citas[j + 1], lista_ultimas_citas[j]
                lista_vacunas[j], lista_vacunas[j + 1] = lista_vacunas[j + 1], lista_vacunas[j]
                lista_enfermedades[j], lista_enfermedades[j + 1] = lista_enfermedades[j + 1], lista_enfermedades[j]

    print("\nLista ordenada alfabéticamente por nombre:\n")
    mostrar_lista()





def menu():
    opcion = 0
    while opcion != -1:
        print("\n--- MENÚ ---")
        print("1. Mostrar lista")
        print("2. Agregar paciente")
        print("3. Buscar paciente")
        print("4. Promedio de edad")
        print("5. Porcentaje sexos")
        print("6. Ordenar alfabéticamente por nombre")
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
        elif opcion == 4:
            promedio_edad(lista_edades)
        elif opcion == 5:
            porcentaje_sexo(lista_sexos)
        elif opcion == 6:
            ordenar_por_nombre()
        elif opcion == -1:
            print("¡Chau!")
        else:
            print("Opción inválida.")

menu()