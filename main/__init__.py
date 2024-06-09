#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=12526104, cast=int)
API_HASH = config("API_HASH", default="a8f5ba5025100f011aa0b65b81fad5b3")
BOT_TOKEN = config("BOT_TOKEN", default="6629920564:AAFE5PeRLYmUXIsfEK60_Xpu95OpVhwPDYo")
SESSION = config("SESSION", default="AQC_IhgAmxftD5CfqInf9FCXbCYCMgsj7xonSpp2rQdeekryrPJjmfeXnc1nrW7TKeUAhZ4vAR8ZKpiHfxIuE0yPMtvewg9uYM4jY1IPvg2LRhB2dDbcDVTWTwXheVL6WdYJ_Vb14G08yz2_Wdq5CtHyWoVgC-6jg0-4DYD7ujAU3dBXX9AsWRAmgX9xT1hzJlu01J5i_Hq96zAuFqwcbZ-vAN_YrjsD_g2W7W7IBv34u_ia9nQeA9sxTRT124r516rWFMW7YtdXHidW4MC0dzNHcpgn3oW0MxeFzjXtkkEewhT0XgptGKLEsGpYNSbru-8MevM-n74wpjJVxZCFdZGIvHs5lQAAAAA4poHhAA")
FORCESUB = config("FORCESUB", default="saverforme")
AUTH = config("AUTH", default=950436321, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
