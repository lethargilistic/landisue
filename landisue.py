from datetime import datetime
import keys
import tweepy
import json
from gpcharts import figure

def get_date(tweet):
    date = datetime.strptime(tweet._json["created_at"], '%a %b %d %H:%M:%S +0000 %Y')
    return date.date()
 
def all_landis_dream():
    '''A graph of all tweets regarding Max Landis Mary Sue tweets over time.
    I will not be able to do this unless I bought access to Twitter Firehose for
    11-ty billion dollars. Or Max Landis could give me his tweet archive and
    I could do part of it. But that's kind of the least interesting interesting
    part of this idea.'''
    more_landis_tweets = api.user_timeline(id="uptomyknees",count=200)
    all_tweets.extend(more_landis_tweets)
    oldest_id = all_tweets[-1].id - 1

    while more_landis_tweets:
        print("Tweets before {}".format(more_landis_tweets[-1]._json["created_at"]))
        
        more_landis_tweets = api.user_timeline(id="uptomyknees",count=200,max_id=oldest_id)
        all_tweets.extend(more_landis_tweets)
        oldest_id = all_tweets[-1].id - 1

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)

all_tweets = []
all_tweets.extend(api.search("max landis mary sue", rpp=100))

date_dict = dict()
for tweet in all_tweets:
    date = get_date(tweet)
    if date in date_dict:
        date_dict[date] += 1
    else:
        date_dict[date] = 1
    print(tweet._json["text"])

print(date_dict)

dates = []
counts = []
for item in date_dict.items():
    dates.append(str(item[0]))
    counts.append(item[1])


print(len(dates))
print(dates)
print(len(counts))
print(counts)

fig1 = figure()
fig1.plot(dates, counts)
