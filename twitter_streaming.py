#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "Enter the token"
access_token_secret = "Enter the token secret"
consumer_key = "Enter API key"
consumer_secret = "Enter API secret"


#This is a basic listener that just prints received tweets to stdout.

MAX_NUM_TWEETS = 50000
class StdOutListener(StreamListener):
    def __init__(self):
        self.count = 0

    def on_data(self, data):
        self.count += 1
        print data
        if self.count > MAX_NUM_TWEETS:
            return False
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'FIFA', 'World', 'Cup','football' etc.
    # stream.filter(track=['FIFA', 'World','Cup','football', 'FIFA World Cup','#FIFA2018','WorldCup','#WorldCup2018','#FifaWorldCup','#FIFAWorldCup','RUSKSA','#RUSKSA','prediction','win','#FIFA'])
    stream.filter(track=['#FIFA','#WorldCup'])