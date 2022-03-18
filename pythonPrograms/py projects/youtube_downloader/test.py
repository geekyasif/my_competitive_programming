from pytube import YouTube, Playlist
from pytube.cli import on_progress

url = input("Enter url : ")
yt = Playlist(url)
# yt = YouTube(url, on_progress_callback=on_progress)
for i in yt.streams:
    print(str(yt.streams.index(i)+1)  + "\tType: " + str(i.mime_type) + "| Res: " +  str(i.resolution) + " | FPS: " + str(i.fps))