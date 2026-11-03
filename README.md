Para el desarrollo del proyecto Análisis de datos TXT y CSV, se seleccionaron tres archivos: uno en formato TXT y dos en formato CSV. Estos archivos contienen información de diferentes áreas y permiten aplicar las funciones del programa, como el análisis estadístico, la búsqueda de patrones, la comparación de datos y la elaboración de gráficos.

Los datos fueron elegidos porque permiten trabajar con información real, tanto textual como numérica, y demostrar las diferentes herramientas de análisis implementadas en Python.

1. Archivo TXT: `llaneros.txt`

El llanero solitario: Bien tapa dura (1971) | Alcaná Libros
Origen: El archivo contiene fragmentos del libro Llaneros solitarios: Hackers, la guerrilla informática, escrito por Raquel Roberti y Fernando Bonsembiante, publicado en Argentina en 1995 por Espasa Calpe.

¿Qué representa? Es un texto sobre la historia de los hackers, sus actividades, la informática y algunos acontecimientos relacionados con la cultura tecnológica argentina.

Este archivo permite analizar la cantidad de palabras, caracteres y líneas, identificar las palabras más frecuentes y estudiar la distribución de la longitud de sus líneas. También permite aplicar la extracción de patrones de texto.

2. Archivo CSV: `Airports.csv`

Origen: La información coincide con registros de la base de datos de aeropuertos de OpenFlights, que utiliza información de OurAirports.

¿Qué representa? Contiene información de aeropuertos de diferentes países del mundo.

Entre los datos que incluye se encuentran:

- Nombre del aeropuerto.
- Ciudad y país donde se encuentra.
- Códigos IATA e ICAO.
- Latitud y longitud geográfica.
- Altitud y zona horaria.

Este archivo permite realizar comparaciones entre aeropuertos, consultar su ubicación geográfica y analizar diferentes variables numéricas y categóricas.

3. Archivo CSV: `Busiest-European-Airports-2021.csv`

Origen: Este conjunto de datos se encuentra publicado en el portal especializado en información aeronáutica Aviation File, dentro de su colección de datos sobre los aeropuertos más transitados de Europa.

aviationfile-Gateway to Aviation World

¿Qué representa? Presenta una clasificación de los aeropuertos europeos con mayor tráfico de pasajeros durante el año 2021.

Entre los datos que contiene se encuentran:

- Posición del aeropuerto en el ranking.
- Nombre del aeropuerto.
- Ciudad y país.
- Cantidad de pasajeros durante 2021 y 2020.
- Diferencia de pasajeros entre ambos años.
- Porcentaje de variación.

Este archivo permite comparar el tráfico de pasajeros entre aeropuertos, identificar cuáles tuvieron mayor movimiento y observar los cambios en la cantidad de viajeros entre 2020 y 2021.

Busiest-European-Airports-2021.csv

Basándonos en los graficos optenidos, podemos optener las siguientes 3 conclusiones:

 * Predominio del vocabulario técnico y común en textos de análisis:
   El análisis de frecuencia de palabras en formato de barras horizontales demuestra que los términos más repetidos combinan palabras funcionales con conceptos clave del dominio de estudio (como sistema, hacker e información), lo que permite identificar rápidamente los temas centrales sobre los cuales gira el contenido de los archivos de texto analizados.

 * Comportamiento y variabilidad en la longitud de las líneas:
   El histograma de distribución evidencia cómo se estructuran internamente los registros o líneas de texto, concentrando la mayor parte de las longitudes en rangos específicos (principalmente entre 50 y 100 caracteres), lo que refleja patrones de redacción regulares o estructuras estandarizadas en los archivos de bitácora (logs).

 * Limitaciones visuales al graficar variables discretas como continuas:
   Las visualizaciones de tipo lineal aplicadas a datos discretos o categóricos (como aeropuertos, códigos ICAO o zonas horarias frente a coordenadas) revelan que el uso de líneas continuas puede saturar o distorsionar la interpretación visual. Esto sugiere que, para este tipo de variables nominales o discretas, resultaría más efectivo utilizar gráficos de barras o diagramas de dispersión independientes en lugar de líneas de tendencia, evitando así sugerir una continuidad inexistente entre los elementos.
