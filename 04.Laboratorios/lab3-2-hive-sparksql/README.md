# LABORATORIO 3-2 - HIVE y SPARKSQL

---
---
---

# CONTENIDO DEL EJERCICIO SOLICITADO.
ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2024-2

Lab 3-2 - Hive y SparkSQL

Realice la reproducción y entendimiento de los ejercicios propuestos en:

1. 03-hive-sparksql
2. Realice la consulta de las tablas creadas en el numeral 1. con SparkSQL desde un notebook que cree para este punto 2.

---
---
---


## Apache Hive

### Breve descrición.

Apache Hive es una herramienta de data warehousing construida sobre **Hadoop** que permite realizar consultas y análisis de grandes volúmenes de datos almacenados en **HDFS** (Hadoop Distributed File System) mediante una sintaxis similar a SQL, conocida como **HiveQL**. 

**Características principales de Hive:**
1. **Data Warehousing**: Permite consultas SQL en datos distribuidos, transformando consultas HiveQL en trabajos MapReduce, lo que hace más fácil realizar análisis sobre grandes volúmenes de datos en un cluster Hadoop.
2. **Esquemas y Particiones**: Hive organiza datos en tablas y particiones, lo que facilita el filtrado y la organización de datos de manera eficiente.
3. **Optimización**: Incluye optimizaciones como el manejo de datos particionados y ordenados, y admite optimizaciones mediante el uso de índices para mejorar el rendimiento en consultas complejas.

**Casos de uso**:
Hive es ideal para **procesamiento batch** y consultas de datos estructurados, comúnmente en grandes volúmenes de datos históricos, como logs, registros financieros o análisis de tendencias.

### Las guías de solución para el sistema HIVE están en el repositorio en los siguientes links.

- [Guía de Hive.](hive/guia-hive.md)



## Apache Spark SQL

### Breve descrición.

Apache Spark SQL es el módulo de Apache Spark diseñado para realizar consultas SQL en grandes volúmenes de datos y trabaja en paralelo con el motor de procesamiento de datos **Spark**. A diferencia de Hive, que se basa en MapReduce, Spark SQL utiliza el motor de ejecución en memoria de Spark, lo que permite realizar consultas mucho más rápidas en comparación con Hive.

**Características principales de Spark SQL:**
1. **Ejecuta SQL y DataFrames**: Spark SQL permite trabajar tanto con sentencias SQL como con **DataFrames**, una estructura de datos distribuida similar a una tabla en una base de datos relacional. 
2. **Alto Rendimiento**: El procesamiento en memoria de Spark SQL permite realizar operaciones hasta 100 veces más rápido que Hadoop MapReduce en algunas cargas de trabajo.
3. **Integración con otros formatos de datos**: Spark SQL es compatible con **HDFS**, **Amazon S3**, y formatos de datos populares como **Parquet** y **Avro**, permitiendo consultas eficientes sobre grandes datasets en diferentes fuentes.

**Casos de uso**:
Spark SQL es ideal para aplicaciones de big data que requieren consultas interactivas, análisis en tiempo real, y machine learning, así como para la exploración y análisis de datos en grandes volúmenes, especialmente cuando se requiere un rendimiento superior en procesamiento.

### Las guías de solución para el sistema HIVE están en el repositorio en los siguientes links.

- [Guía de SparkSQL.](sparksql/guia-sparksql.md)