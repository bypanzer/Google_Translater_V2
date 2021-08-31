from pyrogram import Client ,filters
import os
from helper.database import getid
ADMINS = int(os.environ.get("ADMINS", 1518238620 1933278415))


@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Bütün userlər yaddaşdan çağırılır ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Yayım başladı .... \n Mesajınız {tot} istifadəçiyə göndərilir")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass
