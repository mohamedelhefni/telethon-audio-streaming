import json, math
def get_files(files):
        all_files = []
        for file in files:
                attributes = file.media.document.attributes
                # File
                if len(attributes) == 1:
                        fileName = file.media.document.attributes[0].file_name
                if len(attributes) == 2:
                        fileName = file.media.document.attributes[1].file_name

                new_file = {
                        "id": file.id,
                        "channel_id": file.peer_id.channel_id,
                        "name": fileName,
                        "description":  file.message,
                        "type": file.media.document.mime_type,
                        "size": file.media.document.size,
                        "views": file.views,
                        "time": {
                                "duration": file.media.document.attributes[0].duration,
                                "bitsPerSecond": file.media.document.size / file.media.document.attributes[0].duration
                        }
                }
                if new_file['type'] == "audio/mpeg":
                        all_files.append(new_file)
        return all_files 


def paginate(total, page, limit):
        pagination = {}
        pagination['total']  =  total
        pagination['totalPages'] = math.floor(total/limit)
        if page < pagination['totalPages'] :
                pagination['next'] = page + 1
        if page > 1:
                pagination['prev'] = page - 1
        pagination['currentPage']  = page
        
        return pagination