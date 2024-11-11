```bash





mdch@mdch-X532FLC-S532FL:~/Documents/01._Ingeniería_de_Sistemas-EAFIT/04._SEM/06
._S6-2024.02/04.Top_Telem/04-ACTIVIDADES/04.Laboratorios/01.Laboratorio/para-github/solución-Labs$ ssh -i "laboratorio-3.pem" hadoop@ec2-44-193-77-114.compute-1.amazonaws.com
The authenticity of host 'ec2-44-193-77-114.compute-1.amazonaws.com (44.193.77.114)' can't be established.
ED25519 key fingerprint is SHA256:DsMO3WCA8uCh/1xfzGmj2jrMkSs3xRqa7ly2N3P90Fk.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ec2-44-193-77-114.compute-1.amazonaws.com' (ED25519) to the list of known hosts.

A newer release of "Amazon Linux" is available.
  Version 2023.6.20241028:
  Version 2023.6.20241031:
Run "/usr/bin/dnf check-release-update" for full release and version update info
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
Last login: Sat Nov  9 00:30:26 2024
                                                                    
EEEEEEEEEEEEEEEEEEEE MMMMMMMM           MMMMMMMM RRRRRRRRRRRRRRR    
E::::::::::::::::::E M:::::::M         M:::::::M R::::::::::::::R   
EE:::::EEEEEEEEE:::E M::::::::M       M::::::::M R:::::RRRRRR:::::R 
  E::::E       EEEEE M:::::::::M     M:::::::::M RR::::R      R::::R
  E::::E             M::::::M:::M   M:::M::::::M   R:::R      R::::R
  E:::::EEEEEEEEEE   M:::::M M:::M M:::M M:::::M   R:::RRRRRR:::::R 
  E::::::::::::::E   M:::::M  M:::M:::M  M:::::M   R:::::::::::RR   
  E:::::EEEEEEEEEE   M:::::M   M:::::M   M:::::M   R:::RRRRRR::::R  
  E::::E             M:::::M    M:::M    M:::::M   R:::R      R::::R
  E::::E       EEEEE M:::::M     MMM     M:::::M   R:::R      R::::R
EE:::::EEEEEEEE::::E M:::::M             M:::::M   R:::R      R::::R
E::::::::::::::::::E M:::::M             M:::::M RR::::R      R::::R
EEEEEEEEEEEEEEEEEEEE MMMMMMM             MMMMMMM RRRRRRR      RRRRRR
                                                                    
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -mkdir /user/hadoop/datasets
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 00:36 /user/hadoop/datasets
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -mkdir /user/hadoop/datasets/onu
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 00:37 /user/hadoop/datasets
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -mkdir /user/hadoop/datasets/onu/hdi
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/hdi
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 00:41 /user/hadoop/datasets/onu/hdi
[hadoop@ip-172-31-2-89 ~]$ ^C
[hadoop@ip-172-31-2-89 ~]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
2024-10-23 19:38:39 bucket-por-gui
2024-10-22 22:32:30 datasetsb
2024-10-22 21:01:07 datasetsbucket
2024-10-22 20:08:30 mdcorreahnotebooks
[hadoop@ip-172-31-2-89 ~]$ aws s3 ls s3://datasetsb/datasets/onu
                           PRE onu/
[hadoop@ip-172-31-2-89 ~]$ aws s3 ls s3://datasetsb/datasets/onu/
                           PRE export/
                           PRE hdi/
2024-10-22 22:37:56       4423 export-data.csv
2024-10-22 22:37:56       9235 hdi-data.csv
2024-10-22 22:37:56        260 hdi-metadata.txt
[hadoop@ip-172-31-2-89 ~]$ hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/hdi-data.csv
2024-11-09 01:20:57,031 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2024-11-09 01:20:57,131 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 300 second(s).
2024-11-09 01:20:57,132 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
2024-11-09 01:20:57,592 WARN impl.ConfigurationHelper: Option fs.s3a.connection.establish.timeout is too low (5,000 ms). Setting to 15,000 ms instead
2024-11-09 01:21:00,627 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2024-11-09 01:21:00,627 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2024-11-09 01:21:00,627 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.
[hadoop@ip-172-31-2-89 ~]$ hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/export-data.csv
2024-11-09 01:21:22,095 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2024-11-09 01:21:22,200 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 300 second(s).
2024-11-09 01:21:22,200 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
2024-11-09 01:21:22,366 WARN impl.ConfigurationHelper: Option fs.s3a.connection.establish.timeout is too low (5,000 ms). Setting to 15,000 ms instead
2024-11-09 01:21:24,395 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2024-11-09 01:21:24,395 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2024-11-09 01:21:24,395 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/hdi
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 01:21 /user/hadoop/datasets/onu/hdi/export-data.csv
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 01:21 /user/hadoop/datasets/onu/hdi/hdi-data.csv

[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls 
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 00:37 datasets
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /
Found 4 items
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-11-08 23:53 /apps
drwxrwxrwt   - hdfs hdfsadmingroup          0 2024-11-08 23:55 /tmp
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-11-08 23:53 /user
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-11-08 23:53 /var
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /usr/
bin/     games/   include/ lib/     lib64/   libexec/ local/   sbin/    share/   src/     tmp/     
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user
Found 9 items
drwxrwxrwx   - hadoop   hdfsadmingroup          0 2024-11-09 00:36 /user/hadoop
drwxr-xr-x   - mapred   mapred                  0 2024-11-08 23:53 /user/history
drwxrwxrwx   - hdfs     hdfsadmingroup          0 2024-11-08 23:53 /user/hive
drwxrwxrwx   - hue      hue                     0 2024-11-09 00:17 /user/hue
drwxrwxrwx   - livy     livy                    0 2024-11-08 23:53 /user/livy
drwxrwxrwx   - oozie    oozie                   0 2024-11-08 23:54 /user/oozie
drwxrwxrwx   - root     hdfsadmingroup          0 2024-11-08 23:53 /user/root
drwxrwxrwx   - spark    spark                   0 2024-11-08 23:53 /user/spark
drwxrwxrwx   - zeppelin hdfsadmingroup          0 2024-11-08 23:53 /user/zeppelin
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hive
Found 1 items
drwxrwxrwt   - hdfs hdfsadmingroup          0 2024-11-09 02:00 /user/hive/warehouse
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hive/warehouse
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 02:00 /user/hive/warehouse/hdilabhive
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hive/warehouse/hdilabhive
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls hdfs:///user/hive/warehouse/
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 02:00 hdfs:///user/hive/warehouse/hdilabhive
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
put: `/user/hadoop/datasets/onu/hdi-data.csv': No such file or directory
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls hdfs:///user/hadoop/
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 00:37 hdfs:///user/hadoop/datasets
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls hdfs:///user/hadoop/datasets/onu
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-11-09 01:21 hdfs:///user/hadoop/datasets/onu/hdi
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls hdfs:///user/hadoop/datasets/onu/hdi
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 01:21 hdfs:///user/hadoop/datasets/onu/hdi/export-data.csv
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 01:21 hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
put: `/user/hadoop/datasets/onu/hdi/hdi-data.csv': No such file or directory
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive/
put: `/user/hadoop/datasets/onu/hdi/hdi-data.csv': No such file or directory
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -put /user/hadoop/datasets/onu/hdi/hdi-data.csv /user/hive/warehouse/hdilabhive/
put: `/user/hadoop/datasets/onu/hdi/hdi-data.csv': No such file or directory
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/hdi/hdi-data.csv
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 01:21 /user/hadoop/datasets/onu/hdi/hdi-data.csv
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hive/warehouse/hdilabhive/
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -cp hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
[hadoop@ip-172-31-2-89 ~]$ hdfs dfs -ls /user/hive/warehouse/hdilabhive/
Found 1 items
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 02:28 /user/hive/warehouse/hdilabhive/hdi-data.csv

[hadoop@ip-172-31-2-89 ~]$ beeline
Beeline version 3.1.3-amzn-13 by Apache Hive
beeline> !connect jdbc:hive2://localhost:10000

# Cuando hacemos esto, conectamos a hive2 en el host local y puerto 10000. Ahora necesitamos crear un usuario y contraseña.
# username: <<el-que-desees>>
# password: <<el-que-desees>>
Connecting to jdbc:hive2://localhost:10000
Enter username for jdbc:hive2://localhost:10000: mauricio
Enter password for jdbc:hive2://localhost:10000: ********
Connected to: Apache Hive (version 3.1.3-amzn-13)
Driver: Hive JDBC (version 3.1.3-amzn-13)
Transaction isolation: TRANSACTION_REPEATABLE_READ

# Comando para ver las bases de datos.
0: jdbc:hive2://localhost:10000> SHOW DATABASES;
INFO  : Compiling command(queryId=hive_20241109030236_760456b2-d90d-4915-a24c-86cff69d643f): SHOW DATABASES
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:database_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20241109030236_760456b2-d90d-4915-a24c-86cff69d643f); Time taken: 0.004 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109030236_760456b2-d90d-4915-a24c-86cff69d643f): SHOW DATABASES
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20241109030236_760456b2-d90d-4915-a24c-86cff69d643f); Time taken: 0.08 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
+----------------+
| database_name  |
+----------------+
| default        |
+----------------+
1 row selected (0.148 seconds)
0: jdbc:hive2://localhost:10000> 

# USAMOS LA BASE DE DATOS QUE REQUIRAMOS, EN ESTE CASO ES default.
0: jdbc:hive2://localhost:10000> USE default;
INFO  : Compiling command(queryId=hive_20241109030756_45213c81-047e-4cdf-8456-969f67507406): USE default
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20241109030756_45213c81-047e-4cdf-8456-969f67507406); Time taken: 0.104 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109030756_45213c81-047e-4cdf-8456-969f67507406): USE default
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20241109030756_45213c81-047e-4cdf-8456-969f67507406); Time taken: 0.176 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
No rows affected (0.293 seconds)

# CREAMOS UNA NUEVA TABLA LLAMADA 'hdilabhive2'
0: jdbc:hive2://localhost:10000> CREATE TABLE hdilabhive2 (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
. . . . . . . . . . . . . . . .> ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
. . . . . . . . . . . . . . . .> STORED AS TEXTFILE
. . . . . . . . . . . . . . . .> ;
INFO  : Compiling command(queryId=hive_20241109031043_5c520e1c-5643-4f84-98ce-844f1fbcf0b7): CREATE TABLE hdilabhive2 (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20241109031043_5c520e1c-5643-4f84-98ce-844f1fbcf0b7); Time taken: 0.099 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109031043_5c520e1c-5643-4f84-98ce-844f1fbcf0b7): CREATE TABLE hdilabhive2 (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20241109031043_5c520e1c-5643-4f84-98ce-844f1fbcf0b7); Time taken: 0.467 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
No rows affected (0.579 seconds)

# REVISAMOS LA CREACIÓN DE LAS TABLAS.
0: jdbc:hive2://localhost:10000> SHOW TABLES;
INFO  : Compiling command(queryId=hive_20241109031132_4bdc0172-3bb5-4010-adec-3351d678d941): SHOW TABLES
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20241109031132_4bdc0172-3bb5-4010-adec-3351d678d941); Time taken: 0.091 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109031132_4bdc0172-3bb5-4010-adec-3351d678d941): SHOW TABLES
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20241109031132_4bdc0172-3bb5-4010-adec-3351d678d941); Time taken: 0.207 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
+--------------+
|   tab_name   |
+--------------+
| hdilabhive2  |     --> AQUÍ LA PODEMOS VER CREADA :P
+--------------+
4 rows selected (0.316 seconds)



[hadoop@ip-172-31-12-155 ~]$ aws s3 ls s3://datasetsb/datasets/onu/
                           PRE export/
                           PRE hdi/
2024-10-22 22:37:56       4423 export-data.csv
2024-10-22 22:37:56       9235 hdi-data.csv
2024-10-22 22:37:56        260 hdi-metadata.txt
[hadoop@ip-172-31-12-155 ~]$ hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/hdi-data.csv
2024-11-09 04:04:56,751 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2024-11-09 04:04:56,853 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 300 second(s).
2024-11-09 04:04:56,853 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
2024-11-09 04:04:57,019 WARN impl.ConfigurationHelper: Option fs.s3a.connection.establish.timeout is too low (5,000 ms). Setting to 15,000 ms instead
2024-11-09 04:04:58,914 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2024-11-09 04:04:58,914 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2024-11-09 04:04:58,914 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.
[hadoop@ip-172-31-12-155 ~]$ hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/export-data.csv
2024-11-09 04:05:09,110 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2024-11-09 04:05:09,210 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 300 second(s).
2024-11-09 04:05:09,210 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
2024-11-09 04:05:09,360 WARN impl.ConfigurationHelper: Option fs.s3a.connection.establish.timeout is too low (5,000 ms). Setting to 15,000 ms instead
2024-11-09 04:05:11,123 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2024-11-09 04:05:11,123 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2024-11-09 04:05:11,123 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.
[hadoop@ip-172-31-12-155 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/hdi
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 04:05 /user/hadoop/datasets/onu/hdi/export-data.csv
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 04:04 /user/hadoop/datasets/onu/hdi/hdi-data.csv
[hadoop@ip-172-31-12-155 ~]$ hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive2
[hadoop@ip-172-31-12-155 ~]$ hdfs dfs -ls hdfs:///user/hadoop/datasets/onu/hdi/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 04:05 hdfs:///user/hadoop/datasets/onu/hdi/export-data.csv
-rw-r--r--   1 hadoop hdfsadmingroup       9235 2024-11-09 04:04 hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv


    [hadoop@ip-172-31-12-155 ~]$ beeline
    Beeline version 3.1.3-amzn-13 by Apache Hive
    beeline> !connect jdbc:hive2://localhost:10000
    Connecting to jdbc:hive2://localhost:10000
    Enter username for jdbc:hive2://localhost:10000: mauricio
    Enter password for jdbc:hive2://localhost:10000: *********
    Connected to: Apache Hive (version 3.1.3-amzn-13)
    Driver: Hive JDBC (version 3.1.3-amzn-13)
    Transaction isolation: TRANSACTION_REPEATABLE_READ
    0: jdbc:hive2://localhost:10000> SHOW TABLES;
    INFO  : Compiling command(queryId=hive_20241109043857_884ba883-36c8-43cd-bff0-cccf4c45d3ef): SHOW TABLES
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109043857_884ba883-36c8-43cd-bff0-cccf4c45d3ef); Time taken: 0.097 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109043857_884ba883-36c8-43cd-bff0-cccf4c45d3ef): SHOW TABLES
    INFO  : Starting task [Stage-0:DDL] in serial mode
    INFO  : Completed executing command(queryId=hive_20241109043857_884ba883-36c8-43cd-bff0-cccf4c45d3ef); Time taken: 0.21 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    +--------------+
    |   tab_name   |
    +--------------+
    | hdilabhive2  |
    +--------------+
    1 row selected (0.38 seconds)

    0: jdbc:hive2://localhost:10000> SELECT * FROM hdilabhive2 LIMIT 10;
    INFO  : Compiling command(queryId=hive_20241109043936_a893e396-aca5-4685-8735-971b33e2ca6e): SELECT * FROM hdilabhive2 LIMIT 10
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:hdilabhive2.id, type:int, comment:null), FieldSchema(name:hdilabhive2.country, type:string, comment:null), FieldSchema(name:hdilabhive2.hdi, type:float, comment:null), FieldSchema(name:hdilabhive2.lifeex, type:int, comment:null), FieldSchema(name:hdilabhive2.mysch, type:int, comment:null), FieldSchema(name:hdilabhive2.eysch, type:int, comment:null), FieldSchema(name:hdilabhive2.gni, type:int, comment:null)], properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109043936_a893e396-aca5-4685-8735-971b33e2ca6e); Time taken: 0.396 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109043936_a893e396-aca5-4685-8735-971b33e2ca6e): SELECT * FROM hdilabhive2 LIMIT 10
    INFO  : Completed executing command(queryId=hive_20241109043936_a893e396-aca5-4685-8735-971b33e2ca6e); Time taken: 0.002 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    +-----------------+----------------------+------------------+---------------------+--------------------+--------------------+------------------+
    | hdilabhive2.id  | hdilabhive2.country  | hdilabhive2.hdi  | hdilabhive2.lifeex  | hdilabhive2.mysch  | hdilabhive2.eysch  | hdilabhive2.gni  |
    +-----------------+----------------------+------------------+---------------------+--------------------+--------------------+------------------+
    | NULL            | country              | NULL             | NULL                | NULL               | NULL               | NULL             |
    | 1               | Norway               | 0.943            | 81                  | 12                 | 17                 | 47557            |
    | 2               | Australia            | 0.929            | 81                  | 12                 | 18                 | 34431            |
    | 3               | Netherlands          | 0.91             | 80                  | 11                 | 16                 | 36402            |
    | 4               | United States        | 0.91             | 78                  | 12                 | 16                 | 43017            |
    | 5               | New Zealand          | 0.908            | 80                  | 12                 | 18                 | 23737            |
    | 6               | Canada               | 0.908            | 81                  | 12                 | 16                 | 35166            |
    | 7               | Ireland              | 0.908            | 80                  | 11                 | 18                 | 29322            |
    | 8               | Liechtenstein        | 0.905            | 79                  | 10                 | 14                 | 83717            |
    | 9               | Germany              | 0.905            | 80                  | 12                 | 15                 | 34854            |
    +-----------------+----------------------+------------------+---------------------+--------------------+--------------------+------------------+
    10 rows selected (0.431 seconds)
    0: jdbc:hive2://localhost:10000> 

[hadoop@ip-172-31-12-155 ~]$ hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
    [hadoop@ip-172-31-12-155 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/
    Found 1 items
    drwxrwxrwx   - hadoop hdfsadmingroup          0 2024-11-09 04:05 /user/hadoop/datasets/onu/hdi
    [hadoop@ip-172-31-12-155 ~]$ hdfs dfs -ls /user/hadoop/datasets/onu/hdi
    Found 2 items
    -rwxrwxrwx   1 hadoop hdfsadmingroup       9235 2024-11-09 04:05 /user/hadoop/datasets/onu/hdi/export-data.csv
    -rwxrwxrwx   1 hadoop hdfsadmingroup       9235 2024-11-09 04:04 /user/hadoop/datasets/onu/hdi/hdi-data.csv
    [hadoop@ip-172-31-12-155 ~]$ $ beeline -u "jdbc:hive2://localhost:10000/default"
    -bash: $: command not found
    [hadoop@ip-172-31-12-155 ~]$ beeline -u "jdbc:hive2://localhost:10000/default"
    Connecting to jdbc:hive2://localhost:10000/default
    Connected to: Apache Hive (version 3.1.3-amzn-13)
    Driver: Hive JDBC (version 3.1.3-amzn-13)
    Transaction isolation: TRANSACTION_REPEATABLE_READ
    Beeline version 3.1.3-amzn-13 by Apache Hive
    0: jdbc:hive2://localhost:10000/default> CREATE TABLE exportdata (
    . . . . . . . . . . . . . . . . . . . .>     id INT,
    . . . . . . . . . . . . . . . . . . . .>     country STRING,
    . . . . . . . . . . . . . . . . . . . .>     hdi FLOAT,
    . . . . . . . . . . . . . . . . . . . .>     lifeex INT,
    . . . . . . . . . . . . . . . . . . . .>     myschool INT,
    . . . . . . . . . . . . . . . . . . . .>     eyschool INT,
    . . . . . . . . . . . . . . . . . . . .>     gni INT,
    . . . . . . . . . . . . . . . . . . . .>     gni2 INT,
    . . . . . . . . . . . . . . . . . . . .>     nihdi FLOAT
    . . . . . . . . . . . . . . . . . . . .> )
    . . . . . . . . . . . . . . . . . . . .> ROW FORMAT DELIMITED 
    . . . . . . . . . . . . . . . . . . . .> FIELDS TERMINATED BY ',' 
    . . . . . . . . . . . . . . . . . . . .> STORED AS TEXTFILE;
    INFO  : Compiling command(queryId=hive_20241109051750_92ac5616-270c-4f4e-a331-614f3e80cd07): CREATE TABLE exportdata (
    id INT,
    country STRING,
    hdi FLOAT,
    lifeex INT,
    myschool INT,
    eyschool INT,
    gni INT,
    gni2 INT,
    nihdi FLOAT
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109051750_92ac5616-270c-4f4e-a331-614f3e80cd07); Time taken: 0.098 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109051750_92ac5616-270c-4f4e-a331-614f3e80cd07): CREATE TABLE exportdata (
    id INT,
    country STRING,
    hdi FLOAT,
    lifeex INT,
    myschool INT,
    eyschool INT,
    gni INT,
    gni2 INT,
    nihdi FLOAT
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    INFO  : Starting task [Stage-0:DDL] in serial mode
    INFO  : Completed executing command(queryId=hive_20241109051750_92ac5616-270c-4f4e-a331-614f3e80cd07); Time taken: 0.418 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    No rows affected (0.555 seconds)
    0: jdbc:hive2://localhost:10000/default> SHOW TABLES;
    INFO  : Compiling command(queryId=hive_20241109051818_5eafda6e-2234-48a4-aa4e-70ffb35102b4): SHOW TABLES
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109051818_5eafda6e-2234-48a4-aa4e-70ffb35102b4); Time taken: 0.094 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109051818_5eafda6e-2234-48a4-aa4e-70ffb35102b4): SHOW TABLES
    INFO  : Starting task [Stage-0:DDL] in serial mode
    INFO  : Completed executing command(queryId=hive_20241109051818_5eafda6e-2234-48a4-aa4e-70ffb35102b4); Time taken: 0.235 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    +--------------+
    |   tab_name   |
    +--------------+
    | exportdata   |
    | hdilabhive2  |
    +--------------+
    2 rows selected (0.366 seconds)
    0: jdbc:hive2://localhost:10000/default> LOAD DATA INPATH '/user/hadoop/datasets/onu/hdi/export-data.csv' INTO TABLE exportdata;
    INFO  : Compiling command(queryId=hive_20241109051930_50ba1480-8357-4283-8f2e-bacf7d4c6680): LOAD DATA INPATH '/user/hadoop/datasets/onu/hdi/export-data.csv' INTO TABLE exportdata
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109051930_50ba1480-8357-4283-8f2e-bacf7d4c6680); Time taken: 0.146 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109051930_50ba1480-8357-4283-8f2e-bacf7d4c6680): LOAD DATA INPATH '/user/hadoop/datasets/onu/hdi/export-data.csv' INTO TABLE exportdata
    INFO  : Starting task [Stage-0:MOVE] in serial mode
    INFO  : Loading data to table default.exportdata from hdfs://ip-172-31-12-155.ec2.internal:8020/user/hadoop/datasets/onu/hdi/export-data.csv
    INFO  : Starting task [Stage-1:STATS] in serial mode
    INFO  : Executing stats task
    INFO  : Table default.exportdata stats: [numFiles=1, numRows=0, totalSize=9235, rawDataSize=0]
    INFO  : Completed executing command(queryId=hive_20241109051930_50ba1480-8357-4283-8f2e-bacf7d4c6680); Time taken: 1.257 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    No rows affected (1.415 seconds)
    0: jdbc:hive2://localhost:10000/default> SELECT * FROM exportdata LIMIT 10;
    INFO  : Compiling command(queryId=hive_20241109051950_281f514c-421f-484b-8d86-69ab8496c8c8): SELECT * FROM exportdata LIMIT 10
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Semantic Analysis Completed (retrial = false)
    INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:exportdata.id, type:int, comment:null), FieldSchema(name:exportdata.country, type:string, comment:null), FieldSchema(name:exportdata.hdi, type:float, comment:null), FieldSchema(name:exportdata.lifeex, type:int, comment:null), FieldSchema(name:exportdata.myschool, type:int, comment:null), FieldSchema(name:exportdata.eyschool, type:int, comment:null), FieldSchema(name:exportdata.gni, type:int, comment:null), FieldSchema(name:exportdata.gni2, type:int, comment:null), FieldSchema(name:exportdata.nihdi, type:float, comment:null)], properties:null)
    INFO  : Completed compiling command(queryId=hive_20241109051950_281f514c-421f-484b-8d86-69ab8496c8c8); Time taken: 0.337 seconds
    INFO  : Concurrency mode is disabled, not creating a lock manager
    INFO  : Executing command(queryId=hive_20241109051950_281f514c-421f-484b-8d86-69ab8496c8c8): SELECT * FROM exportdata LIMIT 10
    INFO  : Completed executing command(queryId=hive_20241109051950_281f514c-421f-484b-8d86-69ab8496c8c8); Time taken: 0.001 seconds
    INFO  : OK
    INFO  : Concurrency mode is disabled, not creating a lock manager
    +----------------+---------------------+-----------------+--------------------+----------------------+----------------------+-----------------+------------------+-------------------+
    | exportdata.id  | exportdata.country  | exportdata.hdi  | exportdata.lifeex  | exportdata.myschool  | exportdata.eyschool  | exportdata.gni  | exportdata.gni2  | exportdata.nihdi  |
    +----------------+---------------------+-----------------+--------------------+----------------------+----------------------+-----------------+------------------+-------------------+
    | NULL           | country             | NULL            | NULL               | NULL                 | NULL                 | NULL            | NULL             | NULL              |
    | 1              | Norway              | 0.943           | 81                 | 12                   | 17                   | 47557           | 6                | 0.975             |
    | 2              | Australia           | 0.929           | 81                 | 12                   | 18                   | 34431           | 16               | 0.979             |
    | 3              | Netherlands         | 0.91            | 80                 | 11                   | 16                   | 36402           | 9                | 0.944             |
    | 4              | United States       | 0.91            | 78                 | 12                   | 16                   | 43017           | 6                | 0.931             |
    | 5              | New Zealand         | 0.908           | 80                 | 12                   | 18                   | 23737           | 30               | 0.978             |
    | 6              | Canada              | 0.908           | 81                 | 12                   | 16                   | 35166           | 10               | 0.944             |
    | 7              | Ireland             | 0.908           | 80                 | 11                   | 18                   | 29322           | 19               | 0.959             |
    | 8              | Liechtenstein       | 0.905           | 79                 | 10                   | 14                   | 83717           | -6               | 0.877             |
    | 9              | Germany             | 0.905           | 80                 | 12                   | 15                   | 34854           | 8                | 0.94              |
    +----------------+---------------------+-----------------+--------------------+----------------------+----------------------+-----------------+------------------+-------------------+
    10 rows selected (0.37 seconds)
    0: jdbc:hive2://localhost:10000/default> Closing: 0: jdbc:hive2://localhost:10000/default




    [hadoop@ip-172-31-12-155 ~]$ beeline -u "jdbc:hive2://localhost:10000/default"
Connecting to jdbc:hive2://localhost:10000/default
Connected to: Apache Hive (version 3.1.3-amzn-13)
Driver: Hive JDBC (version 3.1.3-amzn-13)
Transaction isolation: TRANSACTION_REPEATABLE_READ
Beeline version 3.1.3-amzn-13 by Apache Hive
0: jdbc:hive2://localhost:10000/default> SELECT * FROM hdiextxgui LIMIT 10;
INFO  : Compiling command(queryId=hive_20241109061830_0347967c-9e76-46be-ad77-1fe711c605ee): SELECT * FROM hdiextxgui LIMIT 10
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:hdiextxgui.id, type:int, comment:null), FieldSchema(name:hdiextxgui.country, type:string, comment:null), FieldSchema(name:hdiextxgui.hdi, type:float, comment:null), FieldSchema(name:hdiextxgui.lifeex, type:int, comment:null), FieldSchema(name:hdiextxgui.mysch, type:int, comment:null), FieldSchema(name:hdiextxgui.eysch, type:int, comment:null), FieldSchema(name:hdiextxgui.gni, type:int, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20241109061830_0347967c-9e76-46be-ad77-1fe711c605ee); Time taken: 0.462 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109061830_0347967c-9e76-46be-ad77-1fe711c605ee): SELECT * FROM hdiextxgui LIMIT 10
INFO  : Completed executing command(queryId=hive_20241109061830_0347967c-9e76-46be-ad77-1fe711c605ee); Time taken: 0.001 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
+----------------+---------------------+-----------------+--------------------+-------------------+-------------------+-----------------+
| hdiextxgui.id  | hdiextxgui.country  | hdiextxgui.hdi  | hdiextxgui.lifeex  | hdiextxgui.mysch  | hdiextxgui.eysch  | hdiextxgui.gni  |
+----------------+---------------------+-----------------+--------------------+-------------------+-------------------+-----------------+
| NULL           | country             | NULL            | NULL               | NULL              | NULL              | NULL            |
| 1              | Norway              | 0.943           | 81                 | 12                | 17                | 47557           |
| 2              | Australia           | 0.929           | 81                 | 12                | 18                | 34431           |
| 3              | Netherlands         | 0.91            | 80                 | 11                | 16                | 36402           |
| 4              | United States       | 0.91            | 78                 | 12                | 16                | 43017           |
| 5              | New Zealand         | 0.908           | 80                 | 12                | 18                | 23737           |
| 6              | Canada              | 0.908           | 81                 | 12                | 16                | 35166           |
| 7              | Ireland             | 0.908           | 80                 | 11                | 18                | 29322           |
| 8              | Liechtenstein       | 0.905           | 79                 | 10                | 14                | 83717           |
| 9              | Germany             | 0.905           | 80                 | 12                | 15                | 34854           |
+----------------+---------------------+-----------------+--------------------+-------------------+-------------------+-----------------+
10 rows selected (0.55 seconds)
0: jdbc:hive2://localhost:10000/default> SELECT * FROM hdiextxbeeline LIMIT 10;
INFO  : Compiling command(queryId=hive_20241109061947_d7c6e298-4d31-43c5-8dac-88f47c428177): SELECT * FROM hdiextxbeeline LIMIT 10
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Semantic Analysis Completed (retrial = false)
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:hdiextxbeeline.id, type:int, comment:null), FieldSchema(name:hdiextxbeeline.country, type:string, comment:null), FieldSchema(name:hdiextxbeeline.hdi, type:float, comment:null), FieldSchema(name:hdiextxbeeline.lifeex, type:int, comment:null), FieldSchema(name:hdiextxbeeline.mysch, type:int, comment:null), FieldSchema(name:hdiextxbeeline.eysch, type:int, comment:null), FieldSchema(name:hdiextxbeeline.gni, type:int, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20241109061947_d7c6e298-4d31-43c5-8dac-88f47c428177); Time taken: 0.388 seconds
INFO  : Concurrency mode is disabled, not creating a lock manager
INFO  : Executing command(queryId=hive_20241109061947_d7c6e298-4d31-43c5-8dac-88f47c428177): SELECT * FROM hdiextxbeeline LIMIT 10
INFO  : Completed executing command(queryId=hive_20241109061947_d7c6e298-4d31-43c5-8dac-88f47c428177); Time taken: 0.001 seconds
INFO  : OK
INFO  : Concurrency mode is disabled, not creating a lock manager
+--------------------+-------------------------+---------------------+------------------------+-----------------------+-----------------------+---------------------+
| hdiextxbeeline.id  | hdiextxbeeline.country  | hdiextxbeeline.hdi  | hdiextxbeeline.lifeex  | hdiextxbeeline.mysch  | hdiextxbeeline.eysch  | hdiextxbeeline.gni  |
+--------------------+-------------------------+---------------------+------------------------+-----------------------+-----------------------+---------------------+
| NULL               | country                 | NULL                | NULL                   | NULL                  | NULL                  | NULL                |
| 1                  | Norway                  | 0.943               | 81                     | 12                    | 17                    | 47557               |
| 2                  | Australia               | 0.929               | 81                     | 12                    | 18                    | 34431               |
| 3                  | Netherlands             | 0.91                | 80                     | 11                    | 16                    | 36402               |
| 4                  | United States           | 0.91                | 78                     | 12                    | 16                    | 43017               |
| 5                  | New Zealand             | 0.908               | 80                     | 12                    | 18                    | 23737               |
| 6                  | Canada                  | 0.908               | 81                     | 12                    | 16                    | 35166               |
| 7                  | Ireland                 | 0.908               | 80                     | 11                    | 18                    | 29322               |
| 8                  | Liechtenstein           | 0.905               | 79                     | 10                    | 14                    | 83717               |
| 9                  | Germany                 | 0.905               | 80                     | 12                    | 15                    | 34854               |
+--------------------+-------------------------+---------------------+------------------------+-----------------------+-----------------------+---------------------+
10 rows selected (0.418 seconds)
0: jdbc:hive2://localhost:10000/default> Closing: 0: jdbc:hive2://localhost:10000/default





```