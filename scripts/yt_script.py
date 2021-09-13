import youtube_dl
import os

class YoutubeDL:
    def hook(self, d):
        verbose = False
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Finished downloading {}".format(file_tuple[1]))
        if d['status'] == 'downloading' and verbose == True:
            print()

    def __init__(self):
        playlist = 'xxx'
        directory = '/home/faust/watch_later/'
        archive = directory+ 'archive.txt'
        disallowed = "'.!:;-|,/"

        with youtube_dl.YoutubeDL() as ydl:
            playlist_dict = ydl.extract_info(playlist, download=False)
            for video in playlist_dict['entries']:
                filename = video['title'].replace(' ', '_').lower().replace('&', 'and')
                for c in disallowed:
                    filename = filename.replace(c, "")
                filename = filename.replace("__", "_")

                ydl_opts = {
                    'format': 'bestvideo+bestaudio/best',
                    'progress_hooks': [self.hook],
                    'download_archive': archive,
                    'outtmpl': directory + filename
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video['webpage_url']])

ytdl = YoutubeDL()
