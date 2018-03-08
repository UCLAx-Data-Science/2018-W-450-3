# Utilizing Pig in Amazon EMR

Pig is an Apache open source project that provides a data flow engine that executes a SQL-like language into a series of parallel tasks in Hadoop. Amazon has integrated Pig into Amazon EMR for execution in Pig Job Flows. These additions allow Pig scripts to access S3 and other AWS services, along with inclusion of the Piggybank string and date manipulation UDFs, and support for the MapR version of Hadoop.

Pig performs similar data operations as SQL, but has its own syntax and can be extended with user defined functions. You can join, sort, filter, and group data by using operators and language keywords on data sets

1. Connect to the Master node via SSH:

   ```
   (local) $ ssh hadoop@ec2-54-201-52-163.us-west-2.compute.amazonaws.com
   ```
2. Launch an interactive `pig` session

   ```
   (hadoop) $ pig
   ```

3. Regist the Java UDF library `piggybank.jar` to have access to a set of UDFs for performing data manipulation and arithmetic

   ```
   grunt> register file:/usr/lib/pig/piggybank.jar
   ```

4. define the `extract` function

   ```
   grunt> define extract org.apache.pig.piggybank.evaluation.string.EXTRACT;
   ```

5. load the log files

   ```
   grunt> raw_logs = load 's3://joshuacook-test/input/mock.log' using TextLoader as (line:chararray);
   ```
