import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from RishikaRobot import dispatcher
from RishikaRobot.modules.disable import DisableAbleCommandHandler


def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_text = f'*⬤ ᴡᴏʀᴅ ➥ {text}*\n\n❅ ᴅᴇғɪɴɪᴛɪᴏɴ ➥\n{results["list"][0]["definition"]}\n\n✦ ᴇxᴀᴍᴘʟᴇ ➠\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "⬤ ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud, run_async=True)

dispatcher.add_handler(UD_HANDLER)

__help__ = """

⬤ /ud (text) *➥* sᴇᴀʀᴄʜs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴜʀʙᴀɴ ᴅɪᴄᴛɪᴏɴᴀʀʏ ᴀɴᴅ sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
"""
__mod_name__ = "˹ ᴅɪᴄᴛɪᴏɴᴀʀʏ ˼"

__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]
