import discord
import os
import requests
from dotenv import load_dotenv, dotenv_values
from discord.ext import commands
import json

load_dotenv()

intents = discord.Intents.all()
data = commands.Bot(command_prefix="$", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")


@data.event
async def on_message(message):
    if message.content.startswith("!usd"):
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        response_json = response.json()
        response_usd_rate = response_json["bpi"]["USD"]["rate"]
        with open('pricelist.txt', 'a') as p:
            p.write(response_usd_rate)
        with open('pricelist.txt', 'r') as f:
            price = f.read()
        print(price)
        await message.channel.send(price)

data.run(TOKEN)
