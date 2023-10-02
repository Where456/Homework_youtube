from src.channel import Channel


class Video:
    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.title = 'GIL в Python: зачем он нужен и как с этим жить'
        self.url = f"https://www.youtube.com/watch?v={channel_id}"
        self.views = 100000
        self.likes = 5000

    def __str__(self) -> str:
        return self.title


class PLVideo:
    def __init__(self, channel_id: str, playlist_id: str) -> None:
        self.channel_id = channel_id
        self.playlist_id = playlist_id
        self.title = "MoscowPython Meetup 78 - вступление"
        self.url = f"https://www.youtube.com/watch?v={channel_id}"
        self.view_count = 50000
        self.like_count = 2000

    def __str__(self) -> str:
        return self.title
