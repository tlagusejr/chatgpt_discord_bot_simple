
import discord
from discord.ext import commands
import os
import openai
import sys

# 시스템 인코딩 설정의 출력

openai.api_key = "오픈ai api 코드"

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

messages_json=[
            {},
        ]
bot = commands.Bot(command_prefix='/')
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    query = message.content
    messages_json.append({"role":"user","content":query})
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": query},
        ]
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
    messages_json.append({"role":"assistant","content":answer})
    await message.author.send(answer)

@bot.command()
async def hello(message):
    await message.channel.send('Hi!')
@bot.command()
async def 대화종료(message):
    messages_json=[
            {},
        ]
    await message.channel.send("대화가 종료되었습니다.")
 
bot.run('챗봇 코드')
