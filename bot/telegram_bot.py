import telebot
from bot.config import BOT_API_KEY
from bot.utils import get_song_list
from bot.audio_processing import process_song_choice

bot = telebot.TeleBot(BOT_API_KEY)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    commands = [
        "/start - показать список команд",
        "/playlist - показать плейлист песен",
        "/help - справка"
    ]
    bot.send_message(message.chat.id, "Добро пожаловать. Вот список доступных команд:\n" + "\n".join(commands))


@bot.message_handler(commands=["help"])
def send_help(message):
    help_message = """
    Этот бот позволяет тебе:

    1. Просматривать доступные треки в плейлисте с помощью команды /playlist.
    2. Прослушивать демоверсии треков прямо в Telegram, выбрав песню из плейлиста.
    3. Получать помощь и информацию о доступных командах с помощью команды /help.

    Просто отправь мне одну из этих команд, и я буду рад помочь тебе наслаждаться музыкой прямо в твоем чате!
    """
    bot.send_message(message.chat.id, help_message)



@bot.message_handler(commands=["playlist"])
def send_playlist(message):
    try:
        songs = get_song_list()

        if songs:
            playlist = "\n".join([f"{index + 1}. {song}" for index, song in enumerate(songs)])
            bot.send_message(message.chat.id, f"Текущий плейлист:\n{playlist}")
            bot.send_message(message.chat.id, "Введите номер трека из плейлиста, например 3. Вы можете прослушать демоверсию трека, первые 30 секунд.")
            bot.register_next_step_handler(message, process_song_choice)

        else:
            bot.send_message(message.chat.id, "Плейлист не доступен!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")