
# AnalizadorEstadisticoJudicial

## Propósito

Este programa está diseñado para analizar archivos Excel relacionados con la organización del trabajo y la eficiencia en la Judicatura. Automáticamente procesa los datos y genera un consolidado, facilitando la tarea de análisis y presentación de informes.

## ¿Qué hace?

El programa busca archivos Excel con nombres específicos (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.), incluidos aquellos que tienen un sufijo numérico, como 'Tercer Trimestre_1.xls', en caso de que haya múltiples archivos para un trimestre específico. Procesa cada hoja de estos archivos y finalmente genera un archivo consolidado con los resultados.

## ¿Cómo lo hace?

1. Lee cada archivo Excel.
2. Procesa cada hoja dentro de los archivos.
3. Genera un archivo de resultados por cada archivo Excel.
4. Crea un archivo consolidado con todos los resultados.

## Instrucciones de Uso

1. Asegúrese de que todos los archivos Excel que desea analizar se encuentren en la misma carpeta que este programa.
2. Ejecute el programa.
3. Revise la carpeta 'Consolidado' que se creará automáticamente; allí encontrará los resultados.

Nota: Si ejecuta el programa en la raíz donde están los documentos, se creará automáticamente una carpeta 'Consolidado' con los archivos de resultados.

## Desarrollador

Desarrollado por Alexander Oviedo Fadul, Profesional Universitario Grado 11 del Consejo Seccional de la Judicatura de Sucre.

## Funcionalidades Potenciales

- Integración Directa con SIERJU: Si se obtiene acceso a la API o a alguna interfaz de programación de SIERJU, podríamos adaptar el programa para enviar directamente las estadísticas.
- Análisis Avanzado: Incorporar herramientas de análisis estadístico más avanzadas para obtener insights más detallados de los datos.
- Visualización de Datos: Incorporar gráficos y tableros de mando para una visualización más intuitiva de las estadísticas.

## Adaptabilidad

Es importante que cualquier desarrollo software, especialmente en contextos institucionales, sea fácilmente adaptable a cambios futuros. Esto no solo incluye cambios en la estructura de los datos, sino también en las necesidades del usuario y en el contexto legal y regulatorio.
    