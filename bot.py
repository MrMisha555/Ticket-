import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), intents=intents)
