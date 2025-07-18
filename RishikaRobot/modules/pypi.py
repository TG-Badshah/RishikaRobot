from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from RishikaRobot import pbot as app

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/AlisaMusicRobot?startgroup=true"),
    ],
]

def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        # Sending a request to the PyPI API
        response = requests.get(api_url)
        
        # Extracting information from the API response
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"⬤ Error fetching PyPI information ➥ {e}")
        return None

@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        # Getting information from PyPI
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            # Creating a message with PyPI information
            info_message = f"❖ ᴘᴀᴄᴋᴀɢᴇ ɴᴀᴍᴇ ➥ `{pypi_info['info']['name']}`\n\n" \
                           f"● ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ ➥ `{pypi_info['info']['version']}`\n\n" \
                           f"● ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➥ {pypi_info['info']['summary']}\n\n" \
                           f"❖ ᴘʀᴏᴊᴇᴄᴛ ᴜʀʟ ➥ {pypi_info['info']['project_urls']['Homepage']}"
            
            
            client.send_message(message.chat.id, info_message, reply_markup=InlineKeyboardMarkup(EVAA),
    )
        
        else:
            # Handling the case where information retrieval failed
            client.send_message(message.chat.id, "⬤ Failed to fetch information from PyPI.")
    
    except IndexError:

        client.send_message(message.chat.id, "⬤ Please provide a package name after the /pypi command.")

__help__ = """

⬤ /pypi * ➥* ᴄʜᴇᴄᴋ ʟᴇᴀᴛᴇsᴛ ᴘʏᴘɪ ᴠᴇʀsɪᴏɴ ғᴏʀ ʀᴇᴘᴏ.
"""

__mod_name__ = "˹ ᴘʏᴘɪ ˼"
