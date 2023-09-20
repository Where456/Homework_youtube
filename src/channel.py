import json
from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id

    def print_info(self) -> str:
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)
