import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
import json

from soupsieve.util import lower

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
    # define the source
    # fetch data from source
    # convert data to json because it is easy to fetch specific data as json
    # convert to lowercase
    # define a parameter to fetch USD/EUR/GBP
    # fetch a rate word
    url = "https://api.coindesk.com/v1/bpi/currentprice.json" # define the source
    response = requests.get(url) # fetching data with request from defined source
    response_json = response.json() # converting data to json
    price_cur = response_json['bpi'] # fetching specific area to find related currency
    price_cur_lower = json.loads(json.dumps(price_cur).lower()) # convert to lowercase
    price_cur_rate = price_cur_lower[currency]['rate'] # fetching related rate
    await ctx.channel.send(price_cur_rate) # send the result

bot.run(TOKEN)
