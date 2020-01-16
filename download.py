import youtube_dl
import os
from utils import createdir

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download(link,path=os.getcwd()):

    dpath = os.path.join(path, "downloads")
    createdir(dpath)

    vid_name = '%(title)s.%(ext)s'

    vid_path = os.path.join(dpath,vid_name)

    ydl_opts = {
        'format': 'best',
        'logger': MyLogger(),
        'outtmpl': vid_path,
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    return str(os.path.dirname(ydl.prepare_filename(ydl_opts)))
