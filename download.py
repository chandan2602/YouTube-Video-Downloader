# Using the pytube library to download YouTube videos. 
from pytube import YouTube
link=input("enter a youtube video link:")
yt=YouTube(link)
print("title:",yt.title)                  # for video title
print("views:",yt.views)                  # How many views
print("duration:",yt.length)              # Video length/duration
print("description:",yt.description)
print("rating:",yt.rating)
from yt_dlp import YoutubeDL                # Advanced library for downloading youtube video
download_option=input("do you want to download this vedio? (yes/no):").lower()
if download_option=='yes':
    url=link
    ydl_opts={'format':'best'}
    with YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")
        ydl.download([url])
        print("download complited")
else:
    print("Download aborted.")