## Add the Tweets and Mapper File to Your Bucket

11. Show the S3 Buckets on Your Account

    ```
    aws s3 ls
    ```

12. Make a new bucket.
13. Copy the tweet file from my S3 bucket to yours

    ```
    aws s3 cp s3://uclax-twitter/tweets.json s3://your-bucket/input/tweets.json --acl public-read
    ```

1. Copy the file `lib/mapper.py` to `mapper/mapper.py`

    ```
    aws s3 cp lib/mapper.py s3://your-bucket/mapper/mapper.py --acl public-read
    ```





## Sync the logs

```
aws s3 sync s3://joshuacook-test/logs logs
```



   - Under Add Steps, select "Streaming Program" and click **Configure**.
   - Use the following options:
      - Name: Sentiment Analysis
      - Mapper: s3://your-bucket/mapper/mapper.py
      - Reducer: `aggregate`
      - Input S3 Location: s3://your-bucket/input/
      - Output S3 Location: s3://your-bucket/output/
      - Arguments: -cacheFile s3://awsdocs/gettingstarted/latest/sentiment/classifier.p#classifier.p
      - Action on failure: Continue
   - Click **Add**.
   - Select "Auto-terminate cluster after the last step is completed".