from tweepy import Stream
from tweepy import OAuthHandler
import time
from tweepy.streaming import StreamListener

ckey='eZSxJEtGtCY5SqcVh3cZUbf27'
csecretkey='Ub7vovbs2M8uCAKBuGslBy4Sb9ArHOXFaRYhtp12k5ZMQDOZOF'
atoken='449479332-1dha1NMfojFmuY1tBuNjrzHmZnJSRt8bhgejrV0p'
asecret='hpmw39VPT5m3XlFmuDW416u24melcqLVur0E8vZQfLefJ'


class listener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            saveFile= open('twitDB.csv', 'a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except Exception as e:

            print('filed connect',e)
            time.sleep(5)


    def on_error(self, status_code):
        print (status_code)



auth = OAuthHandler(ckey, csecretkey)


auth.set_access_token(atoken, asecret)


twitterStreaming = Stream(auth, listener())

twitterStreaming.filter(track=["car"])
