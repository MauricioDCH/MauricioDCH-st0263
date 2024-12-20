# ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2024-2

## Lab 3-3 - Spark con Notebooks y PySpark.

- Realice la reproducción y entendimiento de los notebooks que hay en: 04-spark

- Teniendo como entrada los datos ejemplo: datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia.csv

    Si quiere trabajar con los últimos datos, descarguelos de: 

        https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD

            ejecute el comando:

            $ wget https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD

        o tambien están en el github: datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia.csv.zip

    Utilizando como base el jupyter notebook: 03-spark/Data_processing_using_PySpark.ipynb realice sobre los datos de covid:

## 1. Almacenar datos en AWS S3 y en google drive (ojo, en ambos)
## 2. Análisis exploratorio de datos en dataframes donde cargamos los datos: (programa en jupyterhub y google colab)
- ###  2.1 Columnas
- ###  2.2 Tipos de datos
- ###  2.3 Seleccionar algunas columnas
- ###  2.4 RENOMBRAR COLUMNAS (esto se recomienda hacerlo para facilitar el procesamiento posterior)
- ###  2.5 Agregar columnas
- ###  2.6 Borrar columnas
- ###  2.7 Filtrar datos
- ###  2.8 Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.

## 3. Contestar las siguientes preguntas de negocio sobre los datos de covid:

ESTE NUMERAL 3, debe ser realizado con 2 tipos de procesamiento Spark: Dataframes y SparkSQL

Ver ejemplo de procesamiento en SparkSQL en:
https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html

Los datos de prueba de este anterior ejemplo:
https://github.com/databricks/LearningSparkV2/tree/master/databricks-datasets/learning-spark-v2/flights

- ### 3.1 Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.
- ### 3.2 Las 10 ciudades con más casos de covid en Colombia ordenados de ### mayor a menor.
- ### 3.3 Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.
- ### 3.4 Distribución de casos por edades de covid en Colombia.
- ### 3.5 Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark.

## 4. Salve los datos del numeral 3, en el bucket público de cada estudiante

## 5. El lab6-2 debe ser realizado en AWS-EMR-jupyterhub y Google Colab con datos origen y destino en S3 y en google drive.

## Entregables:

Cada alumno enviará al profesor vía buzón:

1. El notebook .ipynb donde desarrolla los numerales 2.x y 3.x
2. La URI del S3 donde están los datos de entrada y salida del numeral 3.x
3. Notebooks y URI entregados vía Buzón de Interactiva Virtual.