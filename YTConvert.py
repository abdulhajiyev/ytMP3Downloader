from __future__ import unicode_literals
import io
import youtube_dl
import os
import eel
from sys import argv

eel.init('web')


@eel.expose
def generateMusic(data):
    download_options = {
    'format': 'bestaudio/best',
    'outmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }]
}

    with youtube_dl.YoutubeDL(download_options) as dl:
        return dl.download([data])
eel.start('index.html')
