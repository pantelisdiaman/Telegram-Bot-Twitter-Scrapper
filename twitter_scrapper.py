import time
from typing import NoReturn
from twikit import Client, Tweet
import telegram_bot
import os

# Set window title
os.system('title Twitter scrapper')

# Login with cookies
client = Client()
client.load_cookies('cookies.json')

print("Login successful")

# Get the usernames from the file
f = open("usernames.txt", "r")
text = f.read()
if text == '':
    exit()
usernames = text.split("\n")

# For every username, get the user id and the tweet count
userIdsAndTweetCounts = []

for username in usernames:
    user = client.get_user_by_screen_name(username)
    userIdsAndTweetCounts.append([user.id, user.statuses_count])
    time.sleep(2)

print("Users data fetched\nListening for new tweets...")

# For every user id, check if the tweet count has changed
# If yes, get that tweet and inform the bot to send it
while(True):
    for userIdAndTweetCount in userIdsAndTweetCounts:
        try:
            user = client.get_user_by_id(userIdAndTweetCount[0])
        except Exception as e:
            print("An error occured:\n",e)
        if (user.statuses_count > userIdAndTweetCount[1]):
            userIdAndTweetCount[1] = user.statuses_count
            time.sleep(5)
            tweet = client.get_user_tweets(userIdAndTweetCount[0], "Tweets")[0]
            telegram_bot.sendTweet(tweet.text)
        time.sleep(3)
