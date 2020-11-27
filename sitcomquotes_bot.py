import sys, telepot, json, time, requests, os
from telepot.loop import MessageLoop
import random


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        text = msg['text']

        if text == '/start':
            bot.sendMessage(chat_id, "Hi! Choose the sitcom to get the random quote.\nType */* to check out the options.", parse_mode= 'Markdown')

        elif text == '/friends':
        	RandomQuote("Friends", chat_id)

        elif text == '/himym':
        	RandomQuote("Himym", chat_id)

        elif text == '/github':
        	bot.sendMessage(chat_id, "To know how this bot works: https://github.com/fillics/telegrambot-python")

        else:
        	bot.sendMessage(chat_id, "ERROR: don't text anything.")
        	
    else:
        bot.sendMessage(chat_id, "ERROR: don't send files.")

 
def RandomQuote(sitcom, chat_id):
	if sitcom == "Friends":
		num = random.randint(0,19)
		bot.sendMessage(chat_id, dataFriends[num]['quote'] + "\n" + "*" +
			dataFriends[num]['character'] + "*", parse_mode= 'Markdown')

	if sitcom == "Himym":
		num = random.randint(0,42)
		bot.sendMessage(chat_id, dataHimym[num]['quote'] + "\n" + "*" +
			dataHimym[num]['character'] + "*", parse_mode= 'Markdown')
	
		
fileFriends = open('friends.json')
fileHimym = open('himym.json')
dataFriends = json.load(fileFriends)
dataHimym = json.load(fileHimym)

TOKEN = 'INSERT_YOUR_TOKEN_HERE'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the bot running
while 1:
  time.sleep(10)
