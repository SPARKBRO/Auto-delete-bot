import os
from time import time 
from utils.info import * 
from utils.database import *
from subprocess import Popen
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton

User = Client("auto-delete-user", session_string=SESSION)

@User.on_message(filters.chat(CHATS))
async def delete(user, message):
    try:
        if bool(WHITE_LIST):
            if message.from_user.id in WHITE_LIST:
                return 
        if bool(BLACK_LIST):
            if message.from_user.id not in BLACK_LIST:
                return
        _time = int(time()) + TIME 
        save_message(message, _time)
    except Exception as e:
        print(str(e))

@User.on_message(filters.regex("!start") & filters.private)
async def start(user, message):
    
    start_message = f"<b><i>Hi {message.from_user.first_name},👋🏻\n\n" \
                    "I automatically delete messages in your chat after a specific time to keep it clean.</i></b>"

    if PICS:
        await message.reply_photo(
            photo=PICS,  
            caption=start_message,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Developer 💀", url="https://t.me/SPA4KBRO")
            ]])
        )
    else:
        await message.reply_text(
            start_message,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Developer 💀", url="https://t.me/SPA4KBRO")
            ]])
        )


Popen(f"gunicorn utils.server:app --bind 0.0.0.0:{PORT}", shell=True)
Popen("python3 -m utils.delete", shell=True)
User.run()
