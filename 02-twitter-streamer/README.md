# Twitter Streamer

## Usage

1. If it does not exist, you will need to create a file called `credentials.yml` in the `data` directory.

   This file should contain the following:

   ```
   CONSUMER_KEY: consumer_key_token
   CONSUMER_SECRET: consumer_secret_token
   ACCESS_TOKEN: access_token
   ACCESS_SECRET: access_secret
   ```

   These strings can be obtained from https://apps.twitter.com.

2. Build the required Docker image.

   ```
   docker build -t twitter_streamer .
   ```

3. Run the program using Docker.

   ```
   docker run -it -v `pwd`:/home twitter_streamer
   ```