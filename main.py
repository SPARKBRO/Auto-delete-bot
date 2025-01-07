from time import time 
from utils.info import *
from utils.database import *
from subprocess import Popen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize the user client
User = Client("auto-delete-user",
              session_string=SESSION)

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
    # Create an inline button for the developer's contact link
    inline_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer's Contact", url="https://t.me/SPA4KBRO")]
    ])
    # Send a custom message with the inline button
    await message.reply(
        "Hi, I'm your Auto-Delete bot! I will automatically delete your messages after a certain time.\n\n"
        "If you need support or have questions, you can contact the developer directly.", 
        reply_markup=inline_button
    )

# Start the subprocesses
Popen(f"gunicorn utils.server:app --bind 0.0.0.0:{PORT}", shell=True)
Popen("python3 -m utils.delete", shell=True)

# Run the client
User.run()
