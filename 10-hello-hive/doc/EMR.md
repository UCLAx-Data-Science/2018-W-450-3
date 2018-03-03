# Amazon Elastic MapReduce (EMR)

Amazon EMR is the in-the-cloud workhorse of the Hadoop framework that allows us to analyze vast amounts of data with a configurable and scalable amount of computing power. Amazon EMR makes heavy use of the Amazon Simple Storage Service (S3) to store analysis results and host data sets for processing, and leverages Amazon EC2’s scalable compute resources to run the Job Flows we develop to perform analysis. There is an additional charge of about 30 percent for the EMR EC2 instances.

Amazon EMR performs the computational analysis using the MapReduce framework. The MapReduce framework splits the input data into smaller fragments, or shards, that are distributed to the nodes that compose the cluster. A Job Flow is executed on a series of EC2 instances running the Hadoop components that are broken up into master, core, and task clusters. These individual data fragments are then processed by the MapReduce application running on each of the core and task nodes in the cluster. We commonly call the MapReduce application a **Job Flow**.

The master, core, and task cluster groups perform the following key functions in the Amazon EMR cluster:

## Master group instance

The master group instance manages the Job Flow and allocates all the needed executables, JARs, scripts, and data shards to the core and task instances. The master node monitors the health and status of the core and task instances and also collects the data from these instances and writes it back to Amazon S3. The master group instances serve a critical function in our Amazon EMR cluster. If a master node is lost, you lose the work in progress by the master and the core and task nodes to which it had delegated work.

## Core group instance

Core group instance members run the map and reduce portions of our Job Flow, and store intermediate data to the Hadoop Distributed File System (HDFS) storage in our Amazon EMR cluster. The master node manages the tasks and data delegated to the core and task nodes. Due to the HDFS storage aspects of core nodes, a loss of a core node will result in data loss and possible failure of the complete Job Flow.

## Task group instance

The task group is optional. It can do some of the dirty computational work of the map and reduce jobs, but does not have HDFS storage of the data and intermediate results. The lack of HDFS storage on these instances means the data needs to be transferred to these nodes by the master for the task group to do the work in the Job Flow.

The master and core group instances are critical components in the Amazon EMR cluster. A loss of a node in the master or core group instance can cause an application to fail and need to be restarted. Task groups are optional because they do not control a critical function of the Amazon EMR cluster. In terms of jobs and responsibilities, the master group must maintain the status of tasks. A loss of a node in the master group may make it so the status of a running task cannot be determined or retrieved and lead to Job Flow failure.

The core group runs tasks and maintains the data retained in the Amazon EMR cluster. A loss of a core group node may cause data loss and Job Flow failure.

A task node is only responsible for running tasks delegated to it from the master group and utilizes data maintained by the core group. A failure of a task node will lose any interim calculations. The master node will retry the task node when it detects failure in the running job. Because task group nodes do not control the state of jobs or maintain data in the Amazon EMR cluster, task nodes are optional, but they are one of the key areas where capacity of the Amazon EMR cluster can be expanded or shrunk without affecting the stability of the cluster.