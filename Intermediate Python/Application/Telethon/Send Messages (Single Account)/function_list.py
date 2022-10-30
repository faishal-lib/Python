from telethon.sync import TelegramClient
from telethon import functions, types
from api_list import *

msg = input("Type Messages : ")

def packet1():
    with TelegramClient('syambadra', api_id_syambadra, api_hash_syambadra) as client:
        result = client.send_message('mfaishal24', msg)

def packet2():
    with TelegramClient('yulianur', api_id_yulianur, api_hash_yulianur) as client:
        result = client.send_message('mfaishal24', msg)