#(©)@EdgeBots

from pyrogram import __version__

import config
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"""<b>╭───────────⍟
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='tg://user?id={5543390445}'>Aaru</a>
├➽ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├➽ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3</a>
├➽ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href=https://t.me/Lusty_Leaks>Lusty Leaks</a>
├➽ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href=https://t.me/Adult_18_Contents>Adult 18 Contents</a>
├➽ Mᴀɪɴ Gʀᴏᴜᴘ : <a href=https://t.me/Lusty_Leaks>Lusty Leaks</a></b>
╰───────────────⍟ """,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝙲𝚕𝚘𝚜𝚎", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
