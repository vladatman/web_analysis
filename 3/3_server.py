import smtplib
import tweepy

# Credentials
consumer_key = '-'
consumer_secret = '-'
access_token = '--NdrZM6lsET1LZzHYqy96oFLyOSrdnd'
access_token_secret = '-'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = 'HromadskeUA'
count = 10

tweets = api.user_timeline(screen_name=username, count=count)
keyword = 'your-keyword'

smtp_server = 'your-smtp-server'
smtp_port = 'your-smtp-port'
smtp_username = 'your-smtp-username'
smtp_password = 'your-smtp-password'

alert_email = 'your-email@example.com'

for tweet in tweets:
    if keyword in tweet.text:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, alert_email, f'Keyword found in tweet: {tweet.text}')