import twitterscraper
from twython import Twython
import config

TWITTER_APP_KEY = config.TWITTER_APP_KEY
TWITTER_APP_KEY_SECRET = config.TWITTER_APP_KEY_SECRET
TWITTER_ACCESS_TOKEN = config.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = config.TWITTER_ACCESS_TOKEN_SECRET

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.get_place_trends(id=23424977)

top_hashtag = (search[0]['trends'][0]['name'])

print("The top trending hashtag in the US is", top_hashtag)
tweets = twitterscraper.query_tweets(top_hashtag, 2000,lang='en')
print("got {} tweets".format(len(tweets)))

for i,tweet in enumerate(tweets):
    name = 'vocab/{}.txt'.format(str(i))
    t = tweet.text.split()
    t = filter(lambda x:x[0]!='@' and 'http' not in x, t)
    t = ' '.join(t)
    f = open(name, 'w')
    f.write(t)
    f.close()
