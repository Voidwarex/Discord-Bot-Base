import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
from colorama import init, Fore, Back, Style
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {Fore.CYAN}{bot.user.name}{Fore.WHITE}')

bot.run('TOKEN_GOES_HERE')
