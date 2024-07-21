from pyrogram import Client , filters
from pyrogram.types import Message 
from button.button import *



@Client.on_message(filters.command("start"))
async def Start_Handler(c:Client , m:Message):
    await m.reply_text("HI WELCME CLICK BUTTON" , reply_markup=webapp)