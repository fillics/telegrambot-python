# telegramBot-python
How to create a Telegram Bot with Python. For this guide, I want to create a bot 

## Getting started
First of all, you need to install [Python](https://www.python.org/downloads/) and a text editor to code your bot. I suggest you to use [Sublime Text](https://www.sublimetext.com/) because it's my favourite one due to its minimalism, but every text editor/IDE is fine. 
For this guide, I'll use a text editor and the command prompt to run the script.

Then, you must have a Telegram account and then get the token to access the Telegram bot, using [@BotFather](https://web.telegram.org/#/im?p=@BotFather).

![image](https://user-images.githubusercontent.com/24494773/100011405-f6628a80-2dd1-11eb-950f-a2ad677f4020.png)

Save the **token** because you'll need it later. 

We must install some Python modules throught the Command Prompt: 
1) Open Command Prompt (Select Start button, type "cmd", select Command Prompt from the list).
2) Check if you have correctly installed Python, typing `python --version`. If you see your version, you can pass to the next step, otherwise you need to add Python to your Windows PATH ([guide](https://datatofish.com/add-python-to-windows-path/)). 
3) Type `sudo apt-get update` and `sudo apt-get upgrade` to download updated version of packages from Python location.
4) Type `sudo apt install python3-pip` to install *pip* that is necessary for the next step to install the modules.
5) We need the following modules: telepot, requests, os, json, time, pprint, sys. Install them with `pip install <MODULE>` (for example `pip install telepot`). If *pip install json* doesn't work, type *pip install ijson*. 

## Let's code
Open the text editor/IDE and create a new project. Let's save it with the extension .py, for example *telegramBot.py*. 
First of all, we need to import all of modules we are going to use. 
```
import sys, telepot, json, time
from telepot.loop import MessageLoop
import requests, os

```
