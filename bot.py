# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

botIntents = discord.Intents.default()
botIntents.message_content = True

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(intents=botIntents, command_prefix="?")


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channel = client.get_channel(1009719114023043093)
    await channel.send("Poggers")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '99!':
        response = "123"
        await message.channel.send(response)

@client.event
async def on_reaction_add(reaction, user):
    print("123")
    channel = reaction.message.channel
    await channel.send("let's see")

client.run(TOKEN)