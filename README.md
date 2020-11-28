# telegramBot-python
How to create a Telegram Bot with Python. In this guide, I'll create a bot that gives it back a random quote from two json files.
The user can use only the following commands:
* /start: to run the bot
* /friends: to get a random Friends quote
* /himym: to get a random How I met your mother quote
* /github: to print the link to this guide

The bot created is [@SitComBot](https://web.telegram.org/#/im?p=@randomsitcomquotesBot).
## Prerequisites
To create this simple bot, it's recommended to know the Python fundamentals.

## How does it work
When the user wants to receive a quote, the bot will choose it randomly from [friends.json](friends.json) and [himym.json](himym.json). For sending messages, we'll use the Python library **telepot**.

## Getting started
First of all, you need to install [Python](https://www.python.org/downloads/) and a text editor to code your bot. I suggest you to use [Sublime Text](https://www.sublimetext.com/) because it's my favourite one due to its minimalism, but every text editor/IDE is fine. 
For this guide, I'll use a text editor and the command prompt to run the script.

Then, you must have a Telegram account and then get the token to access the Telegram bot, using [@BotFather](https://web.telegram.org/#/im?p=@BotFather).

![Immagine](https://user-images.githubusercontent.com/24494773/100155376-7575c280-2ea7-11eb-8a0d-30a1624e92bb.png)

Save the **token** because you'll need it later. 

We must install some Python modules throught the Command Prompt: 
1) Open Command Prompt (Select Start button, type "cmd", select Command Prompt from the list).
2) Check if you have correctly installed Python, typing `python --version`. If you see your version, you can pass to the next step, otherwise you need to add Python to your Windows PATH ([guide](https://datatofish.com/add-python-to-windows-path/)). 
3) Type `sudo apt-get update` and `sudo apt-get upgrade` to download updated version of packages from Python location.
4) Type `sudo apt install python3-pip` to install *pip* that is necessary for the next step to install the modules.
5) Install the following modules: telepot, requests, os, time, pprint, sys. Install them typing in the Command Prompt `pip install <NAME_MODULE>` (for example `pip install telepot`).

## Let's code
Open the text editor/IDE and create a new project, saving it in the same folder where there are the two json files, with the extension .py, for example *sitcomquotes_bot.py*. 
Now we're ready. First of all, we need to import all of modules we are going to use. 

```
import sys, telepot, json, time, requests, os, random
from telepot.loop import MessageLoop

```

After that, let's define our *handle* function, to handle messages sent by users. The following code lines are to extract “headline” info about the message sent by users.

```
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
```

The first thing texted from a user is */start*, so we need to define what our bot does in this situation: it sends a welcome message .

```
if text == '/start':
            bot.sendMessage(chat_id, "Hi! Choose the sitcom to get the random quote.")
```
Now the user can choose with the three following commands. /friends and /himym call the *RandomQuote* function that we are going to define.

```
elif text == '/friends':
            ** call the function to get the random quote **
            RandomQuote("Friends", chat_id)
elif text == '/himym':
            ** call the function to get the random quote **
            RandomQuote("Himym", chat_id)
elif text == '/github':
            bot.sendMessage(chat_id, "To know how this bot works: https://github.com/fillics/telegrambot-python")
```

Let's define the function RandomQuote that reads from the json files and sends a message that contains a random quote and the character.

```
def RandomQuote(sitcom, chat_id):
	if sitcom == "Friends":
		num = random.randint(0,19)
		bot.sendMessage(chat_id, dataFriends[num]['quote'] + "\n" + "*" +
			dataFriends[num]['character'] + "*", parse_mode= 'Markdown')

	if sitcom == "Himym":
		num = random.randint(0,42)
		bot.sendMessage(chat_id, dataHimym[num]['quote'] + "\n" + "*" +
			dataHimym[num]['character'] + "*", parse_mode= 'Markdown')
```

We are almost done. To start the bot and keep running it, we need to add the following lines and substitute INSERT_YOUR_TOKEN with the token obtained when we created the bot throught BotFather.

```
TOKEN = 'INSERT_YOUR_TOKEN'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
while 1:
  time.sleep(10)
```

To run the bot, go to the Command Prompt and using the command `cd`, moving into the folder where you saved your telegramBot.py and the two json files.
After that, type `python sitcomquotes_bot.py`. If the terminal prints "Listening", the bot works!

![image](https://user-images.githubusercontent.com/24494773/100470775-2ca55000-30d9-11eb-8184-f68032187e79.png)
