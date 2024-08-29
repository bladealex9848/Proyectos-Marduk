
# AnalizadorEstadisticoJudicial

## Prop�sito

Este programa est� dise�ado para analizar archivos Excel relacionados con la organizaci�n del trabajo y la eficiencia en la Judicatura. Autom�ticamente procesa los datos y genera un consolidado, facilitando la tarea de an�lisis y presentaci�n de informes.

## �Qu� hace?

El programa busca archivos Excel con nombres espec�ficos (por ejemplo, 'Primer Trimestre.xls', 'Segundo Trimestre.xls', etc.), incluidos aquellos que tienen un sufijo num�rico, como 'Tercer Trimestre_1.xls', en caso de que haya m�ltiples archivos para un trimestre espec�fico. Procesa cada hoja de estos archivos y finalmente genera un archivo consolidado con los resultados.

## �C�mo lo hace?

1. Lee cada archivo Excel.
2. Procesa cada hoja dentro de los archivos.
3. Genera un archivo de resultados por cada archivo Excel.
4. Crea un archivo consolidado con todos los resultados.

## Instrucciones de Uso

1. Aseg�rese de que todos los archivos Excel que desea analizar se encuentren en la misma carpeta que este programa.
2. Ejecute el programa.
3. Revise la carpeta 'Consolidado' que se crear� autom�ticamente; all� encontrar� los resultados.

Nota: Si ejecuta el programa en la ra�z donde est�n los documentos, se crear� autom�ticamente una carpeta 'Consolidado' con los archivos de resultados.

## Desarrollador

Desarrollado por Alexander Oviedo Fadul, Profesional Universitario Grado 11 del Consejo Seccional de la Judicatura de Sucre.

## Funcionalidades Potenciales

- Integraci�n Directa con SIERJU: Si se obtiene acceso a la API o a alguna interfaz de programaci�n de SIERJU, podr�amos adaptar el programa para enviar directamente las estad�sticas.
- An�lisis Avanzado: Incorporar herramientas de an�lisis estad�stico m�s avanzadas para obtener insights m�s detallados de los datos.
- Visualizaci�n de Datos: Incorporar gr�ficos y tableros de mando para una visualizaci�n m�s intuitiva de las estad�sticas.

## Adaptabilidad

Es importante que cualquier desarrollo software, especialmente en contextos institucionales, sea f�cilmente adaptable a cambios futuros. Esto no solo incluye cambios en la estructura de los datos, sino tambi�n en las necesidades del usuario y en el contexto legal y regulatorio.
    