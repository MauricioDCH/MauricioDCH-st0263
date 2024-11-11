# COMANDOS REALIZADOS EN CONSOLA PARA TRABAJAR CON S3.

## COMANDO PARA VER LA VERSIÓN QUE TENEMOS DE AWS.
```bash
[hadoop@ip-172-31-10-177 ~]$ aws --version
```
## COMANDO PARA VER LOS BUCKETS QUE TENGO EN S3
```bash
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls
```

## COMANDO PARA CREAR UN NUEVO BUCKET
```bash
[hadoop@ip-172-31-10-177 ~]$ aws s3api create-bucket --bucket datasetsbucket --region us-east-1
```

## COMANDO PARA VER LOS BUCKETS QUE TENGO EN S3
```bash
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls
```

## COMANDO PARA CREAR UNA NUEVA CARPETA EN S3 POR CONSOLA.
```bash
[hadoop@ip-172-31-10-177 ~]$ aws s3api put-object --bucket datasetsbucket --key nueva_carpeta_por_comandos/
```

## COMANDO PARA VER EL CONTENIDO DE MI BUCKET datasetsbucket.
```bash
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls s3://datasetsbucket/
```

## COMANDO QUE CREA EN LOCAL UN ARCHIVO emptyfile.txt Y LO SUBE EN S3 EN s3://datasetsbucket/nueva_carpeta_por_comandos/
```bash
[hadoop@ip-172-31-10-177 ~]$ touch emptyfile.txt
[hadoop@ip-172-31-10-177 ~]$ aws s3 cp emptyfile.txt s3://datasetsbucket/nueva_carpeta_por_comandos/
```

## COMANDO PARA VER EL ARCHIVO RECIÉN CREADO emptyfile.txt
```bash
[hadoop@ip-172-31-10-177 root]$ aws s3 ls s3://datasetsbucket/nueva_carpeta_por_comandos/
```

## COMANDO PARA TRAER UN ARCHIVO DESDE S3 A MI LOCAL.
```bash
[hadoop@ip-172-31-10-177 root]$ sudo aws s3 cp s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt /home/hadoop/para_s3/
```
## COMANDO PARA VER EL CONTENIDO DE MI ARCHIVO QUE ESTÁ EN S3 EN MI CONSOLA.
```bash
[hadoop@ip-172-31-10-177 root]$ aws s3 cp s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt -
Este es un archivo creado desde GUI en S3
```

## COMANDO EN EL QUE CREAMOS UN NUEVO BUCKET LLAMADO otrodatasetsbucket Y EL ARCHIVO otroArchivo.txt LO PASAMOS AL BUCKET CREADO CON EL NOMBRE DE ejemplo.txt
```bash
[hadoop@ip-172-31-10-177 root]$ aws s3api create-bucket --bucket otrodatasetsbucket --region us-east-1
[hadoop@ip-172-31-10-177 root]$ aws s3 mv s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt s3://otrodatasetsbucket/ejemplo.txt
```

## COMANDO PARA PASAR DE HADOOP A S3.
```bash
[hadoop@ip-172-31-10-177 root]$ hadoop fs -cp /user/hadoop/ s3a://datasetsbucket/
```

## COMANDO PARA PASAR DE S3 A HADOOP.
```bash
[hadoop@ip-172-31-10-177 root]$ hadoop fs -cp s3a://datasetsbucket/ /user/hadoop/
```

## COMANDOS PARA CREAR UN NUEVO BUCKET LLAMADO datasetsb Y SUBUR RECURSIVAMENTE LOS DATASETS QUE ESTÁN EN MI NAMESPACE LOCAL A DICHO BUCKET DENTRO DE LA CARPETA 'datasets'.
```bash
[hadoop@ip-172-31-10-177 root]$ aws s3api create-bucket --bucket datasetsb --region us-east-1

[hadoop@ip-172-31-10-177 root]$ aws s3 cp /home/hadoop/st0263-242/bigdata/datasets/ s3://datasetsb/datasets --recursive
```

## COMANDO PARA DESCARGAR RECURSIVAMENTE LOS ARCHIVOS Y DIRECTORIOS DE MI BUCKET  datasetsb QUE ESTÁN EN LA CARPETA datasets/ EN MI NAMESPACE LOCAL

```bash
[hadoop@ip-172-31-10-177 root]$ sudo aws s3 cp s3://datasetsb/datasets/ ~/datasets_local/ --recursive
```

## COMANDOS PARA CREAR UN NUEVO DIRECTORIO EN MI SISTEMA HDFS, Y DESCARGAR LOS ARCHIVOS DE MIS DATASETS QUE ESTÁN EN S3 A MI SISTEMA HDFS.

```bash
[hadoop@ip-172-31-10-177 root]$ hadoop fs -mkdir -p /user/hadoop/datasets_hadoop
[hadoop@ip-172-31-10-177 root]$ hadoop fs -cp s3a://datasetsb/datasets/ /user/hadoop/datasets_hadoop/
```

## COMANDO PARA BORRAR RECURSIVAMENTE LA INFORMACIÓN QUE TIENE LE BUCKET datasetsb.

```bash
[hadoop@ip-172-31-10-177 root]$ aws s3 rm s3://datasetsb/ --recursive
```

## COMANDO PARA VER LOS BUCKETS QUE TENGO EN S3
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3 ls
```

## COMANDO PARA BORRAR EL ARCHIVO ejemplo.txt DEL BUCKET otrodatasetsbucket.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3 rm s3://otrodatasetsbucket/ejemplo.txt
```

## COMANDO PARA VER EL CONTENIDO DEL BUCKET otrodatasetsbucket Y VERIFICAR QUE ESTÁ VACÍO PARA PODERLO BORRAR.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3 ls s3://otrodatasetsbucket/
```

## COMANDO PARA BORRAR EL BUCKET otrodatasetsbucket.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3api delete-bucket --bucket otrodatasetsbucket --region us-east-1
```

## COMANDO PARA VERIFICAR QUE EL BUCKET otrodatasetsbucket FUE BORRADO EXITOSAMENTE.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3 ls
```

## COMANDO PARA ELIMINAR RESTRICCIONES DE BLOQUEO AL ACCESO PÚBLICO AL BUCKET datasetsbucket.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3api put-public-access-block --bucket datasetsbucket --public-access-block-configuration '{
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
}'
```

## COMANDO PARA VERIFICAR EL ESTADO ACTUAL DE LAS RESTRICCIONES.

```bash
[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket datasetsbucket
```

## COMANDO PARA COPIAR OBJETOS ENTRE BUCKETS.
```bash
[hadoop@ip-172-31-9-11 root]$ aws s3 cp s3://datasetsb/datasets/spark/movie_reviews.csv s3://datasetsbucket/nueva_carpeta_por_comandos/movie_reviews.csv
```

