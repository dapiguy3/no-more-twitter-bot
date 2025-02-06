"""i'm keeping this bot super simple. documentation will remain minimal. good luck!"""

#this local file contains your token. dont share it. dont stream it.
#inb4 "use this encryption library you moron": shut it nerd, dont be an idiot!
import auth 

#imports specifically for discord api
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
#this is the actual bot object.
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("bot is live")


@bot.event
async def on_message(message):
    print(message.content)
    if "x.com" in message.content.lower() or "twitter.com" in message.content.lower():
        await message.delete()

bot.run(auth.token)