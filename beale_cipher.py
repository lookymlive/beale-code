import re
from collections import Counter
import matplotlib.pyplot as plt  # Import para visualización

# --- Funciones de procesamiento de texto ---
def preparar_texto(texto):
    """Limpia el texto, eliminando caracteres no alfanuméricos y convirtiendo a mayúsculas."""
    texto_limpio = re.sub(r'[^\w\s]', '', texto).upper()
    texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
    return texto_limpio

# --- Funciones de descifrado ---
def descifrar_con_declaracion(texto_cifrado, usar_ultima_letra=False):
    """Descifra un texto usando la Declaración de Independencia como clave."""
    declaracion = """When in the Course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another and to assume among the powers of the earth the separate and equal station to which the Laws of Nature and of Nature's God entitle them a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."""
    declaracion_limpia = preparar_texto(declaracion)
    palabras_declaracion = declaracion_limpia.split()
    if usar_ultima_letra:
        letras_declaracion = [palabra[-1] for palabra in palabras_declaracion]
    else:
        letras_declaracion = [palabra[0] for palabra in palabras_declaracion]

    texto_cifrado_limpio = preparar_texto(texto_cifrado)
    numeros = [int(x) for x in texto_cifrado_limpio.split()]
    descifrado = ""
    for digito in numeros:
        try:
            indice = digito - 1
            descifrado += letras_declaracion[indice]
        except IndexError:
            descifrado += "?"  # Marca los índices fuera de rango
        except ValueError:
            pass
    return descifrado

# --- Funciones de análisis ---
def analizar_longitud_palabras(texto):
    """Analiza la longitud de las 'palabras' en un texto cifrado."""
    texto_limpio = preparar_texto(texto)
    palabras = texto_limpio.split()
    longitudes = [len(palabra) for palabra in palabras]
    return Counter(longitudes)

def analizar_frecuencia(texto):
    """Analiza la frecuencia de dígitos individuales."""
    digitos = re.findall(r'\d+', texto)
    return Counter(digitos)

def analizar_frecuencia_pares(texto):
    """Analiza la frecuencia de pares de dígitos consecutivos."""
    digitos = re.findall(r'\d+', texto)
    pares = [digitos[i] + digitos[i+1] for i in range(len(digitos) - 1)]
    return Counter(pares)

def analizar_frecuencia_ngramas(texto, n):
    """Analiza la frecuencia de n-gramas de dígitos."""
    digitos = re.findall(r'\d+', texto)
    ngramas = [''.join(digitos[i:i+n]) for i in range(len(digitos) - n + 1)]
    return Counter(ngramas)

def buscar_coincidencias(longitudes_cifrado, longitudes_c2):
    """Busca coincidencias entre las longitudes de palabras en un cifrado y C2."""
    coincidencias = []
    for longitud, frecuencia in longitudes_cifrado.items():
        if longitud in longitudes_c2:
            coincidencias.append((longitud, frecuencia))
    return coincidencias

def visualizar_frecuencias(frecuencias, titulo):
    """Visualiza las frecuencias usando un gráfico de barras."""
    digitos = list(frecuencias.keys())
    frecuencias_valores = list(frecuencias.values())

    plt.bar(digitos, frecuencias_valores)
    plt.xlabel("Elementos")
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.show()

# --- Textos cifrados ---
texto_c1 = """...(texto de C1)"""
texto_c2 = """115, 73, 24, 80, 4, 28, 93, 76, 11, 8, 24, 85, 116, 172, 112, 16, 103, 86, 180, 100, 114, 101, 8, 112, 116, 92, 115, 76, 116, 112, 8, 115, 100, 85, 12, 96, 112, 100, 115, 116, 103, 101, 100, 114, 115"""
texto_c3 = """...(texto de C3)"""

# --- Análisis ---
descifrado_c2 = descifrar_con_declaracion(texto_c2)
print("Descifrado C2:", descifrado_c2)

longitud_palabras_c1 = analizar_longitud_palabras(texto_c1)
longitud_palabras_c2 = analizar_longitud_palabras(texto_c2)
longitud_palabras_c3 = analizar_longitud_palabras(texto_c3)

print("\nLongitud de palabras en C1:", longitud_palabras_c1)
print("Longitud de palabras en C2:", longitud_palabras_c2)
print("Longitud de palabras en C3:", longitud_palabras_c3)

coincidencias_c1_c2 = buscar_coincidencias(longitud_palabras_c1, longitud_palabras_c2)
print("\nCoincidencias de longitud entre C1 y C2:", coincidencias_c1_c2)

frecuencia_digitos_c1 = analizar_frecuencia(texto_c1)
frecuencia_digitos_c3 = analizar_frecuencia(texto_c3)
visualizar_frecuencias(frecuencia_digitos_c1, "Frecuencia de dígitos en C1") # Visualización
visualizar_frecuencias(frecuencia_digitos_c3, "Frecuencia de dígitos en C3") # Visualización

frecuencia_pares_c1 = analizar_frecuencia_pares(texto_c1)
frecuencia_pares_c3 = analizar_frecuencia_pares(texto_c3)
visualizar_frecuencias(frecuencia_pares_c1, "Frecuencia de pares de dígitos en C1") # Visualización
visualizar_frecuencias(frecuencia_pares_c3, "Frecuencia de pares de dígitos en C3") # Visualización

frecuencia_trigramas_c1 = analizar_frecuencia_ngramas(texto_c1, 3)
frecuencia_trigramas_c3 = analizar_frecuencia_ngramas(texto_c3, 3)
visualizar_frecuencias(frecuencia_trigramas_c1, "Frecuencia de trigramas de dígitos en C1") # Visualización
visualizar_frecuencias(frecuencia_trigramas_c3, "Frecuencia de trigramas de dígitos en C3") # Visualización