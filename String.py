import os
os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print("•••   KINGBOT  SESSION  GENERATOR   •••")
print("\nHello!! This is KINGBOT Session Generator\n")
kingbot = input(" Type 777 and hit enter to confirm U r Human 😇 :")
if kingbot == "777":
    print("Choose the string session type: \n1. TELETHON \n2. PYROGRAM")
    store = input("\nYour Choice: ")
    if store == "1":
        print("\nTelethon String Session ")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as kartik:
            print("\nYour Telethon Session Is sent in your Telegram Saved Messages.")
            kartik.send_message("me", f"#KINGBOT #TELETHON_SESSION @KINGBOTOFFICIALCHAT  \n\n`{kartik.session.save()}`")
    elif store == "2":
        print("Pyrogram Session  ")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as kartik:
            print("\nPYROGRAM String Session Is sent in your Telegram Saved Messages.")
            kartik.send_message("me", f"#KINGBOT #PYROGRAM_SESSION\n\n`{kartik.export_session_string()}`")
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("CONTACT @KINGBOTOFFICIALCHAT ")
