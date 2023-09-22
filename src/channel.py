import json
import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
class Channel:

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.title = ""
        self.description = ""
        self.url = ""
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0

        self.fetch_channel_data()

    def print_info(self) -> str:
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        return build('youtube', 'v3', developerKey=api_key)

    def fetch_channel_data(self) -> None:
        """
        Получает данные о канале с использованием YouTube API и заполняет соответствующие атрибуты экземпляра.
        """
        youtube = self.get_service()
        channel_info = youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()

        if 'items' in channel_info:
            channel_info = channel_info['items'][0]
            self.title = channel_info['snippet']['title']
            self.description = channel_info['snippet']['description']
            self.url = f'https://www.youtube.com/channel/{self.channel_id}'
            self.subscriber_count = int(channel_info['statistics']['subscriberCount'])
            self.video_count = int(channel_info['statistics']['videoCount'])
            self.view_count = int(channel_info['statistics']['viewCount'])

    def to_json(self, filename):
        data = {
            'channel_id': self.channel_id,
            'name': self.title,
            'description': self.description,
            'link': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

