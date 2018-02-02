import datetime
import time

from pymongo import MongoClient
from twitter import TwitterStream
from twitter import OAuth

from pymongo.errors import DuplicateKeyError
from urllib.error import HTTPError
from twitter.api import TwitterHTTPError

class Twitterator:

    def __init__(self, credentials, bounding_box):
        self.oauth = OAuth(credentials['ACCESS_TOKEN'],
                           credentials['ACCESS_SECRET'],
                           credentials['CONSUMER_KEY'],
                           credentials['CONSUMER_SECRET'])

        self.mongo_client = MongoClient('34.209.155.42', 27016)
        self.database_reference = self.mongo_client.twitter
        self.collection_reference = self.database_reference.tweets

        self.bounding_box = bounding_box

        self.now = datetime.datetime.now()
        self.last_time = self.now - datetime.timedelta(hours=1)

        self.twitterator = None

    def _create_tweet_iterator(self):
        self.twitter_stream = TwitterStream(auth=self.oauth)
        try:
            tweet_iterator = (self.twitter_stream
                              .statuses
                              .filter(locations=self.bounding_box))
        except HTTPError:
            tweet_iterator = None
            time.sleep(60)
        except TwitterHTTPError:
            tweet_iterator = None
            print("Too many users for this account connected to Twitter. Trying again in 60 seconds.")
            time.sleep(60)
        return tweet_iterator

    def _get_next_tweet(self):
        return next(self.twitterator)

    def _insert_tweet_into_mongo(self, tweet):
        try:
            self.collection_reference.insert_one(tweet)
        except DuplicateKeyError:
            self._log_count("Duplicate Key Error")

    def _log_count(self, message):
        current_hour = (self.now.hour- 8) % 12
        current_minute = self.now.minute
        current_count = self.collection_reference.count()
        print("{} {:2}:{}\t: {}".format(message, current_hour, current_minute, current_count))

    def collect_tweets(self):
        while True:
            try:
                while self.twitterator is None:
                    self.twitterator = self._create_tweet_iterator()

                while True:
                    self.now = datetime.datetime.now()

                    if self.last_time.hour != self.now.hour:
                        self._log_count("Current Count")

                    tweet = self._get_next_tweet()
                    self._insert_tweet_into_mongo(tweet)

                    self.last_time = self.now

            except StopIteration:
                now = datetime.datetime.now()
                self._log_count("Dead Iteration Error")
