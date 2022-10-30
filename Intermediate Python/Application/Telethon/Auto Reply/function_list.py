from telethon.sync import TelegramClient, events
from telethon import functions, types
from api_list import *

select_session = int(input("Select Session : "))
if select_session == 1 : 
    session_name = "syambadra"

elif select_session == 2 : 
    session_name = "yulianur"

username = input("Input Username : ")

def packet1():
    client = TelegramClient('syambadra', api_id_syambadra, api_hash_syambadra)
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if 'Click "Continue" to proceed' in event.raw_text:
            await event.reply('Continue ')

        if 'Click "Submit Details" to submit your details to verify whether you completed all the tasks or not.' in event.raw_text:
            await event.reply('Submit Details ')

        if 'Submit your Email address that you used to register' in event.raw_text:
            await event.reply(username+ '@gmail.com ')

        if 'After joined, press "✅Done"' in event.raw_text:
            await event.reply('✅Done')

        if 'Submit your Twitter profile link' in event.raw_text:
            await event.reply('https://www.twitter.com/' +username)

        if 'Did you perform this task? press "✅Yes" to proceed' in event.raw_text:
            await event.reply('✅Yes')

        if 'Submit your Binance Smart Chain (BEP-20) wallet address' in event.raw_text:
            await event.reply('0xbac480e3e4605635996E201274B6413f6f386C76')

    client.start()
    client.run_until_disconnected()

def packet2():
    client = TelegramClient(session_name, api_id_syambadra, api_hash_syambadra)
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if 'Click "Continue" to proceed' in event.raw_text:
            await event.reply('Continue ')

        if 'Click "Submit Details" to submit your details to verify whether you completed all the tasks or not.' in event.raw_text:
            await event.reply('Submit Details ')

        if 'Submit your Email address that you used to register' in event.raw_text:
            await event.reply(username+ '@gmail.com ')

        if 'After joined, press "✅Done"' in event.raw_text:
            await event.reply('✅Done')

        if 'Submit your Twitter profile link' in event.raw_text:
            await event.reply('https://www.twitter.com/' +username)

        if 'Did you perform this task? press "✅Yes" to proceed' in event.raw_text:
            await event.reply('✅Yes')

        if 'Submit your Binance Smart Chain (BEP-20) wallet address' in event.raw_text:
            await event.reply('0xbac480e3e4605635996E201274B6413f6f386C76')

    client.start()
    client.run_until_disconnected()
