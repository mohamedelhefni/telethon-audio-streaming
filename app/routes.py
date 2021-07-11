import json
from quart import render_template_string, request, Response, stream_with_context 
from app import app, client
from app.utils import getFiles, paginate
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument, InputMessagesFilterMusic


@app.route("/channel/<string:channel>")
@app.route("/channel/<string:channel>/page/<int:page>")
async def getChannelAudioFiles(channel, page=0):
        offset = page if page > 1 else 0
        limit = 99
        files = await client.get_messages(channel, limit=limit,add_offset=(offset  * limit), filter=InputMessagesFilterMusic)
        return json.dumps({"files": getFiles(files), "pagination":  paginate(files.total, page,  limit) }) 



@app.route('/stream/<string:channel>/<int:id>')
async def streamChannelFile(channel, id):
        getOffset = request.args.get('offset')
        offset= getOffset if getOffset is not None else 0
        file = await client.get_messages(channel, ids=id, filter=InputMessagesFilterMusic)
        async def stream(file):
                global client
                async for chunk in client.iter_download(file, offset=int(offset)):
                        yield chunk
        return Response(stream(file), mimetype="audio/x-wav", headers={"Accept-Ranges": "bytes"})


@app.route('/download/<string:channel>/<int:id>')
async def downloadChannelFile(channel, id):
        if id:
                getOffset = request.args.get('offset')
                offset = getOffset if getOffset is not None else 0
                file = await client.get_messages(channel, ids=id, filter=InputMessagesFilterMusic)
                @stream_with_context
                async def download(file):
                        global client
                        async for chunk in client.iter_download(file, offset=int(offset)):
                                yield chunk

        return Response(download(file), mimetype="audio/x-wav")

