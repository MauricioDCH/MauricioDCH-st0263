# LABORATORIO 3-0 - INSTALACIÓN CLUSTER EMR versión 7.3.0. Hadoop/Spark.

---
---
---

# CONTENIDO DEL EJERCICIO SOLICITADO.

ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2024-2


Requisito: CADA ESTUDIANTE, EN SU REPOSITORIO GITHUB PARA LA MATERIA, 
DEBERÁ DOCUMENTAR Y ADJUNTAR TODAS LAS EVIDENCIAS DE LA REALIZACIÓN DE LOS LABORATORIOS DE BIG DATA.

CADA ALUMNO, DEBERÁ ENVIAR EXPLICITAMENTE AL PROFESOR POR INTERACTIVA VIRTUAL, LA URL DEL REPOSITORIO Y DIRECTORIO
DONDE TRABAJARÁ TODOS LOS LABS.

LAB 3-0: Crear un Cluster AWS EMR en Amazon para trabajar todos los laboratorios.

1. trabajo individual, cada estudiante deberá responder por estas actividades.

2. seguir los lineamientos del github:

https://github.com/st0263eafit/st0263-242/tree/main/bigdata

HACER LAS ACTIVIDADES PROPUESTAS EN LOS VIDEOS:

* https://www.youtube.com/watch?v=MyXSwxN5Zdk
* https://www.youtube.com/watch?v=3sao-qJG34Y

Información adicional:

* Creación de un clúster EMR (ver videos previamente enviados), activará HUE, recuerden que deben crear un user 'hadoop' con la clave que gusten.
* También se deben conectar vía shell (ssh) al nodo master del clúster EMR, donde realizará las actividades de HDFS CLI

---
---
---


## Amazon EMR (anteriormente denominada Amazon Elastic MapReduce).

### Breve descrición.

Amazon EMR (Elastic MapReduce) es un servicio de AWS que facilita el procesamiento y análisis de grandes volúmenes de datos en clusters escalables. Utiliza el marco de **Hadoop** para distribuir y procesar datos en múltiples nodos y es compatible con diversas herramientas de big data, como **Apache Spark**, **HBase**, **Presto**, y **Flink**, además de **Hadoop MapReduce**.

### Características Clave de Amazon EMR
1. **Configuración y Gestión Automatizada**: EMR automatiza la configuración y administración de clusters, incluyendo el aprovisionamiento, la configuración, y el ajuste de capacidad. Esto permite a los usuarios enfocarse en el procesamiento de datos en lugar de la administración del sistema.

2. **Escalabilidad**: EMR permite ajustar el tamaño del cluster de forma dinámica, añadiendo o eliminando nodos según la carga de trabajo, lo cual optimiza costos y tiempos de procesamiento.

3. **Integración con S3**: EMR puede integrarse fácilmente con **Amazon S3** para almacenar datos de entrada y salida, lo que permite mantener datos de manera duradera y altamente disponible fuera del cluster y reutilizarlos en múltiples trabajos o análisis.

4. **Soporte para Herramientas de Big Data**: EMR ofrece soporte para frameworks y herramientas de big data populares, como Apache Spark, HBase, Hive y Pig, permitiendo procesar y analizar datos de manera flexible.

5. **Costos Basados en Uso**: EMR permite pagar solo por la capacidad utilizada en el procesamiento, con la opción de usar instancias spot (capacidad ociosa en AWS) para reducir costos.

### Aplicaciones de EMR
EMR es útil para una variedad de aplicaciones de big data:
- **Análisis de datos**: Procesa grandes volúmenes de datos en tiempo real o por lotes.
- **Machine Learning**: Ejecuta algoritmos de ML en grandes datasets.
- **ETL (Extract, Transform, Load)**: Limpia, transforma, y carga datos hacia otros sistemas o almacenes de datos.
  
Amazon EMR es una solución ideal para aquellos que necesitan procesar datos a gran escala de manera rápida, rentable y sin la complejidad de gestionar la infraestructura.

### La guía de solución para Amazon EMR están en el repositorio en el siguiente link.

- ## [Guía creación Cluster EMR.](guia-creación-cluster-emr.md)
