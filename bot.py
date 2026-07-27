import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bejelentkezve: {bot.user}")

    print("Szerverek:")
    for guild in bot.guilds:
        print(f"- {guild.name} ({guild.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)