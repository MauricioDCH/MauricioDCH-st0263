# COMANDOS REALIZADOS EN EL SISTEMA HADOOP.

## COMO ROOT.
```bash
ls
ls /
ls /home/
ls /home/
ls /home/
sudo su hadoop
```

# COMO HADOOP.
```bash
sudo ls
sudo yum install git
sudo git clone https://github.com/st0263eafit/st0263-242.git
sudo ls
hdfs dfs -ls /
hdfs dfs -ls /user
hdfs dfs -ls /user/hadoop
hdfs dfs -mkdir /user/hadoop/datasets
hdfs dfs -mkdir /user/hadoop/datasets
hdfs dfs -ls /user/hadoop/datasets
hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
hdfs dfs -ls /user/hadoop/datasets
hdfs dfs -ls /user/hadoop/datasets/gutenberg-small
sudo ls /home/hadoop/.
sudo ls /home/hadoop/
sudo ls
sudo ls /root/
sudo mv /root/st0263-242/ /home/hadoop/
sudo ls /root/
sudo ls /home/hadoop/
sudo ls /home//hadoop//st0263-242/bigdata/datasets/gutenberg-small/
sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/
hdfs dfs -ls /user/hadoop/datasets/gutenberg-small/
hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/*.txt /user/hadoop/datasets/gutenberg-small/
hdfs dfs -ls /user/hadoop/datasets/gutenberg-small/
sudo ls /home/hadoop/
sudo mkdir /home/hadoop/mis_datasets/
sudo ls /home/hadoop/
sudo hdfs dfs -get /user/hadoop/datasets/gutenberg-small/* ~hadoop/mis_datasets/
sudo ls ~hadoop/mis_datasets/
hdfs dfs -mkdir /user/hadoop/datasets/gutenberg/
sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg/
hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg/* /user/hadoop/datasets/gutenberg/
hdfs dfs -ls /user/hadoop/datasets/gutenberg/
sudo hdfs dfs -copyToLocal /user/hadoop/datasets/gutenberg/gutenberg-small-es.zip ~hadoop/mis_datasets/
sudo ls ~hadoop/mis_datasets/
hdfs dfs -du /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
hdfs dfs -mkdir /user/hadoop/datasets/toMove
hdfs dfs -mv /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt /user/hadoop/datasets/toMove/
hdfs dfs -ls /user/hadoop/datasets/toMove/
hdfs dfs -cp /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt /user/hadoop/datasets/toMove/
hdfs dfs -ls /user/hadoop/datasets/toMove/
hdfs dfs -rm /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
hdfs dfs -ls /user/hadoop/datasets/toMove/
hdfs dfs -cat /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
hdfs dfs -touchz /user/hadoop/datasets/toMove/prueba_para_chmod.txt
hdfs dfs -ls /user/hadoop/datasets/toMove/
hdfs dfs -chmod 644 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
hdfs dfs -ls /user/hadoop/datasets/toMove/
hdfs dfs -chmod 600 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
hdfs dfs -ls /user/hadoop/datasets/toMove/
```
