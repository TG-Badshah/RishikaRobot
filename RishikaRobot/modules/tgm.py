from telegraph import upload_file
from pyrogram import filters
from RishikaRobot import pbot as app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["mmmtgm"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("💌")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f"⬤ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➥ {url}")

##############

@app.on_message(filters.command(["mmgraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("💡")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f"⬤ ʏᴏᴜʀ ɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➥ {url}")
  
__help__ = """

 ⬤ /tgm ➥ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ.
 ⬤ /graph ➥ ɢᴇᴛ ɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ.
"""

__mod_name__ = "˹ ɢʀᴀᴘʜ ˼"
