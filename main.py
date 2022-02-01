import tweepy

import key



if __name__ == '__main__':
    # 認証
    auth = tweepy.OAuthHandler(key.CONSUMER_KEY, key.CONSUMER_SECRET)
    auth.set_access_token(key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    api.update_status("これは自動投稿です")#ツイート
