# The Hadoop Ecosystem

Amazon EMR uses Hadoop and its MapReduce framework at its core. Many of the other core Apache Software Foundation projects that work with Hadoop also work with Amazon EMR.

## Hive
Hive is a distributed data warehouse that allows you to create a Job Flow using a SQL-like language. Hive can be run from a script loaded in S3 or interactively inside of a running EMR instance.

## Pig
Pig is a data flow language. (The language is, not surprisingly, called Pig Latin.) Pig scripts can be loaded into S3 and used to perform the data analysis in a Job Flow. Pig, like Hive, is one of the Job Flow types that can be run interactively inside of a running EMR instance.

## Amazon Cloudwatch
Cloudwatch allows you to monitor the health and progress of Job Flows. It also allows you to set alarms when metrics are outside of normal execution parameters.
