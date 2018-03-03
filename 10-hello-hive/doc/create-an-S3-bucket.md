# Create an S3 Bucket and Configure It For Use with EMR

Note: Storing data on your S3 bucket costs approximately $0.023/GB/month.

## Configure S3

1. Show the S3 Buckets on Your Account

   ```
   aws s3 ls
   ```

1. Make a new bucket

   ```
   aws s3 mb s3://unique-bucket-name
   ```

1. Show the S3 Buckets on Your Account

   ```
   aws s3 ls
   ```