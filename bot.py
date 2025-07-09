import discord
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_DISCORD = os.getenv("TOKEN_DISCORD")
TOKEN_OPENAI = os.getenv("TOKEN_OPENAI")

client_ai = OpenAI(api_key=os.getenv("TOKEN_OPENAI"))

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot {client.user} ligado")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    prompt = message.content.strip()

    if not prompt:
        await message.channel.send("Faça uma pergunta ou me conte algo...")
        return
        
    try:
        resposta = client_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Projeto de BOT conversando com usuário do Discord."},
                {"role": "user", "content": prompt}
            ],
            max_tokens = 100,
            temperature = 0.7
        )

        reply = resposta.choices[0].message.content
        await message.channel.send(reply)

    except Exception as e:
        await message.channel.send("Erro ao gerar uma resposta.")
        print(f"Erro: {e}")

client.run(TOKEN_DISCORD)