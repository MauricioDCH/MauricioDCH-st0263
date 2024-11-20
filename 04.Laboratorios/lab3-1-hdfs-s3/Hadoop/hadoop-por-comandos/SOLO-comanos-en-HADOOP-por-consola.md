# DATOS DE MI CLUSTER EMR

## URL ejemplo para HUE: http://ec2-54-89-19-17.compute-1.amazonaws.com:8888/

Podemos ingresar la siguiente información para crear el usuario.

- **User:** hadoop
- **Contraseña:** HMauricio159!!!

Para entrar por terminal con Linux, después de haber creado el usuario `hadoop`.

```bash
ssh -i "laboratorio-3.pem" hadoop@ec2-3-234-143-224.compute-1.amazonaws.com 
```

# TERMINAL EJECUTADA DURANTE LA ELABORACIÓN DEL LABORATORIO.
- [TERMINAL COMPLETA HADOOP SOLO COMANDOS](TERMINAL_COMPLETA_HADOOP-SOLO-COMANDOS.md)
- [TERMINAL COMPLETA HADOOP](TERMINAL_COMPLETA_HADOOP.md)

# COMANDOS REALIZADOS EN CONSOLA PARA TRABAJAR CON HADOOP.

### DEBEMOS EJECUTAR LO SIGUIENTE PARA TRABAJAR EN HADOOP CON EL USUARIO CREADO HADOOP.

### Instalamos git.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo yum install git
```

### Clonamos el repositorio de la materia de Tópicos de telemática.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo git clone https://github.com/st0263eafit/st0263-242.git
```

### Creamos en hadoop el directorio 'datasets'.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets
```

### Verificamos que se haya creado el directorio y esté vacío.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets
```

### Creamos en hadoop el directorio 'gutenberg-small'.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
```

### Verificamos que se haya creado el directorio y esté vacío.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg-small
```

### Verificamos el contenido de la carpeta /root/
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls /root/
st0263-242
```

### Movemos la carpeta st0263-242 al home del usuario hadoop.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo mv /root/st0263-242/ /home/hadoop/
```

### Verificamos que se haya movido la carpeta al home del usuario hadoop.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
st0263-242
```

### Verificamos el contenido de la carpeta que está dentro de la ruta '/st0263-242/bigdata/datasets/gutenberg-small/'
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
```

### Verificamos que el contenido de la carpeta que está en el sistema hadoop esté vacía.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg-small/
```

### Subimos todos los archivos terminados en .txt que están en el directorio local '/home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/' a hadoop en la carpeta '/user/hadoop/datasets/gutenberg-small/' dentro del sistema de hadoop.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/*.txt /user/hadoop/datasets/gutenberg-small/
```

### Verificamos el contenido recién subido a hadoop.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg-small/
Found 16 items
-rw-r--r--   1 hadoop hdfsadmingroup       5878 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnLetters.txt
-rw-r--r--   1 hadoop hdfsadmingroup      21586 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsFirstInauguralAddress.txt
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup     262083 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt
-rw-r--r--   1 hadoop hdfsadmingroup       4093 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsSecondInauguralAddress.txt
-rw-r--r--   1 hadoop hdfsadmingroup     516298 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt
-rw-r--r--   1 hadoop hdfsadmingroup     167895 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___StateoftheUnionAddresses.txt
-rw-r--r--   1 hadoop hdfsadmingroup       3928 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheEmancipationProclamation.txt
-rw-r--r--   1 hadoop hdfsadmingroup      45664 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt
-rw-r--r--   1 hadoop hdfsadmingroup     459006 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
-rw-r--r--   1 hadoop hdfsadmingroup     505150 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
-rw-r--r--   1 hadoop hdfsadmingroup     254941 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
-rw-r--r--   1 hadoop hdfsadmingroup     209643 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
-rw-r--r--   1 hadoop hdfsadmingroup     692051 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
-rw-r--r--   1 hadoop hdfsadmingroup     601102 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
-rw-r--r--   1 hadoop hdfsadmingroup     478689 2024-10-22 04:20 /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
```

### Creamos una nueva carpeta llamada '/mis_datasets/' dentro del home del usuario hadoop y luego verificamos la creación de la carpeta.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo mkdir /home/hadoop/mis_datasets/
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
mis_datasets  st0263-242
```

### Descargamos con el método 'get' todo el contenido que está en el sistema de hadoop en el directorio /user/hadoop/datasets/gutenberg-small/ y lo subimos a la carpeta local recién creada.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo hdfs dfs -get /user/hadoop/datasets/gutenberg-small/* ~hadoop/mis_datasets/
```

### Verificamos el contenido de descargado.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/mis_datasets/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
```

### Creamos un nuevo directorio en hadoop llamado '/gutenberg/'.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/gutenberg/
```

### Verificamos el contenido de la carpeta /home/hadoop/st0263-242/bigdata/datasets/gutenberg/
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg/
gutenberg-small-es.zip  gutenberg-txt-es.zip-url.txt
```

### Subimos al sistema hadoop el contenido del directorio /home/hadoop/st0263-242/bigdata/datasets/gutenberg/ en el directorio /user/hadoop/datasets/gutenberg/. Posteriormente verificamos el contenido subido.
```bash
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg/* /user/hadoop/datasets/gutenberg/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup    3419810 2024-10-22 04:47 /user/hadoop/datasets/gutenberg/gutenberg-small-es.zip
-rw-r--r--   1 hadoop hdfsadmingroup         67 2024-10-22 04:47 /user/hadoop/datasets/gutenberg/gutenberg-txt-es.zip-url.txt
```

### Descargamos con el método 'copyToLocal' el archivo 'gutenberg-small-es.zip' que está en el sistema de hadoop en el directorio /user/hadoop/datasets/gutenberg/ y lo subimos a la carpeta local recién creada.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo hdfs dfs -copyToLocal /user/hadoop/datasets/gutenberg/gutenberg-small-es.zip ~hadoop/mis_datasets/
```

### Verificamos que el archivo gutenberg-small-es.zip se haya descargado correctamente.
```bash
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/mis_datasets/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt                      gutenberg-small-es.zip
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
```

# PROBANDO OTROS COMANDOS.
```bash
####################

# Comando: hdfs dfs -du <path>             uso de disco en bytes

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -du /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
1653  1653  /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
```

```bash
####################

# Comando: hdfs dfs -mv <src> <dest>       mover archive(s)

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/toMove
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mv /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt /user/hadoop/datasets/toMove/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 1 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
```

```bash
####################

# Comando: hdfs dfs -cp <src> <dest>       copiar archivo(s)

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -cp /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt /user/hadoop/datasets/toMove/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup     459006 2024-10-22 05:10 /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
```

```bash
####################

# Comando: hdfs dfs -rm <path>             borrar archive(s)

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -rm /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
Deleted /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 1 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
```

```bash
####################

# Comando: hdfs dfs -put <localSrc> <dest-hdfs> copiar local a hdfs
# YA SE HICIERON SUFICIENTES PRUEBAS.
```

```bash
####################

# Comando: hdfs dfs -cat <file-name>       mostrar contenido de archivo

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -cat /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt


Lincoln's Gettysburg Address, given November 19, 1863
on the battlefield near Gettysburg, Pennsylvania, USA


Four score and seven years ago, our fathers brought forth
upon this continent a new nation:  conceived in liberty, and
dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war. . .testing whether
that nation, or any nation so conceived and so dedicated. . .
can long endure.  We are met on a great battlefield of that war.

We have come to dedicate a portion of that field as a final resting place
for those who here gave their lives that this nation might live.
It is altogether fitting and proper that we should do this.

But, in a larger sense, we cannot dedicate. . .we cannot consecrate. . .
we cannot hallow this ground.  The brave men, living and dead,
who struggled here have consecrated it, far above our poor power
to add or detract.  The world will little note, nor long remember,
what we say here, but it can never forget what they did here.

It is for us the living, rather, to be dedicated here to the unfinished
work which they who fought here have thus far so nobly advanced.
It is rather for us to be here dedicated to the great task remaining
before us. . .that from these honored dead we take increased devotion
to that cause for which they gave the last full measure of devotion. . .
that we here highly resolve that these dead shall not have died in vain. . .
that this nation, under God, shall have a new birth of freedom. . .
and that government of the people. . .by the people. . .for the people. . .
shall not perish from this earth.
```
```bash
####################
# Comando: hdfs dfs -chmod [-R] mode       cambiar los permisos de un archivo

# Ejecución:
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -touchz /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup          0 2024-10-22 05:20 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -chmod 600 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-------   1 hadoop hdfsadmingroup          0 2024-10-22 05:20 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
```

```bash
####################

#Comando: hdfs dfs -chown <username> files   cambiar el dueño de un archivo

#Ejecución:
#NO SE VA A PROBAR POR CUESTIONES DE TIEMPO.
```

```bash
####################

#Comando: hdfs dfs -chgrp <group> files      cambiar el grupo de un archivo

#Ejecución:
#NO SE VA A PROBAR POR CUESTIONES DE TIEMPO.
```