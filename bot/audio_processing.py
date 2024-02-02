import os
from pydub import AudioSegment
from bot.config import FOLDER_PATH
from bot.utils import get_song_list


def process_song_choice(message):
    from bot.telegram_bot import bot
    try:
        choice = int(message.text.strip()) - 1
        songs = get_song_list()

        if 0 <= choice < len(songs):
            songs_path = os.path.join(FOLDER_PATH, songs[choice])
            song_name, song_ext = os.path.splitext(songs[choice])
            demo_song_path = os.path.join(FOLDER_PATH, f"{song_name}_demo{song_ext}")

            audio = AudioSegment.from_file(songs_path)
            demo_audio = audio[:30000]
            demo_audio.export(demo_song_path, format=song_ext[1:])

            if os.path.exists(demo_song_path):
                with open(demo_song_path, "rb") as audio_file:
                    bot.send_audio(message.chat.id, audio_file)

                os.remove(demo_song_path) # Удаляем временный файл

            else:
                bot.send_message(message.chat.id, "Произошла ошибка при обработке песни.")
        else:
            bot.send_message(message.chat.id, "Ошибка выбора трека")

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")