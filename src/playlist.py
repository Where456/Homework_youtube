import datetime
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.title = ""
        self.url = ""
        self.videos = []

        self.fetch_playlist_data()

    def fetch_playlist_data(self) -> None:
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_info = youtube.playlists().list(
            part='snippet',
            id=self.playlist_id
        ).execute()

        if 'items' in playlist_info:
            playlist_info = playlist_info['items'][0]
            self.title = playlist_info['snippet']['title']
            self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

            playlist_items = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=self.playlist_id,
                maxResults=50
            ).execute()

            for item in playlist_items.get('items', []):
                video_id = item['contentDetails']['videoId']
                self.videos.append(video_id)

    @property
    def total_duration(self) -> datetime.timedelta:
        total_duration = datetime.timedelta(seconds=0)
        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)

        for video_id in self.videos:
            video_info = youtube.videos().list(
                part='contentDetails',
                id=video_id
            ).execute()

            if 'items' in video_info:
                video_info = video_info['items'][0]
                duration_str = video_info['contentDetails']['duration']

                duration = datetime.timedelta()
                time_parts = duration_str.split('T')
                if len(time_parts) == 2:
                    if 'H' in time_parts[1]:
                        hours, rest = time_parts[1].split('H')
                        duration += datetime.timedelta(hours=int(hours))
                        time_parts[1] = rest
                    if 'M' in time_parts[1]:
                        minutes, rest = time_parts[1].split('M')
                        duration += datetime.timedelta(minutes=int(minutes))
                        time_parts[1] = rest
                    if 'S' in time_parts[1]:
                        seconds = time_parts[1].replace('S', '')
                        duration += datetime.timedelta(seconds=int(seconds))

                total_duration += duration

        return total_duration

    def show_best_video(self) -> str:
        if not self.videos:
            return "No videos in the playlist"

        api_key = 'AIzaSyDpDq-CsLp0jkDsSN_sO-hJLFrG8tag9Mw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        best_video_id = ''
        best_likes = 0

        for video_id in self.videos:
            video_info = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            if 'items' in video_info:
                video_info = video_info['items'][0]
                likes = int(video_info['statistics']['likeCount'])

                if likes > best_likes:
                    best_likes = likes
                    best_video_id = video_id

        if best_video_id:
            return f'https://www.youtube.com/{best_video_id}'
        else:
            return "No liked videos in the playlist"
