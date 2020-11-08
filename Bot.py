import os
import json
import time
import discord
import threading
import numpy as np  

from Modules.cmdcolors import *
from Modules import Commands as C
from Modules import CommandHandler as CH

os.system('cls')

class OdinBot(discord.Client):
    
    async def on_ready(self):
        print(f'{BRIGHT_GREEN}Logged in as {self.user}{CLEAR}')
        await C.randStatus(client)

        client.loop.create_task(C.randStatus(client))
    
    async def on_message(self, message):
        if ';;' in message.content:
            return
        else:
            if (message.content.startswith(';')):
                await CH.ProcessCommand(message, client)

        if (not message.content.startswith(';')):
            await CH.RegularMessage(message, client)
            
f = open('config.json')
config = json.load(f)

client = OdinBot()
try:
    client.run(config['token'])
except Exception as e:
    print(e)
    print(f'{BRIGHT_RED}[!]{CLEAR} no internet connection')