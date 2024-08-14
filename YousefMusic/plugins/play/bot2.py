import asyncio
import random
from pyrogram import enums
from pyrogram import types
from YousefMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from YousefMusic import app
from config import *

bot_name = {}

name = "بوت"

Mazen_responses = [
    "انا بوت خاص ب تشغيل الميوزك   ،",
    "امر كيف يمكنني مساعدتك ⋅",
    "نعم يا عيوني  ،",
    "امرني انا بوت تشغيل الميوزك "
    "ارحب انابوت خاص بالموسيقه",
    " ياهلا امرني كيف يمكنني مساعدتك",
    "من خلالي يمكنك تشغيل الميوزك  ",
]

@app.on_message(filters.command(["بوت", "ديا"], ""), group=71135)
async def Mazen_bot(client, message):
    
    bot_username = (await app.get_me()).username
    bar = random.choice(Mazen_responses).format(name)
    await message.reply_text(
        text=f"{bar}",
        disable_web_page_preview=True,
    parse_mode=enums.ParseMode.MARKDOWN)
