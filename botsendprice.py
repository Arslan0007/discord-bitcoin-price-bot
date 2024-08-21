import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
import json
import pandas as pd
from sqlalchemy.orm.sync import update

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
        with open('pricelist_usd.txt', 'w') as p:
            p.write(price)
        with open('pricelist_usd.txt', 'r') as f:
            price_currency = f.read()
        await ctx.channel.send(price_currency)
    elif currency == "EUR":
        with open('pricelist_eur.txt', 'w') as p:
            p.write(price)
        with open('pricelist_eur.txt', 'r') as f:
            price_currency = f.read()
        await ctx.channel.send(price_currency)
    elif currency == "GBP":
        with open('pricelist_gbp.txt', 'w') as p:
            p.write(price)
        with open('pricelist_gbp.txt', 'r') as f:
            price_currency = f.read()
        await ctx.channel.send(price_currency)
    else:
        pass
bot.run(TOKEN)
