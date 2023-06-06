import tweepy


consumer_key = '-'
consumer_secret = '-'
access_token = '5467427035896754874--'
access_token_secret = '-'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

username = 'elonmusk'
count = 10

tweets = api.user_timeline(screen_name=username, count=count)


for tweet in tweets:
    print(tweet.text)
