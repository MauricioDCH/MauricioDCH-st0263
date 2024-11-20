# LABORATORIO 3-1 - HADOOP y S3.

---
---
---

# CONTENIDO DEL EJERCICIO SOLICITADO.

ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2024-2

LAB 3-1: GESTIÓN DE ARCHIVOS EN HDFS Y S3 PARA BIG DATA

1. trabajo individual, cada estudiante deberá responder por estas actividades.

2. seguir los lineamientos del github:

https://github.com/st0263eafit/st0263-242/tree/main/bigdata

HACER LAS ACTIVIDADES PROPUESTAS EN:

https://github.com/st0263eafit/st0263-242/tree/main/bigdata/01-hdfs

3. Tener en cuenta la creación previa en el lab3-0 de la creación de un clúster EMR (ver videos previamente enviados), activará HUE, recuerden que deben crear un user 'hadoop' con la clave que gusten.

También se deben conectar vía shell (ssh) al nodo master del clúster EMR, donde realizará las actividades de HDFS CLI

En este cluster deben hacer:

* Copiar (gestión) de archivos hacia el HDFS vía HUE.

* Copiar (gestión) de archivos hacia el HDFS vía SSH.

Recuerden que estos datos de HDFS son efímeros o temporales y se borran cuando se borre el clúster.

* Copiar (gestión) de archivos hacia AWS S3 vía HUE.

* Copiar (gestión) de archivos hacia el AWS S3 vía SSH.

En esta infraestructura, cada alumno deberá realizar el copiado de los archivos datasets de:

https://github.com/st0263eafit/st0263-242/tree/main/bigdata/datasets

5. Cada alumno, de forma individual, deberá realizar estos labs.

Respecto a los buckets S3, deberán quedar de lectura pública (una simple consulta google: aws s3 public access, les dará los tips para lograrlo).

Este informe lab3-0, debe ser enviado por email de Interactiva Virtual, especificando explícitamente la URL de bucket publico donde están los datasets de trabajo.

Además debe depositar las evidencias en el formato template distribuido a cada estudiante en el onedrive de la materia.

---
---
---

## Hadoop.

### Breve descrición.

Hadoop es un marco de software de código abierto diseñado para procesar y almacenar grandes volúmenes de datos distribuidos en clusters de servidores. Fue desarrollado para manejar datos de manera eficiente y se compone de dos partes principales:

- **Hadoop Distributed File System (HDFS):** Un sistema de archivos distribuido que permite almacenar grandes archivos a través de múltiples nodos en un cluster.

- **MapReduce:** Un modelo de procesamiento paralelo que divide tareas en sub-tareas para ejecutar cálculos de manera simultánea en grandes conjuntos de datos.

Hadoop es popular en proyectos de big data y permite procesar grandes volúmenes de datos no estructurados o semiestructurados, ofreciendo escalabilidad y tolerancia a fallos.

### Las guías de solución para el sistema HADOOP están en el repositorio en los siguientes links.

- ## [Guía Hadoop por línea de comandos.](Hadoop/hadoop-por-comandos/SOLO-comanos-en-HADOOP-por-consola.md)
- ## [Guía Hadoop por GUI.](Hadoop/hadoop-por-gui/GUI-Para-Hadoop.md)

## Amazon S3 (Simple Storage Service) - AWS

### Breve descrición.

Amazon S3 es un servicio de almacenamiento de objetos en la nube ofrecido por Amazon Web Services (AWS). Está diseñado para almacenar y recuperar grandes cantidades de datos de manera escalable y con alta durabilidad. Las características clave incluyen:

- **Escalabilidad:** Puede almacenar prácticamente cantidades ilimitadas de datos.
- **Durabilidad y alta disponibilidad:** Replica los datos en varias zonas de disponibilidad para evitar pérdidas.
- **Flexibilidad:** Permite almacenar cualquier tipo de archivo (imágenes, videos, datos de aplicaciones) y es comúnmente usado para almacenar datos de entrada y salida en aplicaciones de big data.

Amazon S3 es utilizado en combinación con herramientas como Hadoop y Spark para almacenamiento y análisis de grandes volúmenes de datos en la nube, permitiendo acceder y gestionar estos datos de manera remota y segura.

### Las guías de solución para el sistema S3 están en el repositorio en los siguientes links.
- ## [Guía Amazon S3 por línea de comandos.](S3/s3-por-consola/SOLO-comanos-en-S3-por-consola.md)
- ## [Guía Amazon S3 por GUI.](S3/s3-por-gui/GUI-Para-S3.md)