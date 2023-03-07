import discord
from discord.ext import commands
import json
import requests

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)


@client.event
async def on_ready():
    print("Logged in as a bot")
    await client.change_presence(activity=discord.Game(name="Love BTC"))

@client.command()
async def btc(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="BTC Price", description="Live Tracking of BTC Price, powered by Binance API.", color=0xf7931a)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def eth(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="ETH Price", description="Live Tracking of ETH Price, powered by Binance API.", color=0x2f3030)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def bnb(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="BNB Price", description="Live Tracking of BNB Price, powered by Binance API.", color=0xf0b90b)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def xpr(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=XPRUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="XRP Price", description="Live Tracking of XPR Price, powered by Binance API.", color=0x23292f)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/52.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def ada(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="Cardano Price", description="Live Tracking of ADA Price, powered by Binance API.", color=0x0334af)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def doge(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="DOGE Price", description="Live Tracking of DOGE Price, powered by Binance API.", color=0xba9f33)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/74.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def matic(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=MATICUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="POLYGON Price", description="Live Tracking of MATIC Price, powered by Binance API.", color=0x9033d3)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def sol(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="SOL Price", description="Live Tracking of SOL Price, powered by Binance API.", color=0x000000)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def dot(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=DOTUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="DOT Price", description="Live Tracking of DOT Price, powered by Binance API.", color=0xe5007a)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def ltc(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="LTC Price", description="Live Tracking of LTC Price, powered by Binance API.", color=0x6a8bbb)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/2.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def shib(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=SHIBUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="SHIB Price", description="Live Tracking of SHIB Price, powered by Binance API.", color=0xea3c25)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def trx(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=TRXUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="TRX Price", description="Live Tracking of TRX Price, powered by Binance API.", color=0xff0013)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/1958.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def xmr(ctx):
        key = "https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT"
        data = requests.get(key)  
        data = data.json()
        embedVar = discord.Embed(title="XMR Price", description="Live Tracking of XMR Price, powered by Binance API.", color=0xfa6800)
        embedVar.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/328.png")
        embedVar.add_field(name="Price:", value=f"{data['price']}", inline=False)
        embedVar.set_footer(text="Crypto Discord Bot, made by Alexander Leontaridis.")
        await ctx.send(embed=embedVar)

@client.command()
async def command_list(ctx):
        embed=discord.Embed(title="Crypto Bot Help.", description="List of all Crypto Bot Commands:", color=0x3478fe)
        embed.add_field(name="BTC Price:", value="!btc", inline=False)
        embed.add_field(name="ETH Price:", value="!eth", inline=False)
        embed.add_field(name="BNB Price:", value="!bnb", inline=False)
        embed.add_field(name="XPR Price:", value="!xpr", inline=False)
        embed.add_field(name="ADA Price:", value="!ada", inline=False)
        embed.add_field(name="DOGE  Price:", value="!doge", inline=False)
        embed.add_field(name="MATIC Price:", value="!matic", inline=False)
        embed.add_field(name="SOL Price:", value="!sol", inline=False)
        embed.add_field(name="DOT Price:", value="!dot", inline=False)
        embed.add_field(name="LTC Price:", value="!ltc", inline=False)
        embed.add_field(name="SHIB Price:", value="!shib", inline=False)
        embed.add_field(name="TRX Price:", value="!trx", inline=False)
        embed.add_field(name="XMR Price:", value="!xmr", inline=False)
        await ctx.send(embed=embed)

client.run("[Enter Token]")



  
