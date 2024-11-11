```bash
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
                                                                    
[root@ip-172-31-15-140 ~]# ls
[root@ip-172-31-15-140 ~]# ls /
apppusher-group/ cgroup.procs     emr/             lib/             media/           mnt/             proc/            sbin/            tmp/             
bin/             cpu.max          etc/             lib64/           memory.max       mnt1/            root/            srv/             usr/             
boot/            dev/             home/            local/           memory.swap.max  opt/             run/             sys/             var/             
[root@ip-172-31-15-140 ~]# ls /home/
ec2-user/     emr-notebook/ hadoop/       puppet/       
[root@ip-172-31-15-140 ~]# ls /home/
ec2-user/     emr-notebook/ hadoop/       puppet/       
[root@ip-172-31-15-140 ~]# ls /home/
ec2-user  emr-notebook  hadoop  puppet
[root@ip-172-31-15-140 ~]# sudo su hadoop
                                                                    
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
                                                                    
[hadoop@ip-172-31-15-140 root]$ sudo ls
[hadoop@ip-172-31-15-140 root]$ sudo yum install git
Last metadata expiration check: 0:30:39 ago on Tue Oct 22 03:28:57 2024.
Dependencies resolved.
=====================================================================================================================================================================================================================================
 Package                                                  Architecture                                   Version                                                           Repository                                           Size
=====================================================================================================================================================================================================================================
Installing:
 git                                                      x86_64                                         2.40.1-1.amzn2023.0.3                                             amazonlinux                                          54 k
Installing dependencies:
 git-core                                                 x86_64                                         2.40.1-1.amzn2023.0.3                                             amazonlinux                                         4.3 M
 git-core-doc                                             noarch                                         2.40.1-1.amzn2023.0.3                                             amazonlinux                                         2.6 M
 perl-Error                                               noarch                                         1:0.17029-5.amzn2023.0.2                                          amazonlinux                                          41 k
 perl-Git                                                 noarch                                         2.40.1-1.amzn2023.0.3                                             amazonlinux                                          42 k
 perl-TermReadKey                                         x86_64                                         2.38-9.amzn2023.0.2                                               amazonlinux                                          36 k
 perl-lib                                                 x86_64                                         0.65-477.amzn2023.0.6                                             amazonlinux                                          15 k

Transaction Summary
=====================================================================================================================================================================================================================================
Install  7 Packages

Total download size: 7.1 M
Installed size: 34 M
Is this ok [y/N]: y
Downloading Packages:
(1/7): git-2.40.1-1.amzn2023.0.3.x86_64.rpm                                                                                                                                                          897 kB/s |  54 kB     00:00    
(2/7): perl-Error-0.17029-5.amzn2023.0.2.noarch.rpm                                                                                                                                                  1.6 MB/s |  41 kB     00:00    
(3/7): git-core-doc-2.40.1-1.amzn2023.0.3.noarch.rpm                                                                                                                                                  24 MB/s | 2.6 MB     00:00    
(4/7): perl-Git-2.40.1-1.amzn2023.0.3.noarch.rpm                                                                                                                                                     1.7 MB/s |  42 kB     00:00    
(5/7): git-core-2.40.1-1.amzn2023.0.3.x86_64.rpm                                                                                                                                                      29 MB/s | 4.3 MB     00:00    
(6/7): perl-TermReadKey-2.38-9.amzn2023.0.2.x86_64.rpm                                                                                                                                               938 kB/s |  36 kB     00:00    
(7/7): perl-lib-0.65-477.amzn2023.0.6.x86_64.rpm                                                                                                                                                     409 kB/s |  15 kB     00:00    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                                                                                                 34 MB/s | 7.1 MB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                                                                                             1/1 
  Installing       : git-core-2.40.1-1.amzn2023.0.3.x86_64                                                                                                                                                                       1/7 
  Installing       : git-core-doc-2.40.1-1.amzn2023.0.3.noarch                                                                                                                                                                   2/7 
  Installing       : perl-lib-0.65-477.amzn2023.0.6.x86_64                                                                                                                                                                       3/7 
  Installing       : perl-TermReadKey-2.38-9.amzn2023.0.2.x86_64                                                                                                                                                                 4/7 
  Installing       : perl-Error-1:0.17029-5.amzn2023.0.2.noarch                                                                                                                                                                  5/7 
  Installing       : perl-Git-2.40.1-1.amzn2023.0.3.noarch                                                                                                                                                                       6/7 
  Installing       : git-2.40.1-1.amzn2023.0.3.x86_64                                                                                                                                                                            7/7 
  Running scriptlet: git-2.40.1-1.amzn2023.0.3.x86_64                                                                                                                                                                            7/7 
  Verifying        : git-2.40.1-1.amzn2023.0.3.x86_64                                                                                                                                                                            1/7 
  Verifying        : git-core-2.40.1-1.amzn2023.0.3.x86_64                                                                                                                                                                       2/7 
  Verifying        : git-core-doc-2.40.1-1.amzn2023.0.3.noarch                                                                                                                                                                   3/7 
  Verifying        : perl-Error-1:0.17029-5.amzn2023.0.2.noarch                                                                                                                                                                  4/7 
  Verifying        : perl-Git-2.40.1-1.amzn2023.0.3.noarch                                                                                                                                                                       5/7 
  Verifying        : perl-TermReadKey-2.38-9.amzn2023.0.2.x86_64                                                                                                                                                                 6/7 
  Verifying        : perl-lib-0.65-477.amzn2023.0.6.x86_64                                                                                                                                                                       7/7 
=====================================================================================================================================================================================================================================
WARNING:
  A newer release of "Amazon Linux" is available.

  Available Versions:

  Version 2023.6.20241010:
    Run the following command to upgrade to 2023.6.20241010:

      dnf upgrade --releasever=2023.6.20241010

    Release notes:
     https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20241010.html

=====================================================================================================================================================================================================================================

Installed:
  git-2.40.1-1.amzn2023.0.3.x86_64                git-core-2.40.1-1.amzn2023.0.3.x86_64     git-core-doc-2.40.1-1.amzn2023.0.3.noarch     perl-Error-1:0.17029-5.amzn2023.0.2.noarch     perl-Git-2.40.1-1.amzn2023.0.3.noarch    
  perl-TermReadKey-2.38-9.amzn2023.0.2.x86_64     perl-lib-0.65-477.amzn2023.0.6.x86_64    

Complete!
[hadoop@ip-172-31-15-140 root]$ sudo git clone https://github.com/st0263eafit/st0263-242.git
Cloning into 'st0263-242'...
remote: Enumerating objects: 1194, done.
remote: Counting objects: 100% (1194/1194), done.
remote: Compressing objects: 100% (922/922), done.
remote: Total 1194 (delta 222), reused 1192 (delta 220), pack-reused 0 (from 0)
Receiving objects: 100% (1194/1194), 30.97 MiB | 28.21 MiB/s, done.
Resolving deltas: 100% (222/222), done.
[hadoop@ip-172-31-15-140 root]$ sudo ls
st0263-242
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /
Found 4 items
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-10-22 03:40 /apps
drwxrwxrwt   - hdfs hdfsadmingroup          0 2024-10-22 03:42 /tmp
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-10-22 03:40 /user
drwxr-xr-x   - hdfs hdfsadmingroup          0 2024-10-22 03:40 /var
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user
Found 9 items
drwxrwxrwx   - hadoop   hdfsadmingroup          0 2024-10-22 03:40 /user/hadoop
drwxr-xr-x   - mapred   mapred                  0 2024-10-22 03:40 /user/history
drwxrwxrwx   - hdfs     hdfsadmingroup          0 2024-10-22 03:40 /user/hive
drwxrwxrwx   - hue      hue                     0 2024-10-22 03:40 /user/hue
drwxrwxrwx   - livy     livy                    0 2024-10-22 03:40 /user/livy
drwxrwxrwx   - oozie    oozie                   0 2024-10-22 03:40 /user/oozie
drwxrwxrwx   - root     hdfsadmingroup          0 2024-10-22 03:40 /user/root
drwxrwxrwx   - spark    spark                   0 2024-10-22 03:40 /user/spark
drwxrwxrwx   - zeppelin hdfsadmingroup          0 2024-10-22 03:40 /user/zeppelin
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets
mkdir: `/user/hadoop/datasets': File exists
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets
Found 1 items
drwxr-xr-x   - hadoop hdfsadmingroup          0 2024-10-22 04:02 /user/hadoop/datasets/gutenberg-small
[hadoop@ip-172-31-15-140 root]$ ^C
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg-small
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/.
./             ../            .aws/          .bash_profile  .bashrc        .config/       .ssh/          
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
[hadoop@ip-172-31-15-140 root]$ sudo ls
st0263-242
[hadoop@ip-172-31-15-140 root]$ sudo ls /root/
st0263-242
[hadoop@ip-172-31-15-140 root]$ ^C
[hadoop@ip-172-31-15-140 root]$ sudo mv /root/st0263-242/ /home/hadoop/
[hadoop@ip-172-31-15-140 root]$ sudo ls /root/
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
st0263-242
[hadoop@ip-172-31-15-140 root]$ sudo ls /home//hadoop//st0263-242/bigdata/datasets/gutenberg-small/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg-small/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg-small/*.txt /user/hadoop/datasets/gutenberg-small/
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
[hadoop@ip-172-31-15-140 root]$ hadoop distcp s3://st0263datasets/datasets/airlines.csv /tmp/

2024-10-22 04:23:57,654 INFO tools.DistCp: Input Options: DistCpOptions{atomicCommit=false, syncFolder=false, deleteMissing=false, ignoreFailures=false, overwrite=false, append=false, useDiff=false, useRdiff=false, fromSnapshot=null, toSnapshot=null, skipCRC=false, blocking=true, numListstatusThreads=0, maxMaps=20, mapBandwidth=0.0, copyStrategy='uniformsize', preserveStatus=[], atomicWorkPath=null, logPath=null, sourceFileListing=null, sourcePaths=[s3://st0263datasets/datasets/airlines.csv], targetPath=/tmp, filtersFile='null', blocksPerChunk=0, copyBufferSize=8192, verboseLog=false, directWrite=false, useiterator=false}, sourcePaths=[s3://st0263datasets/datasets/airlines.csv], targetPathExists=true, preserveRawXattrs=false
2024-10-22 04:23:57,886 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at ip-172-31-15-140.ec2.internal/172.31.15.140:8032
2024-10-22 04:23:58,009 INFO client.AHSProxy: Connecting to Application History server at ip-172-31-15-140.ec2.internal/172.31.15.140:10200
2024-10-22 04:24:02,147 ERROR tools.DistCp: Exception encountered 
java.io.IOException: com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.model.AmazonS3Exception: The specified bucket does not exist (Service: Amazon S3; Status Code: 404; Error Code: NoSuchBucket; Request ID: 7RFZ2T464Z4RM1PT; S3 Extended Request ID: 8sJ1D5JVdGLKZquSHlQqMCRPR1ZMk0ku9IC+9tJ0lFDvQ9sOxqNoqMAgetb+HGCJdzCtFsyVz85qAaL3sfoNhw==; Proxy: null), S3 Extended Request ID: 8sJ1D5JVdGLKZquSHlQqMCRPR1ZMk0ku9IC+9tJ0lFDvQ9sOxqNoqMAgetb+HGCJdzCtFsyVz85qAaL3sfoNhw==
        at com.amazon.ws.emr.hadoop.fs.s3n.Jets3tNativeFileSystemStore.list(Jets3tNativeFileSystemStore.java:429)
        at com.amazon.ws.emr.hadoop.fs.s3n.Jets3tNativeFileSystemStore.isFolderUsingFolderObject(Jets3tNativeFileSystemStore.java:255)
        at com.amazon.ws.emr.hadoop.fs.s3n.Jets3tNativeFileSystemStore.isFolder(Jets3tNativeFileSystemStore.java:218)
        at com.amazon.ws.emr.hadoop.fs.s3n.S3NativeFileSystem.getFileStatus(S3NativeFileSystem.java:554)
        at org.apache.hadoop.fs.Globber.getFileStatus(Globber.java:115)
        at org.apache.hadoop.fs.Globber.doGlob(Globber.java:349)
        at org.apache.hadoop.fs.Globber.glob(Globber.java:202)
        at org.apache.hadoop.fs.FileSystem.globStatus(FileSystem.java:2287)
        at com.amazon.ws.emr.hadoop.fs.EmrFileSystem.globStatus(EmrFileSystem.java:461)
        at org.apache.hadoop.tools.GlobbedCopyListing.doBuildListing(GlobbedCopyListing.java:77)
        at org.apache.hadoop.tools.CopyListing.buildListing(CopyListing.java:86)
        at org.apache.hadoop.tools.DistCp.createInputFileListing(DistCp.java:370)
        at org.apache.hadoop.tools.DistCp.prepareFileListing(DistCp.java:96)
        at org.apache.hadoop.tools.DistCp.createAndSubmitJob(DistCp.java:205)
        at org.apache.hadoop.tools.DistCp.execute(DistCp.java:182)
        at org.apache.hadoop.tools.DistCp.run(DistCp.java:153)
        at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:82)
        at org.apache.hadoop.tools.DistCp.main(DistCp.java:443)
Caused by: com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.model.AmazonS3Exception: The specified bucket does not exist (Service: Amazon S3; Status Code: 404; Error Code: NoSuchBucket; Request ID: 7RFZ2T464Z4RM1PT; S3 Extended Request ID: 8sJ1D5JVdGLKZquSHlQqMCRPR1ZMk0ku9IC+9tJ0lFDvQ9sOxqNoqMAgetb+HGCJdzCtFsyVz85qAaL3sfoNhw==; Proxy: null), S3 Extended Request ID: 8sJ1D5JVdGLKZquSHlQqMCRPR1ZMk0ku9IC+9tJ0lFDvQ9sOxqNoqMAgetb+HGCJdzCtFsyVz85qAaL3sfoNhw==
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.handleErrorResponse(AmazonHttpClient.java:1879)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.handleServiceErrorResponse(AmazonHttpClient.java:1418)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeOneRequest(AmazonHttpClient.java:1387)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeHelper(AmazonHttpClient.java:1157)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.doExecute(AmazonHttpClient.java:814)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.executeWithTimer(AmazonHttpClient.java:781)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.execute(AmazonHttpClient.java:755)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutor.access$500(AmazonHttpClient.java:715)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient$RequestExecutionBuilderImpl.execute(AmazonHttpClient.java:697)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:561)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.http.AmazonHttpClient.execute(AmazonHttpClient.java:541)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:5558)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.AmazonS3Client.invoke(AmazonS3Client.java:5505)
        at com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.AmazonS3Client.listObjectsV2(AmazonS3Client.java:1002)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.call.ListObjectsV2Call.perform(ListObjectsV2Call.java:26)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.call.ListObjectsV2Call.perform(ListObjectsV2Call.java:12)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.executor.GlobalS3Executor$CallPerformer.call(GlobalS3Executor.java:114)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.executor.GlobalS3Executor.execute(GlobalS3Executor.java:141)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.AmazonS3LiteClient.invoke(AmazonS3LiteClient.java:196)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.AmazonS3LiteClient.invoke(AmazonS3LiteClient.java:191)
        at com.amazon.ws.emr.hadoop.fs.s3.lite.AmazonS3LiteClient.listObjectsV2(AmazonS3LiteClient.java:75)
        at com.amazon.ws.emr.hadoop.fs.s3n.Jets3tNativeFileSystemStore.list(Jets3tNativeFileSystemStore.java:420)
        ... 17 more
[hadoop@ip-172-31-15-140 root]$ aws s3 ls
2024-10-18 14:43:03 aws-logs-779784271243-us-east-1
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
st0263-242
[hadoop@ip-172-31-15-140 root]$ sudo mkdir /home/hadoop/mis_datasets/
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/
mis_datasets  st0263-242
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -get /user/hadoop/datasets/gutenberg-small/* ~hadoop/mis_datasets/
get: /home/hadoop/mis_datasets/AbrahamLincoln___LincolnLetters.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___LincolnsFirstInauguralAddress.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___LincolnsSecondInauguralAddress.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___StateoftheUnionAddresses.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheEmancipationProclamation.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt._COPYING_ (Permission denied)
get: /home/hadoop/mis_datasets/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt._COPYING_ (Permission denied)
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/mis_datasets/
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/
mis_datasets  st0263-242
[hadoop@ip-172-31-15-140 root]$ sudo hdfs dfs -get /user/hadoop/datasets/gutenberg-small/* ~hadoop/mis_datasets/
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/mis_datasets/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
[hadoop@ip-172-31-15-140 root]$ sudo hdfs dfs -copyToLocal /user/hadoop/datasets/gutenberg/gutenberg-small.zip ~hadoop/mis_datasets/
copyToLocal: `/user/hadoop/datasets/gutenberg/gutenberg-small.zip': No such file or directory
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/gutenberg/
[hadoop@ip-172-31-15-140 root]$ sudo ls /home/hadoop/st0263-242/bigdata/datasets/gutenberg/
gutenberg-small-es.zip  gutenberg-txt-es.zip-url.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -put /home/hadoop/st0263-242/bigdata/datasets/gutenberg/* /user/hadoop/datasets/gutenberg/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/gutenberg/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup    3419810 2024-10-22 04:47 /user/hadoop/datasets/gutenberg/gutenberg-small-es.zip
-rw-r--r--   1 hadoop hdfsadmingroup         67 2024-10-22 04:47 /user/hadoop/datasets/gutenberg/gutenberg-txt-es.zip-url.txt
[hadoop@ip-172-31-15-140 root]$ sudo hdfs dfs -copyToLocal /user/hadoop/datasets/gutenberg/gutenberg-small-es.zip ~hadoop/mis_datasets/
[hadoop@ip-172-31-15-140 root]$ sudo ls ~hadoop/mis_datasets/
AbrahamLincoln___LincolnLetters.txt                                   AbrahamLincoln___StateoftheUnionAddresses.txt                                AbrahamLincoln___TheWritingsofAbrahamLincolnVolume4.txt
AbrahamLincoln___LincolnsFirstInauguralAddress.txt                    AbrahamLincoln___TheEmancipationProclamation.txt                             AbrahamLincoln___TheWritingsofAbrahamLincolnVolume5.txt
AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt   AbrahamLincoln___TheLifeandPublicServiceofGeneralZacharyTaylorAnAddress.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume6.txt
AbrahamLincoln___LincolnsInauguralsAddressesandLettersSelections.txt  AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt                      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume7.txt
AbrahamLincoln___LincolnsSecondInauguralAddress.txt                   AbrahamLincoln___TheWritingsofAbrahamLincolnVolume2.txt                      gutenberg-small-es.zip
AbrahamLincoln___SpeechesandLettersofAbrahamLincoln1832-1865.txt      AbrahamLincoln___TheWritingsofAbrahamLincolnVolume3.txt
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -du /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
1653  1653  /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mkdir /user/hadoop/datasets/toMove
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -mv /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt /user/hadoop/datasets/toMove/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 1 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -cp /user/hadoop/datasets/gutenberg-small/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt /user/hadoop/datasets/toMove/
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup     459006 2024-10-22 05:10 /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -rm /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
Deleted /user/hadoop/datasets/toMove/AbrahamLincoln___TheWritingsofAbrahamLincolnVolume1.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 1 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
[hadoop@ip-172-31-15-140 root]$ 
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


[hadoop@ip-172-31-15-140 root]$ hdfs dfs -touchz /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup          0 2024-10-22 05:20 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -chmod 644 /user/hadoop/datasets/toMove/prueba_para_chmod.txthdfs dfs -chmod 644 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
chmod: `/user/hadoop/datasets/toMove/prueba_para_chmod.txthdfs': No such file or directory
chmod: `dfs': No such file or directory
chmod: `-chmod': No such file or directory
chmod: `644': No such file or directory
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -chmod 644 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-r--r--   1 hadoop hdfsadmingroup          0 2024-10-22 05:20 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -chmod 600 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$ hdfs dfs -ls /user/hadoop/datasets/toMove/
Found 2 items
-rw-r--r--   1 hadoop hdfsadmingroup       1653 2024-10-22 04:20 /user/hadoop/datasets/toMove/AbrahamLincoln___LincolnsGettysburgAddressGivenNovember-19-1863.txt
-rw-------   1 hadoop hdfsadmingroup          0 2024-10-22 05:20 /user/hadoop/datasets/toMove/prueba_para_chmod.txt
[hadoop@ip-172-31-15-140 root]$
```