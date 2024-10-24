```bash
mdch@mdch-X532FLC-S532FL:~/Documents/01._Ingeniería_de_Sistemas-EAFIT/04._SEM/06._S6-2024.02/04.Top_Telem/04-ACTIVIDADES/04.Laboratorios/01.Primer_Laboratorio$ ssh -i "laboratorio-3.pem" hadoop@ec2-3-234-143-224.compute-1.amazonaws.com

A newer release of "Amazon Linux" is available.
  Version 2023.6.20241010:
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
Last login: Tue Oct 22 20:47:12 2024
                                                                    
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
                                                                    
[hadoop@ip-172-31-10-177 ~]$ aws --version
aws-cli/2.15.30 Python/3.9.16 Linux/6.1.109-118.189.amzn2023.x86_64 source/x86_64.amzn.2023 prompt/off
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
2024-10-22 20:08:30 mdcorreahnotebooks
[hadoop@ip-172-31-10-177 ~]$ aws s3api create-bucket --bucket datasetsbucket --region us-east-1
{
    "Location": "/datasetsbucket"
}
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
2024-10-22 21:01:07 datasetsbucket
2024-10-22 20:08:30 mdcorreahnotebooks
[hadoop@ip-172-31-10-177 ~]$ aws s3api put-object --bucket datasetsbucket --key nueva_carpeta_por_comandos/
{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
    "ServerSideEncryption": "AES256"
}
[hadoop@ip-172-31-10-177 ~]$ aws s3 ls s3://datasetsbucket/
                           PRE nueva_carpeta_por_comandos/
[hadoop@ip-172-31-10-177 ~]$ touch emptyfile.txt
aws s3 cp emptyfile.txt s3://datasetsbucket/nueva_carpeta_por_comandos/
upload: ./emptyfile.txt to s3://datasetsbucket/nueva_carpeta_por_comandos/emptyfile.txt
[hadoop@ip-172-31-10-177 root]$ aws s3 ls s3://datasetsbucket/nueva_carpeta_por_comandos/
2024-10-22 21:43:46          0 
2024-10-22 21:48:26          0 emptyfile.txt
[hadoop@ip-172-31-10-177 root]$ sudo aws s3 cp s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt /home/hadoop/para_s3/
download: s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt to ../home/hadoop/para_s3/otroArchivo.txt
[hadoop@ip-172-31-10-177 root]$ aws s3 cp s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt -
Este es un archivo creado desde GUI en S3
[hadoop@ip-172-31-10-177 root]$ aws s3api create-bucket --bucket otrodatasetsbucket --region us-east-1
{
    "Location": "/otrodatasetsbucket"
}
[hadoop@ip-172-31-10-177 root]$ aws s3 mv s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt s3://otrodatasetsbucket/ejemplo.txt
move: s3://datasetsbucket/nueva_carpeta_por_comandos/otroArchivo.txt to s3://otrodatasetsbucket/ejemplo.txt
[hadoop@ip-172-31-10-177 root]$ hadoop fs -cp /user/hadoop/ s3a://datasetsbucket/
[hadoop@ip-172-31-10-177 root]$ aws s3api create-bucket --bucket datasetsb --region us-east-1
[hadoop@ip-172-31-10-177 root]$ aws s3 cp /home/hadoop/st0263-242/bigdata/datasets/ s3://datasetsb/datasets --recursive
upload: ../home/hadoop/st0263-242/bigdata/datasets/all-news/url.txt to s3://datasetsb/datasets/all-news/url.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___LincolnsSecondInauguralAddress.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsSecondInauguralAddress.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___LincolnLetters.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnLetters.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-1K.csv to s3://datasetsb/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-1K.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___LincolnsFirstInauguralAddress.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsFirstInauguralAddress.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/airlines.csv to s3://datasetsb/datasets/airlines.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___StateoftheUnionAddresses.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___StateoftheUnionAddresses.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheEmancipationProclamation.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheEmancipationProclamation.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg/gutenberg-txt-es.zip-url.txt to s3://datasetsb/datasets/gutenberg/gutenberg-txt-es.zip-url.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt to s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/onu/export-data.csv to s3://datasetsb/datasets/onu/export-data.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/gutenberg/gutenberg-small-es.zip to s3://datasetsb/datasets/gutenberg/gutenberg-small-es.zip
upload: ../home/hadoop/st0263-242/bigdata/datasets/onu/hdi-data.csv to s3://datasetsb/datasets/onu/hdi-data.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/onu/export/export-data.csv to s3://datasetsb/datasets/onu/export/export-data.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/onu/hdi-metadata.txt to s3://datasetsb/datasets/onu/hdi-metadata.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/onu/hdi/hdi-data2.csv to s3://datasetsb/datasets/onu/hdi/hdi-data2.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/dataempleados.csv to s3://datasetsb/datasets/otros/dataempleados.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/dataempleados.txt to s3://datasetsb/datasets/otros/dataempleados.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/dataempresas.csv to s3://datasetsb/datasets/otros/dataempresas.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/dataempresas.txt to s3://datasetsb/datasets/otros/dataempresas.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/datapeliculas.csv to s3://datasetsb/datasets/otros/datapeliculas.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/sample_data.csv to s3://datasetsb/datasets/sample_data.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/otros/datapeliculas.txt to s3://datasetsb/datasets/otros/datapeliculas.txt
upload: ../home/hadoop/st0263-242/bigdata/datasets/spark/movie_reviews.csv to s3://datasetsb/datasets/spark/movie_reviews.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-100K.csv to s3://datasetsb/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-100K.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/spark/sample_data.csv to s3://datasetsb/datasets/spark/sample_data.csv
upload: ../home/hadoop/st0263-242/bigdata/datasets/retail_logs/access.log.zip to s3://datasetsb/datasets/retail_logs/access.log.zip
upload: ../home/hadoop/st0263-242/bigdata/datasets/spark/online-retail-dataset.csv.zip to s3://datasetsb/datasets/spark/online-retail-dataset.csv.zip
upload: ../home/hadoop/st0263-242/bigdata/datasets/flights/departuredelays.csv to s3://datasetsb/datasets/flights/departuredelays.csv
[hadoop@ip-172-31-10-177 root]$ sudo mkdir -p ~/datasets_local
[hadoop@ip-172-31-10-177 root]$ sudo ls
[hadoop@ip-172-31-10-177 root]$ sudo ls ~/datasets_local
[hadoop@ip-172-31-10-177 root]$ sudo ls ~/
[hadoop@ip-172-31-10-177 root]$ sudo aws s3 cp s3://datasetsb/datasets/ ~/datasets_local/ --recursive
download: s3://datasetsb/datasets/all-news/url.txt to ../home/hadoop/datasets_local/all-news/url.txt
download: s3://datasetsb/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-1K.csv to ../home/hadoop/datasets_local/covid19/Casos_positivos_de_COVID-19_en_Colombia-1K.csv
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsFirstInauguralAddress.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___LincolnsFirstInauguralAddress.txt
download: s3://datasetsb/datasets/airlines.csv to ../home/hadoop/datasets_local/airlines.csv
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsSecondInauguralAddress.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___LincolnsSecondInauguralAddress.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnLetters.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___LincolnLetters.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheEmancipationProclamation.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheEmancipationProclamation.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___StateoftheUnionAddresses.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___StateoftheUnionAddresses.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
download: s3://datasetsb/datasets/gutenberg/gutenberg-txt-es.zip-url.txt to ../home/hadoop/datasets_local/gutenberg/gutenberg-txt-es.zip-url.txt
download: s3://datasetsb/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt to ../home/hadoop/datasets_local/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
download: s3://datasetsb/datasets/onu/export-data.csv to ../home/hadoop/datasets_local/onu/export-data.csv
download: s3://datasetsb/datasets/onu/export/export-data.csv to ../home/hadoop/datasets_local/onu/export/export-data.csv
download: s3://datasetsb/datasets/otros/dataempleados.csv to ../home/hadoop/datasets_local/otros/dataempleados.csv
download: s3://datasetsb/datasets/onu/hdi/hdi-data2.csv to ../home/hadoop/datasets_local/onu/hdi/hdi-data2.csv
download: s3://datasetsb/datasets/onu/hdi-metadata.txt to ../home/hadoop/datasets_local/onu/hdi-metadata.txt
download: s3://datasetsb/datasets/otros/dataempleados.txt to ../home/hadoop/datasets_local/otros/dataempleados.txt
download: s3://datasetsb/datasets/otros/dataempresas.csv to ../home/hadoop/datasets_local/otros/dataempresas.csv
download: s3://datasetsb/datasets/otros/dataempresas.txt to ../home/hadoop/datasets_local/otros/dataempresas.txt
download: s3://datasetsb/datasets/onu/hdi-data.csv to ../home/hadoop/datasets_local/onu/hdi-data.csv
download: s3://datasetsb/datasets/otros/datapeliculas.csv to ../home/hadoop/datasets_local/otros/datapeliculas.csv
download: s3://datasetsb/datasets/otros/datapeliculas.txt to ../home/hadoop/datasets_local/otros/datapeliculas.txt
download: s3://datasetsb/datasets/covid19/Casos_positivos_de_COVID-19_en_Colombia-100K.csv to ../home/hadoop/datasets_local/covid19/Casos_positivos_de_COVID-19_en_Colombia-100K.csv
download: s3://datasetsb/datasets/spark/sample_data.csv to ../home/hadoop/datasets_local/spark/sample_data.csv
download: s3://datasetsb/datasets/sample_data.csv to ../home/hadoop/datasets_local/sample_data.csv
download: s3://datasetsb/datasets/gutenberg/gutenberg-small-es.zip to ../home/hadoop/datasets_local/gutenberg/gutenberg-small-es.zip
download: s3://datasetsb/datasets/spark/movie_reviews.csv to ../home/hadoop/datasets_local/spark/movie_reviews.csv
download: s3://datasetsb/datasets/flights/departuredelays.csv to ../home/hadoop/datasets_local/flights/departuredelays.csv
download: s3://datasetsb/datasets/retail_logs/access.log.zip to ../home/hadoop/datasets_local/retail_logs/access.log.zip
download: s3://datasetsb/datasets/spark/online-retail-dataset.csv.zip to ../home/hadoop/datasets_local/spark/online-retail-dataset.csv.zip
[hadoop@ip-172-31-10-177 root]$ hadoop fs -mkdir -p /user/hadoop/datasets_hadoop
[hadoop@ip-172-31-10-177 root]$ hadoop fs -cp s3a://datasetsb/datasets/ /user/hadoop/datasets_hadoop/
2024-10-22 22:45:42,327 INFO impl.MetricsConfig: Loaded properties from hadoop-metrics2.properties
2024-10-22 22:45:42,437 INFO impl.MetricsSystemImpl: Scheduled Metric snapshot period at 300 second(s).
2024-10-22 22:45:42,437 INFO impl.MetricsSystemImpl: s3a-file-system metrics system started
2024-10-22 22:45:43,534 WARN s3.S3TransferManager: The provided S3AsyncClient is an instance of MultipartS3AsyncClient, and thus multipart download feature is not enabled. To benefit from all features, consider using S3AsyncClient.crtBuilder().build() instead.
2024-10-22 22:45:52,592 INFO impl.MetricsSystemImpl: Stopping s3a-file-system metrics system...
2024-10-22 22:45:52,593 INFO impl.MetricsSystemImpl: s3a-file-system metrics system stopped.
2024-10-22 22:45:52,593 INFO impl.MetricsSystemImpl: s3a-file-system metrics system shutdown complete.


[hadoop@ip-172-31-9-11 root]$ sudo ls
[hadoop@ip-172-31-9-11 root]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
2024-10-22 22:32:30 datasetsb
2024-10-22 21:01:07 datasetsbucket
2024-10-22 20:08:30 mdcorreahnotebooks
2024-10-22 22:16:08 otrodatasetsbucket
[hadoop@ip-172-31-9-11 root]$ aws s3api delete-bucket --bucket otrodatasetsbucket --region us-east-1

An error occurred (BucketNotEmpty) when calling the DeleteBucket operation: The bucket you tried to delete is not empty
[hadoop@ip-172-31-9-11 root]$ aws s3 rm s3://otrodatasetsbucket/ejemplo.txt
delete: s3://otrodatasetsbucket/ejemplo.txt
[hadoop@ip-172-31-9-11 root]$ aws s3 ls aws s3 ls s3://otrodatasetsbucket/

Unknown options: s3,ls,s3://otrodatasetsbucket/
[hadoop@ip-172-31-9-11 root]$ aws s3 ls s3://otrodatasetsbucket/
[hadoop@ip-172-31-9-11 root]$ aws s3api delete-bucket --bucket otrodatasetsbucket --region us-east-1
[hadoop@ip-172-31-9-11 root]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
2024-10-22 22:32:30 datasetsb
2024-10-22 21:01:07 datasetsbucket
2024-10-22 20:08:30 mdcorreahnotebooks

[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket datasetsbucket
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": false,
        "IgnorePublicAcls": false,
        "BlockPublicPolicy": false,
        "RestrictPublicBuckets": false
    }
}
[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket datasetsb
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
    }
}
[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket datasetsb --public-access-block-configuration '{
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
}'

usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: --public-access-block-configuration, {
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
}

[hadoop@ip-172-31-9-11 root]$ aws s3api put-public-access-block --bucket datasetsb --public-access-block-configuration '{
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
}'
[hadoop@ip-172-31-9-11 root]$ aws s3api put-public-access-block --bucket mdcorreahnotebooks --public-access-block-configuration '{
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
}'
[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket datasetsb
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": false,
        "IgnorePublicAcls": false,
        "BlockPublicPolicy": false,
        "RestrictPublicBuckets": false
    }
}
[hadoop@ip-172-31-9-11 root]$ aws s3api get-public-access-block --bucket mdcorreahnotebooks
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": false,
        "IgnorePublicAcls": false,
        "BlockPublicPolicy": false,
        "RestrictPublicBuckets": false
    }
}

[hadoop@ip-172-31-9-11 root]$ aws s3 cp s3://datasetsb/datasets/spark/movie_reviews.csv s3://datasetsbucket/nueva_carpeta_por_comandos/movie_reviews.csv
copy: s3://datasetsb/datasets/spark/movie_reviews.csv to s3://datasetsbucket/nueva_carpeta_por_comandos/movie_reviews.csv

```