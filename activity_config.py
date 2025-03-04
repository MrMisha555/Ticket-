import os
from dotenv import load_dotenv
import discord

# Загружаем переменные из .env
load_dotenv()

# Читаем настройки из .env или задаём значения по умолчанию
BOT_STATUS_MESSAGE = os.getenv("BOT_STATUS_MESSAGE", "Смотрит на ваши Ticket's")
BOT_STATUS_TYPE = os.getenv("BOT_STATUS_TYPE", "Watching")

# Словарь с типами активности
STATUS_TYPES = {
    "Playing": discord.ActivityType.playing,
    "Streaming": discord.ActivityType.streaming,
    "Watching": discord.ActivityType.watching,
    "Listening": discord.ActivityType.listening
}

# Определяем тип активности (по умолчанию Watching)
ACTIVITY_TYPE = STATUS_TYPES.get(BOT_STATUS_TYPE, discord.ActivityType.watching)

# Создаём объект активности
BOT_ACTIVITY = discord.Activity(type=ACTIVITY_TYPE, name=BOT_STATUS_MESSAGE)
