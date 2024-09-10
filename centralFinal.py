# Parte 1: Cargar los datos

def cargar_datos(lineas_archivo):
    generos_peliculas = set()  # se crea un conjunto para almacenar los generos sin repetir
    peliculas_por_genero = {}  # Diccionario donde la clave es el "género" y el valor es una lista de películas
    info_peliculas = []  # Lista de tuplas con la información de las películas

    for linea in lineas_archivo:
        # Separamos los elementos de la línea en una lista
        elementos = linea.strip().split(",")
        
        #los primeros elementos son fijos
        titulo = elementos[0]
        popularidad = float(elementos[1])
        voto_promedio = float(elementos[2])
        cantidad_votos = int(elementos[3])
        
        generos = elementos[4].split(";")  # Dividimos los géneros por ";" para obtener los generos que estan en la pelicula

        # Agregar géneros a la lista de géneros únicos
        for genero in generos:
            generos_peliculas.add(genero)

            # Añadir la película a la lista de ese género
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            peliculas_por_genero[genero].append(titulo)

        # Crear la tupla de información de la película y añadirla a la lista
        info_peliculas.append((titulo, popularidad, voto_promedio, cantidad_votos, generos))

    # Convertimos el set a una lista antes de retornarlo
    generos_peliculas = list(generos_peliculas)

    # Convertimos peliculas_por_genero a una lista de tuplas
    peliculas_por_genero = [(genero, peliculas) for genero, peliculas in peliculas_por_genero.items()]

    return generos_peliculas, peliculas_por_genero, info_peliculas

# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    _, _, info_peliculas = cargar_datos(lineas_archivo)
    for pelicula in info_peliculas:
        if pelicula[0] == nombre_pelicula:
            return (pelicula[2], pelicula[3])  # Retornamos voto_promedio y cantidad_votos
    return None  # Si no se encuentra la película
      
def filtrar_y_ordenar(genero_pelicula):
    lineas_archivo = leer_archivo()
    _, peliculas_por_genero, _ = cargar_datos(lineas_archivo)
    for genero, peliculas in peliculas_por_genero:
        if genero == genero_pelicula:
            return sorted(peliculas, reverse=True)  # Orden alfabético inverso
    return []  # Si no se encuentra el género
    

def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    _, _, info_peliculas = cargar_datos(lineas_archivo)
    valores = []
    for pelicula in info_peliculas:
        titulo, popularidad, voto_promedio, cantidad_votos, generos = pelicula
        if genero_pelicula in generos:
            if criterio == "popularidad":
                valores.append(popularidad)
            elif criterio == "voto promedio":
                valores.append(voto_promedio)
            elif criterio == "cantidad votos":
                valores.append(cantidad_votos)

    if valores:
        maximo = max(valores)
        minimo = min(valores)
        promedio = sum(valores) / len(valores)
        return [maximo, minimo, promedio]
    return []  # Si no se encuentran películas del género o criterio inválido


# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion

#funcion que retorna una lista de las peliculas y su informacion
def leer_archivo():
    lineas_peliculas = [] #Litsa de las lineas de la peliculas
    with open("movies.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip()) #Lee una linea a la vez y la agrega a lineas pelicula, borrando los espacios antes y despues de la cadena con .strip
            
    
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(lineas_archivo)
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas)

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                resultado = obtener_puntaje_y_votos(nombre_pelicula)
                if resultado is not None:
                    ptje, votos = resultado
                    print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                    print(f"    - Puntaje promedio: {ptje}")
                    print(f"    - Votos: {votos}")
                else:
                    print(f"\nLa película '{nombre_pelicula}' no fue encontrada.")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
