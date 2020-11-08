from telethon import TelegramClient
import time
# Use your own values from my.telegram.org



api_id = int(input("APP_ID : "))

api_hash = input ("API_HASH : ")

user = ("TELEGRAM USER : ")
msg = input(" MASSG : ")
mssg = msg
# The first parameter is the .session file name (absolute paths allowed)
while True:
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(user, mssg)
        time.sleep(0.3)
    