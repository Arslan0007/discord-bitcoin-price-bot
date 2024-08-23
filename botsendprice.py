import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
import json
import pprint


load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command(description="Returns all commands")
async def commands(self):
    help_command = [c.name for c in self.client.commands]
    print(help_command)

@bot.command(name="price")
async def get_bitcoin_price(ctx, currency):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response_json = response.json()
    price = response_json['bpi'][currency]['rate']
    print(price)
    if currency == "USD":
        await ctx.channel.send(price)
    elif currency == "EUR":
        await ctx.channel.send(price)
    elif currency == "GBP":
        await ctx.channel.send(price)
    else:
        pass
bot.run(TOKEN)
