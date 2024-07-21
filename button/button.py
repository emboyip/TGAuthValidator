from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup , WebAppInfo
from var.var import url

webapp = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="click" , web_app=WebAppInfo(url=url))]
    ]
)