import json
import hypercorn.asyncio
from quart import Quart 
from quart_cors import cors
from telethon import TelegramClient

with open('config.json') as config_file:
        data = json.load(config_file)
        api_id = data['api_id']
        api_hash = data['api_hash']
        session = data['session']


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
