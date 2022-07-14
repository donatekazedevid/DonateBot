import os
from telethon import TelegramClient, events, functions, Button
from telethon.tl.functions.users import GetFullUserRequest
from .Var import *

API_ID = Var.API_ID
API_HASH = Var.API_HASH
TOKEN = Var.TOKEN
OWNER_ID = Var.OWNER_ID
DONATE_TEXT = Var.DONATE_TEXT

telegram = TelegramClient("telegram_client", api_id=API_ID, api_hash=API_HASH).start(bot_token=TOKEN)

@telegram.on(events.NewMessage(pattern="^ ?(.*)"))
async def _(event):
    # Send Donate Message
    await telegram.send_message(event.chat_id, DONATE_TEXT)

    # Forword Message to the Owner
    incoming = event.raw_text
    who = event.sender_id
    if incoming.startswith("/start"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.forward_to(OWNER_ID)

import logging
logging.basicConfig(level=logging.WARNING)

print("Donatation Bot is Redy !")
print("Be Thankful to @KenalSayaaa")

telegram.run_until_disconnected()

# <! Functions Ends >
