from .. import bot
from telethon import events
import asyncio
#import openai
#openai.my_api_id=openai_key


@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
  await event.reply("Hello This is K Bot")

  
@bot.on(events.NewMessage(incoming=True, pattern="/get"))
async def start(event):
  await event.reply("Hello This is get command")
 
