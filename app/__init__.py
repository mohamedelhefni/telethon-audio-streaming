import json,os
import hypercorn.asyncio
from quart import Quart 
from quart_cors import cors
from telethon import TelegramClient

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]
client = TelegramClient(session, api_id, api_hash)

quart_cfg = hypercorn.Config()
quart_cfg.bind = ["0.0.0.0:8000"]
app = Quart(__name__)
app = cors(app, allow_origin="*")

@app.before_serving
async def startup():
        await client.connect()


# After we're done serving (near shutdown), clean up the client
@app.after_serving
async def cleanup():
        await client.disconnect()


from app import routes



async def main():
        await hypercorn.asyncio.serve(app, quart_cfg)
