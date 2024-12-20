# LABORATORIO 3-3 - SPARK CON NOTEBOOKS Y PYSPARK.

---
---
---

# CONTENIDO DEL EJERCICIO SOLICITADO.
ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2024-2

Lab 3-3 - Spark con Notebooks y PySpark.

* realice la reproducción y entendimiento de los notebooks que hay en:

* 04-spark
---
# Universidad EAFIT
# Curso ST0263 Tópicos Especiales en Telemática, 2024-2

# LAB SPARK

* Se puede programar en python, scala o java.

* ejemplos en python:

## 1. De forma interactiva via 'pyspark' (en el nodo master de EMR)

// ya trae preconfigurado las variables sc y spark

    $ pyspark
    >>> files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
    >>> files_rdd = sc.textFile("s3://emontoyadatasets/gutenberg-small/*.txt")
    >>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    >>> wc = wc_unsort.sortBy(lambda a: -a[1])
    >>> for tupla in wc.take(10):
    >>>     print(tupla)
    >>> wc.saveAsTextFile("hdfs:///tmp/wcout1")

    * asi salva wc un archivo por rdd.
    * si quiere que se consolide en un solo archivo de salida:

    $ pyspark
    >>> ...
    >>> ...
    >>> wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout2")

## 2. Como un archivo python: [wc-pyspark.py](wc-pyspark.py)

* correrlo:

    $ spark-submit --master yarn --deploy-mode cluster wc-pyspark.py

## 3. Desde Zeppelin Nodebook:

    * Si es en EMR, por defecto NO tiene login/pass

![login](fotos-cont-lab/zeppelin-login.png)

Cree un Notebook:

![crear Notebook](fotos-cont-lab/zeppelin-create1.png)

![crear Notebook](fotos-cont-lab/zeppelin-create2.png)

### Wordcount en python:

```python
    %spark2.pyspark
    # WORDCOUNT COMPACTO
    #files_rdd = sc.textFile("s3://emontoyadatasets/gutenberg-small/*.txt")
    files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
    wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    wc = wc_unsort.sortBy(lambda a: -a[1])
    for tupla in wc.take(10):
        print(tupla)
    wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout1")
```
## 4. Jupyter Notebooks en EMR

1. Clone el cluster EMR
2. cree un notebook
3. importe el archivo [wordcount-spark.ipynb](wordcount-spark.ipynb) o copie las lineas en un nonebook nuevo.
4. Ejecute el notebook paso a paso y comprenda los diferentes pasos.

### NOTA: Manejo de notebooks en EMR

* varias opciones:

    ** a través del servicio jupyterhub como componente de EMR
    ** Notebooks como servicio de amazon para EMR (opción a trabajar)

Para trabajar con los notebooks gestionados por amazon, la gestión de paquetes, versión de python puede ser consultado en:

    https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-scoped-libraries.html

* Opciones importantes:

** cambiar versión de python:

    %%configure -f
    { "conf":{
    "spark.pyspark.python": "python3",
    "spark.pyspark.virtualenv.enabled": "true",
    "spark.pyspark.virtualenv.type":"native",
    "spark.pyspark.virtualenv.bin.path":"/usr/bin/virtualenv"
    }}

** Example – Listing Current Libraries

    sc.list_packages()

** Example – Installing the NLTK Library

    sc.install_pypi_package("nltk")

** Example – Uninstalling a Library

    sc.uninstall_package("nltk")
---

Teniendo como entrada los datos ejemplo: datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia.csv

si quiere trabajar con los últimos datos, descarguelos de: 

    https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD

        ejecute el comando:

        $ wget https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD

    o tambien están en el github: datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia.csv.zip

Utilizando como base el jupyter notebook: 03-spark/Data_processing_using_PySpark.ipynb realice sobre los datos de covid:

1. almacenar datos en AWS S3 y en google drive (ojo, en ambos)
2. análisis exploratorio de datos en dataframes donde cargamos los datos: (programa en jupyterhub y google colab)
   2.1 columnas
   2.2 tipos de datos
   2.3 seleccionar algunas columnas
   2.4 RENOMBRAR COLUMNAS (esto se recomienda hacerlo para facilitar el procesamiento posterior)
   2.5 agregar columnas
   2.6 borrar columnas
   2.7 filtrar datos
   2.8 ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.

3. contestar las siguientes preguntas de negocio sobre los datos de covid:

ESTE NUMERAL 3, debe ser realizado con 2 tipos de procesamiento Spark: Dataframes y SparkSQL

Ver ejemplo de procesamiento en SparkSQL en:
https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html

Los datos de prueba de este anterior ejemplo:
https://github.com/databricks/LearningSparkV2/tree/master/databricks-datasets/learning-spark-v2/flights

   3.1 Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.
   3.2 Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor.
   3.3 Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.
   3.4 Distribución de casos por edades de covid en Colombia.
   3.5 Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark.

4. salve los datos del numeral 3, en el bucket público de cada estudiante

5. El lab6-2 debe ser realizado en AWS-EMR-jupyterhub y Google Colab con datos origen y destino en S3 y en google drive.

Entregables:

Cada alumno enviará al profesor vía buzón:

      El notebook .ipynb donde desarrolla los numerales 2.x y 3.x
      La URI del S3 donde están los datos de entrada y salida del numeral 3.x
      Notebooks y URI entregados vía Buzón de Interactiva Virtual.
      

---
---
---