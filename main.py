from pytube import YouTube
from moviepy.editor import *
import os

def convert_to_mp3(video_url):
    try:
        yt = YouTube(video_url)

        video = yt.streams.get_highest_resolution()
        video.download()

        video_path = video.default_filename

        print(f"Video indirildi: {video_path}")
        mp4_file = video_path
        mp3_file = video_path[:-4] + '.mp3'
        video = VideoFileClip(mp4_file)
        video.audio.write_audiofile(mp3_file)

        video.close()
        os.remove(mp4_file)

        print(f"MP3 dosyası '{mp3_file}' başarıyla oluşturuldu!")

    except Exception as e:
        print(f"Error: {str(e)}")
video_url = input("Youtube video URL'si girin: ")
convert_to_mp3(video_url)
