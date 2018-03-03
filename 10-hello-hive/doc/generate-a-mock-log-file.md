# Generate a Mock `log` File with Python

In the `src` directory, there is a file called `generate_mock_log.py` that can be used to create a file of simulated log messages. The output resembles the output stream that might be seen as part of an application's normal operation.

## Execute the script using

```
python3 src/generate_mock_log.py
```

## Copy the Result to S3

```
aws s3 cp data/mock.log s3://your-bucket/input/mock.log
```
