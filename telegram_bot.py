import telebot

# Create bot
bot = telebot.TeleBot(token='XXXX')

# Send tweet
def sendTweet(tweet):  
    bot.send_message('XXXX', tweet)
