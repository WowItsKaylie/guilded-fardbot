#!/usr/bin/python3

import guilded
import os
import random
import subprocess
tokentxt = open('fard-token.txt', 'r')
token = (tokentxt.read())
tokentxt.close()

client = guilded.Client()

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'fard':
        if message.author.id == "mpKYeqQd":
            await message.channel.send('im not talking to you neo')
        else:
            await message.channel.send('fard sex')
        if message.author.id == "VdxE582m":
            await message.channel.send('owner fard sex')
            print('user is a developer')
        else:
            print('user isnt a developer')
        if message.author.id == "d8LQQykd":
            await message.channel.send('fard sex (hi lapi!!!!!)')
    if message.content == 'FARD':
        await message.channel.send('BRAAAAP LOUD FARD!!!! LOUD FARD SEX!!!!!!!!!')
    if message.content == 'pyfard?':
        await message.channel.send('yes')
    if message.content == 'fard, neofetch':
        neofetchOut = subprocess.getoutput("neofetch --stdout")
        await message.channel.send(neofetchOut)
    if message.content == 'fard, home file count':
        fileOut = subprocess.getoutput("find ~/ -type f | wc -l")
        await message.channel.send("there are " + fileOut + " in the user's home directory.")
    if message.content == 'fard, give me your wisdom':
        fortuneOut = subprocess.getoutput("fortune")
        await message.channel.send(fortuneOut)
        print(fortuneOut)
    if message.content == 'fard, test line breaks':
        await message.channel.send("line one\n line two")
client.run(token)
