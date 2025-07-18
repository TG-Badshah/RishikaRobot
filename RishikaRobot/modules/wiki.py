import wikipedia
from telegram import ParseMode, Update
from telegram.ext import CallbackContext
from wikipedia.exceptions import DisambiguationError, PageError

from RishikaRobot import dispatcher
from RishikaRobot.modules.disable import DisableAbleCommandHandler


def wiki(update: Update, context: CallbackContext):
    msg = (
        update.effective_message.reply_to_message
        if update.effective_message.reply_to_message
        else update.effective_message
    )
    res = ""
    if msg == update.effective_message:
        search = msg.text.split(" ", maxsplit=1)[1]
    else:
        search = msg.text
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        update.message.reply_text(
            "⬤ ᴅɪsᴀᴍʙɪɢᴜᴀᴛᴇᴅ ᴘᴀɢᴇs ғᴏᴜɴᴅ ! ᴀᴅᴊᴜsᴛ ʏᴏᴜʀ ǫᴜᴇʀʏ ᴀᴄᴄᴏʀᴅɪɴɢʟʏ.\n❍ <i>{}</i>".format(
                e
            ),
            parse_mode=ParseMode.HTML,
        )
    except PageError as e:
        update.message.reply_text(
            "⬤ <code>{}</code>".format(e), parse_mode=ParseMode.HTML
        )
    if res:
        result = f"⬤ <b>{search}</b>\n\n"
        result += f"⬤ <i>{res}</i>\n"
        result += f"""⬤ <a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">ʀᴇᴀᴅ ᴍᴏʀᴇ...</a>"""
        if len(result) > 4000:
            with open("result.txt", "w") as f:
                f.write(f"⬤ {result}\n\n⬤ ᴜᴡᴜ ᴏᴡᴏ ᴏᴍᴏ ᴜᴍᴜ")
            with open("result.txt", "rb") as f:
                context.bot.send_document(
                    document=f,
                    filename=f.name,
                    reply_to_message_id=update.message.message_id,
                    chat_id=update.effective_chat.id,
                    parse_mode=ParseMode.HTML,
                )
        else:
            update.message.reply_text(
                result, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            )


WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, run_async=True)
dispatcher.add_handler(WIKI_HANDLER)

__help__ = """

⬤ /wiki (text) *➥* sᴇᴀʀᴄʜs ᴀʙᴏᴜᴛ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡɪᴋɪᴘᴇᴅɪᴀ.
"""
__mod_name__ = "˹ ᴡɪᴋɪ ˼"
