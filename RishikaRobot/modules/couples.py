import os 
import random
from datetime import datetime 
from telegraph import upload_file
from PIL import Image , ImageDraw
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

from RishikaRobot import pbot as app
from RishikaRobot.mongo.couples_db import _get_image, get_couple

AVISHA = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/AlisaMusicRobot?startgroup=true",
        ),
    ],
]
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list
    

def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a

tomorrow = str(dt_tom())
today = str(dt()[0])

@app.on_message(filters.command("couples"))
async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")
    try:
     #  is_selected = await get_couple(cid, today)
     #  if not is_selected:
         msg = await message.reply_text("🐾")
         #GET LIST OF USERS
         list_of_users = []

         async for i in app.get_chat_members(message.chat.id, limit=50):
             if not i.user.is_bot:
               list_of_users.append(i.user.id)

         c1_id = random.choice(list_of_users)
         c2_id = random.choice(list_of_users)
         while c1_id == c2_id:
              c1_id = random.choice(list_of_users)


         photo1 = (await app.get_chat(c1_id)).photo
         photo2 = (await app.get_chat(c2_id)).photo
 
         N1 = (await app.get_users(c1_id)).mention 
         N2 = (await app.get_users(c2_id)).mention
         
         try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
         except Exception:
            p1 = "RishikaRobot/Love/upic.png"
         try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
         except Exception:
            p2 = "RishikaRobot/Love/upic.png"
            
         img1 = Image.open(f"{p1}")
         img2 = Image.open(f"{p2}")

         img = Image.open("RishikaRobot/Love/HMMM.jpg")

         img1 = img1.resize((390,390))
         img2 = img2.resize((390,390))

         mask = Image.new('L', img1.size, 0)
         draw = ImageDraw.Draw(mask) 
         draw.ellipse((0, 0) + img1.size, fill=255)

         mask1 = Image.new('L', img2.size, 0)
         draw = ImageDraw.Draw(mask1) 
         draw.ellipse((0, 0) + img2.size, fill=255)


         img1.putalpha(mask)
         img2.putalpha(mask1)

         draw = ImageDraw.Draw(img)

         img.paste(img1, (91, 215), img1)
         img.paste(img2, (805, 215), img2)

         img.save(f'test_{cid}.png')
    
         TXT = f"""
❖ ᴛᴏᴅᴀʏ's sᴇʟᴇᴄᴛᴇᴅ ᴄᴏᴜᴘʟᴇs ⏤͟͟͞͞★ 

{N1} + {N2} = ♥️

❖ ɴᴇxᴛ ᴄᴏᴜᴘʟᴇs sᴇʟᴇᴄᴛᴇᴅ ᴏɴ `{tomorrow}`
"""
    
         await message.reply_photo(f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(AVISHA),
    )
         await msg.delete()
         a = upload_file(f"test_{cid}.png")
         for x in a:
           img = "https://graph.org/" + x
           couple = {"c1_id": c1_id, "c2_id": c2_id}
    except Exception as e:
        print(str(e))
    try:
      os.remove(f"./downloads/pfp1.png")
      os.remove(f"./downloads/pfp2.png")
      os.remove(f"test_{cid}.png")
    except Exception:
       pass

    
__help__ = """

 ⬤ /couples ➥ ᴄʜᴏᴏsᴇ 2 ᴜsᴇʀs ᴀɴᴅ sᴇɴᴅ ᴛʜᴇɪʀ ɴᴀᴍᴇ ᴀs ᴄᴏᴜᴘʟᴇs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
 ⬤ /lov <fristuser seconduser> ➥ sʜᴏᴡ ʟᴏᴠᴇ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ.
"""

__mod_name__ = "˹ ᴄᴏᴜᴘʟᴇ ˼"
