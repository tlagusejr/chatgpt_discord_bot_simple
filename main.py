
import discord
from discord.ext import commands
import os
import openai
import sys

# 시스템 인코딩 설정의 출력

openai.api_key = "오픈ai api 키"

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

messages_json=[]
bot = commands.Bot(command_prefix='/')
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
@bot.event
async def on_message(message):
    global messages_json
    if message.author == bot.user:
        return
    
    query = message.content
    query = query[1:]
    if query == "대화종료":
        messages_json=[]
        print("대화가 종료되었습니다.")
        
        await message.author.send("대화 종료")
    else:

        messages_json.append({"role":"user","content":query})
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "user", "content": query},
            ]
        )
        answer = response['choices'][0]['message']['content']
        print(answer)
        print(messages_json)
        messages_json.append({"role":"assistant","content":answer})
        await message.author.send(answer)

 
bot.run('')
