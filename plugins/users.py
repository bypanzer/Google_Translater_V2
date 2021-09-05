import os
from pyrogram import Client ,filters
from helper.database import getid
ADMIN = int(os.environ.get("ADMIN", 923943045))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def users(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Bütün İD-lər yaddaşdan alınır ...")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Ümumi istifadəçi sayı: {tot}")
