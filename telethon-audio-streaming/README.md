# Telethon Audio Streaming 
A streaming service that uses [telethon](https://docs.telethon.dev/en/latest/) to deal with telegram api.  
as telethon uses asyncio library I used [Quart](https://pgjones.gitlab.io/quart/) to write the API and stream the content.  

# Installation

1. Register an application on [telegram api ](https://core.telegram.org/)
2. Create a session file from [here](https://docs.telethon.dev/en/latest/basic/quick-start.html)
3. Create a ```config.json``` file with content   
```json
{
	"api_id": YOUR_API_ID,
	"api_hash": "YOUR_API_HASH",
	"session": "YOUR_SESSION_FILE_NAME"
}
```
4. Install requirments ```pip install -r requirments.txt```
5. Finally run the server ```python3 run.py ```
