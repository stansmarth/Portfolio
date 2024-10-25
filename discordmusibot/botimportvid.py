import youtube_dl as ytdl
import discord



    def __init__(self, url, requested_by):

        with ytdl.YoutubeDL(YTDL_OPTS) as ydl:
            video = self._get_info(url)
            video_format = video["formats"][0]
            self.stream_url = video_format["url"]
            self.video_url = video["webpage_url"]
            self.title = video["title"]

    def _get_info(self, video_url):
        with ytdl.YoutubeDL(YTDL_OPTS) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video = None
            if "_type" in info and info["_type"] == "playlist":
                return self._get_info(
                    info["entries"][0]["url"])  
            else:
                video = info
            return video
