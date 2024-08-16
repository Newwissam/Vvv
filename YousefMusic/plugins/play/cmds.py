import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from YousefMusic import app
from config import OWNER_ID, LOGGER_ID, START_IMG_URL
import config

@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"""<b> -› مرحبا بك  </b> {message.from_user.mention} .\n\n<b>-› جميع اوامر البوت موجودة بالقائمة هذي ، اضغط الازرار الي تحت  \n واستكشف ياوحش
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اوامر التشغيل ", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        " اوامرالقناه ", callback_data="zzzch"),
                    InlineKeyboardButton(
                        " اوامرالادمن ", callback_data="zzzad"),

                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],
            ]
        ),
    )

