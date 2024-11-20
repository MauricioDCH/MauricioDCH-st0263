from pyspark.sql import SparkSession

# puede no necesitar instanciar las variables spark y sc si esta ejecutando en AWS EMR:
spark = SparkSession.builder.appName("WordCount").getOrCreate()
sc = spark.sparkContext


# Cargar desde HDFS
files_rdd = sc.textFile("hdfs:///user/hadoop/datasets/gutenberg-small/*.txt")

# O cargar desde S3
# files_rdd = sc.textFile("s3://datasets-mauricio/datasets/gutenberg-small/*.txt")

# Separar líneas en palabras y contar ocurrencias
wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Ordenar palabras por frecuencia (descendente)
wc = wc_unsort.sortBy(lambda a: -a[1])

# Consolidar el resultado en un solo archivo.
wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout3")