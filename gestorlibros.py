


import json
libros = []

def cargar_libros_desde_archivo(nombre_archivo='biblioteca.json'):
    global libros
    try:
        with open(nombre_archivo, 'r') as archivo:
            libros = json.load(archivo)
            print(f'Se cargaron {len(libros)} libros desde el archivo.')
    except FileNotFoundError:
        print('No se encontró el archivo. Se creará uno nuevo al guardar.')

def guardar_libros_en_archivo(nombre_archivo='biblioteca.json'):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(libros, archivo, indent=2)
        print(f'Se guardaron {len(libros)} libros en el archivo.')
        
    
def agregar_libro(titulo, autor, genero):
    libro = {'titulo': titulo, 'autor': autor, 'genero': genero, 'prestado': False, 'veces_prestado': 0}
    libros.append(libro)
    print(f'Libro "{titulo}" agregado con éxito.')

def buscar_por_titulo(titulo):
    resultados = [libro for libro in libros if libro['titulo'].lower() == titulo.lower()]
    mostrar_resultados(resultados, f'Libros con el título "{titulo}"')

def buscar_por_autor(autor):
    resultados = [libro for libro in libros if libro['autor'].lower() == autor.lower()]
    mostrar_resultados(resultados, f'Libros del autor {autor}')

def buscar_por_genero(genero):
    resultados = [libro for libro in libros if libro['genero'].lower() == genero.lower()]
    mostrar_resultados(resultados, f'Libros del género {genero}')

def buscar_por_estado_prestamo(estado):
    resultados = [libro for libro in libros if libro['prestado'] == estado]
    estado_str = 'prestados' if estado else 'disponibles'
    mostrar_resultados(resultados, f'Libros {estado_str}')

def mostrar_estadisticas():
    total_libros = len(libros)
    libros_prestados = sum(libro['prestado'] for libro in libros)
    libros_disponibles = total_libros - libros_prestados
    print(f'Estadísticas de la biblioteca:')
    print(f'Total de libros: {total_libros}')
    print(f'Libros prestados: {libros_prestados}')
    print(f'Libros disponibles: {libros_disponibles}')

def prestar_libro(titulo):
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            if not libro['prestado']:
                libro['prestado'] = True
                libro['veces_prestado'] += 1  # Incrementar el contador
                print(f'Libro "{titulo}" prestado con éxito.')
            else:
                print(f'Libro "{titulo}" ya está prestado.')
            return
    print(f'Libro "{titulo}" no encontrado.')

def devolver_libro(titulo):
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            if libro['prestado']:
                libro['prestado'] = False
                print(f'Libro "{titulo}" devuelto con éxito.')
            else:
                print(f'Libro "{titulo}" no está prestado.')
            return
    print(f'Libro "{titulo}" no encontrado.')

def mostrar_todos_los_libros():
    mostrar_resultados(libros, 'Todos los libros')

def mostrar_libros_prestados():
    prestados = [libro for libro in libros if libro['prestado']]
    mostrar_resultados(prestados, 'Libros prestados')

def mostrar_resultados(resultados, mensaje):
    if resultados:
        print(mensaje + ":")
        for libro in resultados:
            print(f'- {libro["titulo"]} ({libro["autor"]}) - {libro["genero"]}')
    else:
        print(f'No se encontraron resultados para {mensaje.lower()}.')

def modificar_libro(titulo):
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            print(f'Información actual del libro "{titulo}":')
            print(f'Título: {libro["titulo"]}')
            print(f'Autor: {libro["autor"]}')
            print(f'Género: {libro["genero"]}')
            nueva_autor = input('Ingrese el nuevo autor (presione Enter para dejar sin cambios): ')
            nueva_genero = input('Ingrese el nuevo género (presione Enter para dejar sin cambios): ')
            if nueva_autor:
                libro['autor'] = nueva_autor
            if nueva_genero:
                libro['genero'] = nueva_genero
            print(f'Información del libro "{titulo}" actualizada con éxito.')
            return
    print(f'Libro "{titulo}" no encontrado.')

def eliminar_libro(titulo):
    global libros
    libros = [libro for libro in libros if libro['titulo'].lower() != titulo.lower()]
    print(f'Libro "{titulo}" eliminado con éxito.')

def ordenar_libros_por_titulo():
    libros.sort(key=lambda x: x['titulo'].lower())
    print('Libros ordenados por título.')

def ordenar_libros_por_autor():
    libros.sort(key=lambda x: x['autor'].lower())
    print('Libros ordenados por autor.')

def ordenar_libros_por_genero():
    libros.sort(key=lambda x: x['genero'].lower())
    print('Libros ordenados por género.')

def mejores_libros_por_prestamo(top_n):
    libros_ordenados = sorted(libros, key=lambda x: x.get('veces_prestado', 0), reverse=True)
    mejores_libros = libros_ordenados[:top_n]
    
    if mejores_libros:
        print(f"Los {top_n} libros más prestados:")
        mostrar_resultados(mejores_libros, 'Mejores libros')
    else:
        print("No hay libros disponibles para mostrar.")

def mostrar_menu():
    print("\n----- Menú -----")
    print("1. Agregar libro")
    print("2. Buscar por título")
    print("3. Buscar por autor")
    print("4. Buscar por género")
    print("5. Buscar por estado de préstamo")
    print("6. Mostrar estadísticas")
    print("7. Prestar libro")
    print("8. Devolver libro")
    print("9. Mostrar todos los libros")
    print("10. Mostrar libros prestados")
    print("11. Modificar libro")
    print("12. Eliminar libro")
    print("13. Ordenar libros por título")
    print("14. Ordenar libros por autor")
    print("15. Ordenar libros por género")
    print("16. Mejores libros por número de veces prestado")
    print("17. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        genero = input("Ingrese el género del libro: ")
        agregar_libro(titulo, autor, genero)
    elif opcion == '2':
        titulo = input("Ingrese el título a buscar: ")
        buscar_por_titulo(titulo)
    elif opcion == '3':
        autor = input("Ingrese el autor a buscar: ")
        buscar_por_autor(autor)
    elif opcion == '4':
        genero = input("Ingrese el género a buscar: ")
        buscar_por_genero(genero)
    elif opcion == '5':
        estado = input("Ingrese el estado de préstamo (1 para prestado, 0 para disponible): ")
        buscar_por_estado_prestamo(bool(int(estado)))
    elif opcion == '6':
        mostrar_estadisticas()
    elif opcion == '7':
        titulo = input("Ingrese el título del libro a prestar: ")
        prestar_libro(titulo)
    elif opcion == '8':
        titulo = input("Ingrese el título del libro a devolver: ")
        devolver_libro(titulo)
    elif opcion == '9':
        mostrar_todos_los_libros()
    elif opcion == '10':
        mostrar_libros_prestados()
    elif opcion == '11':
        titulo = input("Ingrese el título del libro a modificar: ")
        modificar_libro(titulo)
    elif opcion == '12':
        titulo = input("Ingrese el título del libro a eliminar: ")
        eliminar_libro(titulo)
    elif opcion == '13':
        ordenar_libros_por_titulo()
    elif opcion == '14':
        ordenar_libros_por_autor()
    elif opcion == '15':
        ordenar_libros_por_genero()
    elif opcion == '16':
        top_n = int(input("Ingrese la cantidad de libros a mostrar: "))
        mejores_libros_por_prestamo(top_n)
    elif opcion == '17':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Intente nuevamente.")

# Ejemplo de uso del menú
while True:
    cargar_libros_desde_archivo()  # Cargar libros al inicio del programa
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada (1-17): ")
    ejecutar_opcion(opcion)
    guardar_libros_en_archivo()  # Guardar libros antes de salir del programa
    if opcion == '17':
        break
    

