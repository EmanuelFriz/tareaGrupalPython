# tareaGrupalPython
Tareas desarrolladas en Clases de Bootcamp de desarrollo Full Stack de Python

TAREAS A REALIZAR

El presente desarrollo contempla aplicar todos los conocimiento adquiridos en el modulo 3 (Fundamentos de Python), debe apegarse estrictamente a los siguiente lineamientos.

●	La actividad sera realizada en pareja
●	La defensa del proyecto se hara individualmente en base a quien sera escojido por el profesor para que explique cada parte del desarrollo
●	Se entrega un el archivo central.py, que corresponde al archivo principal del programa, en el que deberás cargar la información entregada y completar las consultas que se solicitan. Este es el único archivo que debes modificar.
●	Se entrega el archivo movies.csv: Este archivo contiene información sobre diversas películas. Cada línea contiene los datos de una película separados por comas (“”), de la siguiente forma:
titulo,popularidad,voto_promedio,cantidad_votos,generos Donde los significados de cada atributo son los siguientes:
titulo: Es el nombre de la película.
popularidad: Número que indica la popularidad de la película. Entre más alto, más popular es actualmente la película.
voto_promedio: Es un número que indica el puntaje promedio de la película.
cantidad_votos: Es un número que indica la cantidad de votos que ha recibido la película.
generos: Representa un listado de géneros a los que pertenece una película, separados por un punto y coma (“;”). Por ejemplo, si en la columna “generos” de una película se encuentra el texto “Adventure;Action;Science Fiction”, significa que la película es categorizada bajo esos tres géneros.

El código que se entrega contiene implementado el flujo del menú principal, el cual recibe un input indicando la consulta a realizar, abre el archivo de películas y almacena cada línea de este en una lista y en base a esto ejecuta la función correspondiente para finalmente mostrar el resultado en consola. Para asegurar su funcionamiento, debes realizar las siguientes tareas:


Cargar los datos.

La primera parte del trabajo consiste en guardar los datos del archivo de películas en diversas estructuras.
Como se indicó anteriormente, el código entregado ya se encarga de abrir el archivo de películas y generar una lista en donde cada elemento es una línea del archivo, por lo que debes trabajar en base a esta lista.

Para esto, debes completar la función cargar_datos(lineas_archivo) que se encuentra en el archivo central.py, la cual tiene como argumento la lista de películas extraídas del archivo, es decir, cada línea del archivo en formato string, y en donde debes crear las siguientes estructuras:

  generos_peliculas: Es una lista que debe almacenar todos los géneros distintos de películas que existen en el archivo. Como una película puede tener más de un género, debes ingresar los géneros de cada película por separado a la lista. Además, como las películas pueden compartir géneros, debes verificar que cada género sea guardado en la lista una sola vez.
  peliculas_por_genero: Es una lista de tuplas con el formato (genero, [peliculas]), en donde el primer elemento corresponde al nombre de un género de película, y el segundo elemento es una lista de películas que poseen dicho género. Por cada género distinto de película, debería haber exactamente una tupla. Sin embargo, como una película puede tener más de un género, puede ocurrir que una película este en más de una tupla.
  info_peliculas: Es una lista de tuplas con el formato (titulo,popularidad,voto_promedio,cantidad_votos,[generos]), en donde el último elemento debe ser una lista de los géneros de la película. Por cada película, debería haber exactamente una tupla que la represente.
 
Finalmente, una vez que creadas las estructuras, debes hacer que la función las retorne como una tupla, en donde los elementos deben poseer el siguiente orden: generos_peliculas, peliculas_por_genero, info_peliculas.

Completar las consultas.

La segunda parte del trabajo consiste en completar las consultas que se utilizarán para obtener información sobre las películas. Para esto, debes completar las siguientes funciones que se encuentran en el archivo central.py:

  obtener_puntaje_y_votos(nombre_pelicula): Esta función recibe un string, que corresponde al nombre de una película y debe retornar una tupla, donde el primer elemento debe ser el puntaje promedio de la película y el segundo elemento debe ser la cantidad de votos que tiene.
  filtrar_y_ordenar(genero_pelicula): Esta función recibe un string que corresponde a un género de película. Debes filtrar todas las películas que sean de este género y retornar sus nombres en una lista. Además, esta lista debe estar ordenada según orden alfabético inverso (es decir, películas con z primero y al final películas con a).
  obtener_estadisticas(genero_pelicula, criterio): Esta función recibe un string que corresponde a un género de película. Debes analizar las películas que sean de este género y obtener el máximo,
mínimo y promedio de los valores dados por criterio (que puede ser “popularidad”, “voto promedio”,
“cantidad votos”). Esto debe ser entregado en formato de lista con el formato [max, min, promedio], en el orden mostrado.

Para procesar la información requerida en las funciones, debes utilizar las estructuras de datos creadas en el apartado anterior que consideres pertinentes. No es necesario que las utilices todas, pero sí debes usar al menos una.

Nota: Para que puedas realizar tu evaluación, deberás usar un método para strings de Python llamado split(), el cual permite separar elementos de un string y almacenarlos en una lista.

