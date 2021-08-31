from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from helper.database import set,unset ,insert
from helper.list import list

@Client.on_message(filters.private &filters.command(['unset']))
async def unsetlg(client,message):
	unset(int(message.chat.id))
	await message.reply_text("Seçdiyiniz dil uğurla silindi ✅")

@Client.on_message(filters.private &filters.command(['set']))
async def setlg(client,message):
    	    user_id = int(message.chat.id)
    	    insert(user_id)
    	    text = message.text
    	    textspit = text.split('/set')
    	    lg_code = textspit[1]
    	    if lg_code:
    	    		cd = lg_code.lower().replace(" ", "")
    	    		try:
    	    			lgcd = list[cd]
    	    		except:
    	    			await message.reply_text("❗️ Bu dil mənim üçün əlçatan deyil \n Zəhmət olmasa, birdə yoxla😉",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Əlçatan Dillər 📑" ,url="https://telegra.ph/%C6%8Fl%C3%A7atan-Dill%C9%99r-DilmancAzBot-08-31")]]))
    	    			return
    	    		set(user_id,lgcd)
    	    		await message.reply_text(f" **{cd}** artıq bütün mesajlara tətbiq ediləcək🙆,kənarlaşdırmaq üçün /unset toxun")
    	    else:
    	    		await message.reply_text(" Zəhmət olmasa,əmri dil adı ilə birgə istifadə et. \n **Məsələn:/set Azerbaijani**",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Kömək 🆘",url = "https://t.me/EpicProjects")]]))
