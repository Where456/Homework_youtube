from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.title = None
        self.url = None
        self.views = None
        self.likes = None

        self.fetch_video_data()

    def fetch_video_data(self) -> None:
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        try:
            video_info = youtube.videos().list(
                part='snippet,statistics',
                id=self.video_id
            ).execute()

            if 'items' in video_info:
                video_info = video_info['items'][0]
                self.title = video_info['snippet']['title']
                self.url = f'https://www.youtube.com/watch?v={self.video_id}'
                self.views = int(video_info['statistics']['viewCount'])
                self.likes = int(video_info['statistics']['likeCount'])
        except Exception:
            print('Передан несуществующий id видео')

    def __str__(self) -> str:
        return self.title


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
