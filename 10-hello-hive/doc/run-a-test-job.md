# Run A Test Job

# Sample Data

For this test job, the sample data and sample script are already provided for you.

## Sample Data Overview

The sample data is a series of Amazon CloudFront web distribution log files. The data is stored in Amazon S3 at `s3://us-west-2.elasticmapreduce.samples`.

Each entry in the CloudFront log files provides details about a single user request in the following format:

```
2014-07-05 20:00:00 LHR3 4260 10.0.0.15 GET eabcd12345678.cloudfront.net /test-image-1.jpeg 200 - Mozilla/5.0%20(MacOS;%20U;%20Windows%20NT%205.1;%20en-US;%20rv:1.9.0.9)%20Gecko/2009040821%20IE/3.0.9
```

## Sample Hive Script Overview

The sample script calculates the total number of requests per operating system over a specified timeframe. The script uses HiveQL, which is a SQL-like scripting language for data warehousing and analysis. The script is stored in Amazon S3 at `s3://us-west-2.elasticmapreduce.samples/cloudfront/code/Hive_CloudFront.q`.

The sample Hive script does the following:

- Creates a Hive table named cloudfront_logs.
- Reads the CloudFront log files from Amazon S3 using EMRFS and parses the CloudFront log files using the regular expression serializer/deserializer (RegEx SerDe).
- Writes the parsed results to the Hive table cloudfront_logs.
- Submits a HiveQL query against the data to retrieve the total requests per operating system for a given time frame.
- Writes the query results to your Amazon S3 output bucket.

### Sample Hive Code

The Hive code that creates the table looks like the following:

```
CREATE EXTERNAL TABLE IF NOT EXISTS cloudfront_logs ( 
    DateObject Date, 
    Time STRING, 
    Location STRING, 
    Bytes INT, 
    RequestIP STRING, 
    Method STRING, 
    Host STRING, 
    Uri STRING, 
    Status INT, 
    Referrer STRING, 
    OS String, 
    Browser String, 
    BrowserVersion String 
)
```

The Hive code that parses the log files using the RegEx SerDe looks like the following:

```
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' 
WITH SERDEPROPERTIES ( 
  "input.regex" = "^(?!#)([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+([^ ]+)\\s+[^\(]+[\(]([^\;]+).*\%20([^\/]+)[\/](.*)$"
) LOCATION '${INPUT}/cloudfront/data/';
```

The HiveQL query looks like the following:

```
INSERT OVERWRITE DIRECTORY '${OUTPUT}/os_requests/' SELECT os, COUNT(*) count FROM cloudfront_logs WHERE dateobject BETWEEN '2014-07-05' AND '2014-08-05' GROUP BY os;
```

# Process Your Sample Data By Running a Hive Script

In this step of the test job, you run your Hive script in your cluster as a step in the Amazon EMR console to process your sample data. In Amazon EMR, a **step** is a unit of work that contains one or more Hadoop jobs. You can submit steps when you create the cluster or when the cluster is running (if it is a long-running cluster).

## Submit the Hive Script as a Step

Use the Add Step option to submit your Hive script to the cluster using the console. The Hive script and sample data used by the script have been uploaded to Amazon S3 for you.

To submit your Hive script as a step:
1. Open the Amazon EMR console at https://console.aws.amazon.com/elasticmapreduce/.
1. In Cluster List, select the name of your cluster.
1. Scroll to the Steps section and expand it, then choose Add step.

In the Add Step dialog:

1. For Step type, choose Hive program.
1. For Name, accept the default name (Hive program) or type a new name.
1. For Script S3 location, type `s3://us-west-2.elasticmapreduce.samples/cloudfront/code/Hive_CloudFront.q`
1. For Input S3 location, type `s3://us-west-2.elasticmapreduce.samples`
1. For Output S3 location, type or browse to the `output` bucket that you created in Create an Amazon S3 Bucket.
1. For Arguments, include the following argument to allow column names that are the same as reserved words: `-hiveconf hive.support.sql11.reserved.keywords=false`
1. For Action on failure, accept the default option Continue.
1. Choose Add. The step appears in the console with a status of Pending.

The status of the step changes from Pending to Running to Completed as the step runs. To update the status, choose Refresh above the Actions column. The step runs in approximately 1 minute.

## View the Results

After the step completes successfully, the query output produced by the Hive script is stored in the Amazon S3 output folder that you specified when you submitted the step.

### Sync the Output

Run this command to sync the output to your working directory.

```
aws s3 sync s3://joshuacook-test/output output
```

You can view the output in your shell