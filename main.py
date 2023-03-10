
import discord
from discord.ext import commands
import os
import openai
import sys

openai.api_key = "openapi_key"

model = "gpt-3.5-turbo"


bot = commands.Bot(command_prefix='!')
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    query = message.content
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": query},
        ]
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
    await message.author.send(answer)

@bot.command()
async def hello(message):
    await message.channel.send('Hi!')
 
bot.run('discord_api_key')
