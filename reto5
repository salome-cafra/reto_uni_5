import os
import csv
import re
import statistics
from collections import Counter
import matplotlib.pyplot as plt

# VARIABLES GLOBALES

carpeta_actual = ""
archivos_txt = []
archivos_csv = []

# Palabras que no queremos contar como palabras importantes
CONECTORES = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "a", "ante", "bajo", "con", "contra", "desde",
    "en", "entre", "hacia", "hasta", "para", "por", "segun",
    "sin", "sobre", "tras", "y", "e", "o", "u", "que", "se",
    "es", "al", "lo", "como", "su", "sus", "mi", "tu"
}

# 1. EXPLORAR DIRECTORIO

def explorar_directorio():
    global carpeta_actual, archivos_txt, archivos_csv

    ruta = input("\nIngrese la ruta de la carpeta: ").strip().strip('"')

    if not os.path.isdir(ruta):
        print("\nLa ruta ingresada no existe.")
        return

    carpeta_actual = ruta

    archivos_txt = []
    archivos_csv = []

    for archivo in os.listdir(ruta):
        if archivo.lower().endswith(".txt"):
            archivos_txt.append(archivo)
        elif archivo.lower().endswith(".csv"):
            archivos_csv.append(archivo)

    print("\n========== ARCHIVOS DISPONIBLES ==========")

    if not archivos_txt and not archivos_csv:
        print("No se encontraron archivos .txt o .csv.")
        return

    print("\nArchivos TXT:")
    if archivos_txt:
        for i, archivo in enumerate(archivos_txt, 1):
            print(i, "-", archivo)
    else:
        print("No hay archivos TXT.")

    print("\nArchivos CSV:")
    if archivos_csv:
        for i, archivo in enumerate(archivos_csv, 1):
            print(i, "-", archivo)
    else:
        print("No hay archivos CSV.")

# SELECCIONAR ARCHIVO

def seleccionar_archivo(lista):
    if carpeta_actual == "":
        print("\nPrimero debe explorar un directorio.")
        return None

    if not lista:
        print("\nNo hay archivos disponibles de este tipo.")
        return None

    print("\nArchivos disponibles:")

    for i, archivo in enumerate(lista, 1):
        print(i, "-", archivo)

    try:
        opcion = int(input("\nSeleccione un archivo: "))

        if opcion < 1 or opcion > len(lista):
            print("Opción fuera de rango.")
            return None

        return os.path.join(carpeta_actual, lista[opcion - 1])

    except ValueError:
        print("Debe ingresar un número.")
        return None

# LEER TXT

def leer_txt(ruta):
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as archivo:
            return archivo.readlines()

    except FileNotFoundError:
        print("\nEl archivo no fue encontrado.")
        return None

# OBTENER PALABRAS

def obtener_palabras(lineas):
    texto = " ".join(lineas).lower()

    # Busca únicamente palabras
    palabras = re.findall(r"[a-záéíóúñü]+", texto)

    # Eliminar conectores
    palabras_limpias = []

    for palabra in palabras:
        if palabra not in CONECTORES:
            palabras_limpias.append(palabra)

    return palabras_limpias

# TXT - RESUMEN ESTADÍSTICO

def resumen_texto(ruta):
    lineas = leer_txt(ruta)

    if lineas is None:
        return

    texto = "".join(lineas)

    palabras_totales = re.findall(r"[a-záéíóúñü]+", texto.lower())
    palabras_limpias = obtener_palabras(lineas)

    caracteres_con_espacios = len(texto)
    caracteres_sin_espacios = len(texto.replace(" ", "").replace("\n", ""))

    frecuentes = Counter(palabras_limpias).most_common(5)

    print("\n========== RESUMEN ESTADÍSTICO ==========")
    print("Total de líneas:", len(lineas))
    print("Total de palabras:", len(palabras_totales))
    print("Caracteres con espacios:", caracteres_con_espacios)
    print("Caracteres sin espacios:", caracteres_sin_espacios)

    print("\nTop 5 palabras más repetidas:")

    if frecuentes:
        for palabra, cantidad in frecuentes:
            print(palabra, ":", cantidad)
    else:
        print("No se encontraron palabras.")

# TXT - EXTRAER PATRONES DE LOGS

def extraer_patrones(ruta):
    lineas = leer_txt(ruta)

    if lineas is None:
        return

    texto = "".join(lineas)

    errores = len(re.findall(r"\bERROR\b", texto, re.IGNORECASE))
    errores_404 = len(re.findall(r"\b404\b", texto))

    # Formatos comunes: 25/10/2026 o 25-10-2026
    fechas = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b", texto)

    print("\n========== PATRONES ENCONTRADOS ==========")
    print("Apariciones de ERROR:", errores)
    print("Apariciones de 404:", errores_404)
    print("Fechas encontradas:", len(fechas))

    if fechas:
        print("\nFechas más frecuentes:")

        for fecha, cantidad in Counter(fechas).most_common(5):
            print(fecha, ":", cantidad)

# TXT - GRÁFICO DE PALABRAS

def grafico_palabras(ruta):
    lineas = leer_txt(ruta)

    if lineas is None:
        return

    palabras = obtener_palabras(lineas)
    frecuentes = Counter(palabras).most_common(10)

    if not frecuentes:
        print("\nNo hay palabras suficientes para generar el gráfico.")
        return

    nombres = []
    cantidades = []

    for palabra, cantidad in frecuentes:
        nombres.append(palabra)
        cantidades.append(cantidad)

    # Invertir para que la más frecuente aparezca arriba
    nombres.reverse()
    cantidades.reverse()

    plt.barh(nombres, cantidades)
    plt.title("10 palabras más frecuentes")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")
    plt.tight_layout()
    plt.show()

# TXT - HISTOGRAMA DE LONGITUD DE LÍNEAS

def grafico_longitud_lineas(ruta):
    lineas = leer_txt(ruta)

    if lineas is None:
        return

    longitudes = []

    for linea in lineas:
        longitudes.append(len(linea.rstrip("\n")))

    if not longitudes:
        print("\nEl archivo está vacío.")
        return

    mayor = max(longitudes)

    # Intervalos 0-50, 51-100, etc.
    limite = ((mayor // 50) + 2) * 50
    intervalos = range(0, limite + 1, 50)

    plt.hist(longitudes, bins=intervalos, edgecolor="black")
    plt.title("Distribución de longitud de líneas")
    plt.xlabel("Cantidad de caracteres")
    plt.ylabel("Número de líneas")
    plt.tight_layout()
    plt.show()

# LEER CSV

def leer_csv(ruta):
    try:
        with open(ruta, "r", encoding="utf-8-sig", errors="ignore") as archivo:

            muestra = archivo.read(2048)
            archivo.seek(0)

            try:
                delimitador = csv.Sniffer().sniff(
                    muestra,
                    delimiters=",;\t"
                ).delimiter
            except csv.Error:
                delimitador = ","

            lector = csv.DictReader(archivo, delimiter=delimitador)

            columnas = lector.fieldnames

            if columnas is None:
                print("\nEl CSV no tiene encabezados.")
                return None, None

            datos = list(lector)

            return columnas, datos

    except FileNotFoundError:
        print("\nEl archivo no fue encontrado.")
        return None, None

# MOSTRAR COLUMNAS

def seleccionar_columna(columnas, mensaje):
    print("\nColumnas disponibles:")

    for i, columna in enumerate(columnas, 1):
        print(i, "-", columna)

    try:
        opcion = int(input("\n" + mensaje + ": "))

        if opcion < 1 or opcion > len(columnas):
            print("Opción fuera de rango.")
            return None

        return columnas[opcion - 1]

    except ValueError:
        print("Debe ingresar un número.")
        return None

# CSV - VISTA PREVIA

def vista_previa(ruta):
    columnas, datos = leer_csv(ruta)

    if datos is None:
        return

    print("\n========== COLUMNAS ==========")
    print(" | ".join(columnas))

    print("\n========== PRIMERAS 10 FILAS ==========")

    for fila in datos[:10]:
        print(" | ".join(str(fila.get(columna, "")) for columna in columnas))

    print("\n========== ÚLTIMAS 5 FILAS ==========")

    for fila in datos[-5:]:
        print(" | ".join(str(fila.get(columna, "")) for columna in columnas))

# CONVERTIR COLUMNA A NÚMEROS

def obtener_numeros(datos, columna):
    numeros = []

    for fila in datos:
        valor = fila.get(columna, "").strip()

        if valor == "":
            continue

        try:
            numero = float(valor.replace(",", "."))
            numeros.append(numero)

        except ValueError:
            continue

    return numeros

# CSV - ESTADÍSTICAS DESCRIPTIVAS

def estadisticas_csv(ruta):
    columnas, datos = leer_csv(ruta)

    if datos is None:
        return

    columna = seleccionar_columna(
        columnas,
        "Seleccione una columna numérica"
    )

    if columna is None:
        return

    numeros = obtener_numeros(datos, columna)

    if not numeros:
        print("\nLa columna seleccionada no contiene datos numéricos válidos.")
        return

    print("\n========== ESTADÍSTICAS ==========")
    print("Columna:", columna)
    print("Registros válidos:", len(numeros))
    print("Promedio:", round(statistics.mean(numeros), 2))
    print("Mediana:", round(statistics.median(numeros), 2))
    print("Valor máximo:", max(numeros))
    print("Valor mínimo:", min(numeros))

# CSV - GRÁFICO DE TENDENCIA

def grafico_tendencia(ruta):
    columnas, datos = leer_csv(ruta)

    if datos is None:
        return

    columna_x = seleccionar_columna(
        columnas,
        "Seleccione la columna para el eje X (por ejemplo Fecha)"
    )

    if columna_x is None:
        return

    columna_y = seleccionar_columna(
        columnas,
        "Seleccione la columna numérica para el eje Y"
    )

    if columna_y is None:
        return

    x = []
    y = []

    for fila in datos:
        valor_x = fila.get(columna_x, "").strip()
        valor_y = fila.get(columna_y, "").strip()

        if valor_x == "" or valor_y == "":
            continue

        try:
            numero = float(valor_y.replace(",", "."))

            x.append(valor_x)
            y.append(numero)

        except ValueError:
            continue

    if not y:
        print("\nNo hay datos válidos para generar el gráfico.")
        return

    plt.plot(x, y, marker="o")
    plt.title(columna_y + " según " + columna_x)
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)

    # Evita que las fechas o categorías se amontonen
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# CSV - GRÁFICO DE PASTEL

def grafico_pastel(ruta):
    columnas, datos = leer_csv(ruta)

    if datos is None:
        return

    columna = seleccionar_columna(
        columnas,
        "Seleccione una columna categórica"
    )

    if columna is None:
        return

    valores = []

    for fila in datos:
        valor = fila.get(columna, "").strip()

        if valor != "":
            valores.append(valor)

    if not valores:
        print("\nNo hay datos válidos.")
        return

    conteo = Counter(valores)

    etiquetas = list(conteo.keys())
    cantidades = list(conteo.values())

    plt.pie(
        cantidades,
        labels=etiquetas,
        autopct="%1.1f%%"
    )

    plt.title("Distribución de " + columna)
    plt.tight_layout()
    plt.show()

# CSV - GRÁFICO DE DISPERSIÓN

def grafico_dispersion(ruta):
    columnas, datos = leer_csv(ruta)

    if datos is None:
        return

    columna_x = seleccionar_columna(
        columnas,
        "Seleccione la primera columna numérica"
    )

    if columna_x is None:
        return

    columna_y = seleccionar_columna(
        columnas,
        "Seleccione la segunda columna numérica"
    )

    if columna_y is None:
        return

    x = []
    y = []

    for fila in datos:
        valor_x = fila.get(columna_x, "").strip()
        valor_y = fila.get(columna_y, "").strip()

        try:
            numero_x = float(valor_x.replace(",", "."))
            numero_y = float(valor_y.replace(",", "."))

            x.append(numero_x)
            y.append(numero_y)

        except ValueError:
            continue

    if not x:
        print("\nNo hay suficientes datos numéricos válidos.")
        return

    plt.scatter(x, y)
    plt.title(columna_x + " vs " + columna_y)
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.tight_layout()
    plt.show()

# SUBMENÚ TXT

def menu_txt():
    ruta = seleccionar_archivo(archivos_txt)

    if ruta is None:
        return

    while True:

        print("\n========== ANÁLISIS DE TXT ==========")
        print("Archivo:", os.path.basename(ruta))
        print()
        print("1. Resumen estadístico del texto")
        print("2. Extracción de patrones")
        print("3. Gráfico de palabras frecuentes")
        print("4. Histograma de longitud de líneas")
        print("5. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            resumen_texto(ruta)

        elif opcion == "2":
            extraer_patrones(ruta)

        elif opcion == "3":
            grafico_palabras(ruta)

        elif opcion == "4":
            grafico_longitud_lineas(ruta)

        elif opcion == "5":
            break

        else:
            print("\nOpción inválida.")

# SUBMENÚ CSV

def menu_csv():
    ruta = seleccionar_archivo(archivos_csv)

    if ruta is None:
        return

    while True:

        print("\n========== ANÁLISIS DE CSV ==========")
        print("Archivo:", os.path.basename(ruta))
        print()
        print("1. Vista previa de datos")
        print("2. Estadísticas descriptivas")
        print("3. Evolución temporal / tendencia")
        print("4. Comparación categórica")
        print("5. Correlación de variables")
        print("6. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            vista_previa(ruta)

        elif opcion == "2":
            estadisticas_csv(ruta)

        elif opcion == "3":
            grafico_tendencia(ruta)

        elif opcion == "4":
            grafico_pastel(ruta)

        elif opcion == "5":
            grafico_dispersion(ruta)

        elif opcion == "6":
            break

        else:
            print("\nOpción inválida.")

# MENÚ PRINCIPAL

def main():

    while True:

        print("\n==========================================")
        print("     ANÁLISIS DE DATOS TXT Y CSV")
        print("==========================================")
        print("1. Explorar directorio")
        print("2. Procesar Bitácoras / Textos Reales (.txt)")
        print("3. Analizar Dataset de Datos Abiertos (.csv)")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            explorar_directorio()

        elif opcion == "2":
            menu_txt()

        elif opcion == "3":
            menu_csv()

        elif opcion == "4":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

# INICIAR PROGRAMA

if __name__ == "__main__":
    main()
