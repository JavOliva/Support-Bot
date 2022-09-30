import discord
from personal_bot_token import token


client = discord.Client(intents=discord.Intents.default())

client.run(token)