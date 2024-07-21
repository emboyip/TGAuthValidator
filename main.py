from pyrogram import Client
from var.var import *


plugin = dict(root="plugin")

app = Client(
    name="emboy",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=plugin
)


app.run()