# Utilizing Hive in Amazon EMR

Hive is a powerful SQL-like language that allows us to query Amazon EMR. Hive was built to lower the barrier of entry for the large masses of IT professionals who know how to develop in SQL and harness the power of Amazon EMR. The Hive Query Language (HQL) much more closely resembles SQL in feature and function than Pig. The time required for someone who already understands SQL to begin developing in Hive is much shorter than it would be for Pig or Java MapReduce development. Hive is preinstalled on the Amazon EMR nodes in clusters using the Hive Program Job Flow.

1. Connect to the Master node via SSH:

   ```
   (local) $ ssh hadoop@ec2-54-201-52-163.us-west-2.compute.amazonaws.com
   ```
2. Launch an interactive `hive` session

   ```
   (hadoop) $ hive
   ```

3. Create a table for the `log_data`

   ```
   CREATE EXTERNAL TABLE log_data (
           timestring STRING,
           host STRING,
           application STRING,
           message STRING,
           username STRING)
       ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
       STORED AS TEXTFILE
       LOCATION 's3://your-bucket/input';
   ```

4. Run SQL Queries on the `log_data` table:

   ```
   select count(*) from log_data;

   select * from log_data limit 5;

   select * from log_data where message rlike '.*SEVERE*.' limit 5;
   ```

5. Write the results to an external file:

   ```
   insert overwrite directory  's3://your-bucket/output/'
   row format delimited
   fields terminated by ','
   stored as textfile
   select username, count(*) from log_data where message rlike '.*SEVERE*.' group by username;
   ```

6. Copy the file to your local computer. Import the csv into pandas and create a bar plot of the results.

7. More SQL queries

   ```
   select message, count(*) as cnt from log_data where message rlike '.*SEVERE*.' group by message order by cnt desc limit 10;

   show tables;

   describe log_data;

   drop table log_data;

   CREATE EXTERNAL TABLE log_data (
           timestring STRING,
           host STRING,
           application STRING,
           message STRING,
           username STRING)
       ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
       STORED AS TEXTFILE
       LOCATION 's3://your-bucket/input';

   select timestring, count(*) from log_data group by timestring;
   ```
