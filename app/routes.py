from quart import render_template_string, request, Response, stream_with_context 
from app import app, client
from app.utils import getFiles
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterDocument, InputMessagesFilterMusic


@app.route("/channel/<string:channel>")
async def getChannelFiles(channel):
        files = await client.get_messages(channel, limit=100, filter=InputMessagesFilterMusic)
        return getFiles(files)

@app.route("/files")
async def list():
        files = await client.get_messages(channel, limit=100, filter=InputMessagesFilterMusic)
        return getFiles(files)




@app.route('/stream/<channel>/<id>')
async def streamChannelFile(channel, id):
        getOffset = request.args.get('offset')
        offset= getOffset if getOffset is not None else 0
        file = await client.get_messages(channel, ids=int(id), filter=InputMessagesFilterMusic)
        async def stream(file):
                global client
                async for chunk in client.iter_download(file, offset=int(offset)):
                        yield chunk
        return Response(stream(file), mimetype="audio/x-wav", headers={"Accept-Ranges": "bytes"})



@app.route('/stream/<id>')
async def get(id):
        if id:
                getOffset = request.args.get('offset')
                offset = getOffset if getOffset is not None else 0
                file = await client.get_messages(channel, ids=int(id), filter=InputMessagesFilterMusic)
                async def stream(file):
                        global client
                        async for chunk in client.iter_download(file, offset=int(offset)):
                                yield chunk

        return Response(stream(file), mimetype="audio/x-wav", headers={"Accept-Ranges": "bytes"})


@app.route('/download/<id>')
async def downloadfile(id):
        if id:
                getOffset = request.args.get('offset')
                print(getOffset)
                offset = getOffset if getOffset is not None else 0
                file = await client.get_messages(channel, ids=int(id), filter=InputMessagesFilterMusic)
                @stream_with_context
                async def download(file):
                        global client
                        async for chunk in client.iter_download(file, offset=int(offset)):
                                yield chunk

        return Response(download(file), mimetype="audio/x-wav")

