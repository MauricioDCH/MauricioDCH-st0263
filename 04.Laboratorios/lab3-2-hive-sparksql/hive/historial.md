# HISTORIAL DE COMANDOS REALIZADOS EN EL PRIMER CLUSTER.

```bash
# PRIMER PARTE ANTES DE TENER QUE TERMINAR EL CLUSTER.
[hadoop@ip-172-31-2-89 ~]$ history 
    1  hdfs dfs -ls /user/hadoop/
    2  hdfs dfs -mkdir /user/hadoop/datasets
    3  hdfs dfs -ls /user/hadoop/
    4  hdfs dfs -mkdir /user/hadoop/datasets/onu
    5  hdfs dfs -ls /user/hadoop/
    6  hdfs dfs -ls /user/hadoop/datasets/onu
    7  hdfs dfs -mkdir /user/hadoop/datasets/onu/hdi
    8  hdfs dfs -ls /user/hadoop/datasets/onu/hdi
    9  hdfs dfs -ls /user/hadoop/datasets/onu
   10  aws s3 ls
   11  aws s3 ls s3://datasetsb/datasets/onu
   12  aws s3 ls s3://datasetsb/datasets/onu/
   13  hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/hdi-data.csv
   14  hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/export-data.csv
   15  hdfs dfs -ls /user/hadoop/datasets/onu/hdi
   16  hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi-data.csv hdfs:///user/hive/warehouse/usernamedb.db/hdi
   17  beeline
   18  exit
   19  hdfs dfs -ls 
   20  hdfs dfs -ls /
   21  hdfs dfs -ls /user
   22  hdfs dfs -ls /user/hive
   23  hdfs dfs -ls /user/hive/warehouse
   24  hdfs dfs -ls /user/hive/warehouse/hdilabhive
   25  hdfs dfs -ls hdfs:///user/hive/warehouse/
   26  hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
   27  hdfs dfs -ls hdfs:///user/hadoop/
   28  hdfs dfs -ls hdfs:///user/hadoop/datasets/onu
   29  hdfs dfs -ls hdfs:///user/hadoop/datasets/onu/hdi
   30  hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
   31  hdfs dfs -put hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive/
   32  hdfs dfs -put /user/hadoop/datasets/onu/hdi/hdi-data.csv /user/hive/warehouse/hdilabhive/
   33  hdfs dfs -ls /user/hadoop/datasets/onu/hdi/hdi-data.csv
   34  hdfs dfs -ls /user/hive/warehouse/hdilabhive/
   35  hdfs dfs -cp hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive
   36  hdfs dfs -ls /user/hive/warehouse/hdilabhive/
   37  clear
   38  hdfs dfs -ls /user/hive/warehouse/hdilabhive
   39  hdfs dfs -ls hdfs:///user/hive/warehouse/
   40  clear
   41  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive
   42  hdfs dfs -rm hdfs:///user/hive/warehouse/hdilabhive
   43  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive
   44  hdfs dfs -rm hdfs:///user/hive/warehouse/hdilabhive/hdi-data.csv
   45  clear
   46  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive
   47  clear
   48  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive
   49  hdfs dfs -ls hdfs:///user/hadoop/datasets/onu
   50  clear
   51  beeline
   52  clear
   53  history 
```
```bash
# SEGUNDA PARTE ANTES DE TENER QUE TERMINAR EL CLUSTER.
    1  clear
    2  beeline
    3  clear
    4  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive2
    5  hdfs dfs -mkdir /user/hadoop/datasets
    6  hdfs dfs -mkdir /user/hadoop/datasets/onu
    7  hdfs dfs -mkdir /user/hadoop/datasets/onu/hdi
    8  hdfs dfs -ls /user/hadoop/datasets/onu/hdi
    9  hdfs dfs -ls /user/hadoop/datasets/onu
   10  aws s3 ls s3://datasetsb/datasets/onu/
   11  hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/hdi-data.csv
   12  hadoop fs -cp s3a://datasetsb/datasets/onu/hdi-data.csv  /user/hadoop/datasets/onu/hdi/export-data.csv
   13  hdfs dfs -ls /user/hadoop/datasets/onu/hdi
   14  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive2
   15  hdfs dfs -ls hdfs:///user/hadoop/datasets/onu/hdi/
   16  hdfs dfs -cp hdfs:///user/hadoop/datasets/onu/hdi/hdi-data.csv hdfs:///user/hive/warehouse/hdilabhive2/hdi-data.csv
   17  hdfs dfs -ls hdfs:///user/hive/warehouse/hdilabhive2
   18  clear
   19  beeline
   20  clear
   21  history 
   22  clear
   23  hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
   24  beeline -u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000"
   25  ping sandbox-hdp.hortonworks.com
   26  beeline -u "jdbc:hive2://sandbox-hdp.hortonworks.com:2"
   27  clear
   28  hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
   29  ping sandbox.hortonworks.com
   30  beeline -u "jdbc:hive2://sandbox.hortonworks.com:10000/default" -n tu_usuario -p tu_contraseña
   31  clear
   32  $ hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
   33  clear
   34  hdfs dfs -chmod -R 777 /user/hadoop/datasets/onu/
   35  hdfs dfs -ls /user/hadoop/datasets/onu/
   36  hdfs dfs -ls /user/hadoop/datasets/onu/hdi
   37  $ beeline -u "jdbc:hive2://localhost:10000/default"
   38  beeline -u "jdbc:hive2://localhost:10000/default"
   39  clear
   40  history 

```