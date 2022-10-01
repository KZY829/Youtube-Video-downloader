from __future__ import unicode_literals
import youtube_dl

url = input('ダウンロードしたい動画のURLをはってください。>> ')
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print('ダウンロードが完了しました。')
