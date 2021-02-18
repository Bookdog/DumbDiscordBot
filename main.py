import discord
import os
import requests
import json
import random

from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you use my worthless commands'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

    #Help command

  if message.content.startswith('$help'):
    await message.channel.send('DumbBot has only a few commands! The prefix it goes by is `$`.')

    #Utility Commands

  if message.content.startswith('$invite'):
    await message.channel.send('Invite me here: https://discord.com/api/oauth2/authorize?client_id=805835541764767804&permissions=388160&scope=bot')

  if message.content.startswith('$hi'):
    list = ["Hiya!", "Yo!", "Wassup!", "Hello!"]
    await message.channel.send(random.choice(list))

  if message.content.startswith('$coinflip'):
    list = ["The coin landed on Heads!", "The coin landed on Tails!"] 
    await message.channel.send(random.choice(list))

  if message.content.startswith('$dice'):
    list = ["One", "Two", "Three", "Four", "Five", "Six"]
    await message.channel.send(random.choice(list))
  
    #Game 

  if message.content.startswith('$wyr'):
    wyrList = ["Would you rather drown or be burned alive?", "Would you rather lose the ability to read or lose the ability to speak?", "Would you rather be covered in fur or covered in scales?", " Would you rather be in jail for a year or lose a year off your life?", "Would you rather always be 10 minutes late or always be 20 minutes early?", "Would you rather have all traffic lights you approach be green or never have to stand in line again?", " Would you rather give up all drinks except for water or give up eating anything that was cooked in an oven?", "Would you rather be able to see 10 minutes into your own future or 10 minutes into the future of anyone but yourself?", "Would you rather have an easy job working for someone else or work for yourself but work incredibly hard?", "Would you rather be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?", "Would you rather go back to age 5 with everything you know now or know now everything your future self will learn?", "Would you rather have unlimited international first-class tickets or never have to pay for food at restaurants?", "Would you rather see what was behind every closed door or be able to guess the combination of every safe on the first try?", "Would you rather be an average person in the present or a king of a large country 2500 years ago?", " Would you rather move to a new city or town every week or never be able to leave the city or town you were born in?", "Would you rather be a reverse centaur or a reverse mermaid/merman?", "Would you rather only be to use a fork (no spoon) or only be able to use a spoon (no fork)?", " Would you rather be a famous director or a famous actor?", "Would you rather live in a cave or live in a tree house?", "Would you rather be able to control fire or water?", "Would you rather live without the internet or live without AC and heating?", "Would you rather be able to teleport anywhere or be able to read minds?", "Would you rather be unable to use search engines or unable to use social media?", "Would you rather be beautiful/handsome but stupid or intelligent but ugly?", "Would you rather be famous but ridiculed or be just a normal person?", "Would you rather have a flying carpet or a car that can drive underwater?", "Would you rather never be stuck in traffic again or never get another cold?", "Would you rather be forced to eat only spicy food or only incredibly bland food?", "Would you rather be a bowling champion or a curling champion?", "Would you rather live on the beach or in a cabin in the woods?", "Would you rather be completely invisible for one day or be able to fly for one day?", "Would you rather never be able to drink sodas like coke again or only be able to drink sodas and nothing else?", "Would you rather give up watching TV/movies for a year or give up playing games for a year?", "Would you rather have amazingly fast typing/texting speed or be able to read ridiculously fast?"]
    await message.channel.send(random.choice(wyrList))

keep_alive()
client.run(os.getenv('TOKEN'))