import os
import asyncio
import discord
import datetime
import threading
from urllib.parse import parse_qs, urlparse
from concurrent.futures import ProcessPoolExecutor

from Modules import MatchFlix
from Modules import Commands as C

os.system('cls')

def getargs(string):

    split = string.split()

    command = ''

    if len(split) < 1:
        return
    else:
        command = split[0]

    commandargs = []
    for word in split:
        commandargs.append(word)

    commandargs.pop(0)

    return (command, commandargs)

async def RegularMessage(message, client):
    if message.content == 'albugo' or message.content == 'albungos':
        await message.channel.send('https://cdn.discordapp.com/attachments/509084581056741377/748618697324757103/b76f85fdd9e180c6977552ed14aafc07.jpg')
    else:
        ct = datetime.datetime.now()
        day = f'{ct.day}/{ct.month}/{ct.year}'
        time = f'{ct.hour}:{ct.minute}'
        print(f'\n\u001b[32;1m[{time}]\u001b[0m\u001b[36;1m <{message.author}\> \u001b[0m{message.content} \u001b[36;1m<\> \u001b[36;1m*in* \u001b[0m{message.guild} - {message.channel}')

async def ProcessCommand(message, client):
    Command = message.content.replace(';','')
    print(f'default : {Command}')
    
    #(command, commandargs) = getargs(Command)

    disCommands = {
        ';help':'show all Commands',
        ';info':'show information about bot',
        ';w2g':'generate a watch2gether room (Slowish)',
        ';rimg':'pull a random image from prnt.src website (possibly NSFW)',
        ';join':'(NOT WORKING) join voice channel',
        ';leave':'(NOT WORKING) leave voice channel',
        ';tom':'(NOT WORKING) play random tom hardy quote (31 quotes)!',
        ';play':'(NOT WORKING) play specific quote'
    }

    eCommands = {
        'help':C.Help,
        'info':C.Info,
        'clear':C.Clear,
        'rimg':C.Randimg,
        'join':C.joinvc,
        'leave':C.leavevc
    }

    command, commandargs = getargs(Command)

    for key in eCommands.keys():
        if command.lower() == key:
            print(f'\n\u001b[33;1m{message.author} just used the command *{key}* in {message.guild} - {message.channel}\u001b[0m')
            await eCommands[key](message, client, commandargs, disCommands)
        elif command.lower() == 'w2g':
            loop = asyncio.get_event_loop()
            p = ProcessPoolExecutor(2)
            loop.run_until_complete(await C.Watch2gether(message))
        else:
            continue


async def MatchflixLink(message, client):
    url = message.content
    obj = urlparse(url)
    q = parse_qs(obj.query)
    movieId = q['jbv']
    
    matchflix = MatchFlix.Matchflix(movieId)
    matchflix.GetCountries()
    matchflix.GetDetails()

    if matchflix.isInSweden() == False:
        inSweden = ':x:'
    else:
        inSweden = ':white_check_mark:'
    if matchflix.isInAmerica() == False:
        inUS = ':x:'
    else:
        inUS = ':white_check_mark:'
    if matchflix.isInUK() == False:
        inUK = ':x:'
    else:
        inUK = ':white_check_mark:'
    
    embed=discord.Embed(title=matchflix.getTitle(), description=matchflix.getSynopsis(), color=0xff0000, url=message.content)
    embed.set_image(url=matchflix.getImg())
    embed.set_author(name="Matchflix", icon_url="https://media.wearemotto.com/wp-content/uploads/2017/01/11012028/What-Netflix-Can-Teach-1920x1080.gif")
    embed.add_field(name="Is in Sweden", value=inSweden, inline=True)
    embed.add_field(name="Is in UK", value=inUK, inline=True)
    embed.add_field(name="Is in US", value=inUS, inline=True)
    embed.set_footer(text=f"{matchflix.getMatlabel()}/{matchflix.getRuntime()}")
    await message.delete()
    await message.channel.send(embed=embed)
    
