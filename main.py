#inb4 "use this encryption library you moron": shut it nerd, dont be an idiot!
import auth 
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_message(message):
    print(message.content)
    if "x.com" in message.content.lower() or "twitter.com" in message.content.lower():
        await message.delete()
bot.run(auth.token)