import discord
import os
from dotenv import load_dotenv, dotenv_values
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)

