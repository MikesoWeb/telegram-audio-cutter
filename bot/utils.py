import os
from .config import FOLDER_PATH

def get_song_list():
    song_list = []
    supported_formats = [".mp3"]

    for file_name in os.listdir(FOLDER_PATH):
        if os.path.isfile(os.path.join(FOLDER_PATH, file_name)):
            file_ext = os.path.splitext(file_name)[1]
            if file_ext.lower() in supported_formats:
                song_list.append(file_name)

    return song_list