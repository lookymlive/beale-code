# Beale Cipher Analysis

Este proyecto analiza y descifra textos cifrados utilizando la Declaración de Independencia de los Estados Unidos como clave. También realiza análisis de frecuencias y longitudes de palabras en los textos cifrados.

## Requisitos

- Python 3.x
- Bibliotecas adicionales:
  - `matplotlib`

Puedes instalar las bibliotecas necesarias ejecutando:
```sh
pip install matplotlib
Archivos
beale_cipher.py: Contiene el código principal para el análisis y descifrado de los textos cifrados.
Uso
Preparar el entorno: Asegúrate de tener Python 3.x y las bibliotecas necesarias instaladas.

Ejecutar el script: Ejecuta el script beale_cipher.py para realizar el análisis y descifrado de los textos cifrados.

Resultados: El script imprimirá en la consola los resultados del descifrado y los análisis de frecuencias y longitudes de palabras. También generará gráficos de barras para visualizar las frecuencias de dígitos y n-gramas.
Funciones Principales
preparar_texto(texto): Limpia el texto eliminando caracteres no alfanuméricos y convirtiéndolo a mayúsculas.
descifrar_con_declaracion(texto_cifrado, usar_ultima_letra=False): Descifra un texto cifrado usando la Declaración de Independencia como clave.
analizar_longitud_palabras(texto): Analiza la longitud de las palabras en un texto cifrado.
analizar_frecuencia(texto): Analiza la frecuencia de dígitos individuales en un texto cifrado.
analizar_frecuencia_pares(texto): Analiza la frecuencia de pares de dígitos consecutivos en un texto cifrado.
analizar_frecuencia_ngramas(texto, n): Analiza la frecuencia de n-gramas de dígitos en un texto cifrado.
buscar_coincidencias(longitudes_cifrado, longitudes_c2): Busca coincidencias entre las longitudes de palabras en un cifrado y C2.
visualizar_frecuencias(frecuencias, titulo): Visualiza las frecuencias usando un gráfico de barras.
Ejemplo de Uso
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.

