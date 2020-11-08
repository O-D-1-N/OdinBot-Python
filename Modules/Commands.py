import os
import discord
import asyncio
import ffmpeg
import youtube_dl
import random as rand
import requests as req
from discord.utils import get
from discord.ext import commands

from . import Rimg

triggers = {
    'Arthur!.mp3': 'arthur!',
    'Shalom.mp3': 'shalom',
    'Yeah_i_knew.mp3': 'yeah i knew yeno',
    'a_proper_shoot_out.mp3': 'proper shootout',
    'cryin_out_loud.mp3': 'cryin out loud',
    'die_by_sword.mp3': 'die by the sword',
    'fkn_stand_there_juding_me.mp3': 'stand there judging me',
    'get_it_on_my_back.mp3': 'get it on my back',
    'get_out_my_way.mp3': 'get out my fkn way',
    'give_ron_your_sausage.mp3': 'give ron sausage',
    'i prefer boys.mp3': 'i prefer boys',
    'i_did_not_know.mp3': 'i did not know',
    'i_had_a_negro_once.mp3': 'ron doesnt discriminate',
    'its_a_rolling_pin.mp3': 'its a fkn rolling pin',
    'lemon_sherbet.mp3': 'lemon sherbet',
    'lets_hav_it.mp3': 'lets have it',
    'like_a_western.mp3': 'western',
    'not_in_my_Arse.mp3': 'not in my arse',
    'pour_a_pint.mp3': 'pour a pint',
    'quicker!.mp3': 'quicker!',
    'shoot_out_is_a_shoot_out.mp3': 'a shootout is a shootout',
    'shut_ya_mouth.mp3': 'shut ya mouth',
    'spare_me_pact.mp3': 'spare me',
    'thats_noice_init.mp3': 'thats nice init',
    'u_fukin_wot.mp3': 'u fucking wot',
    'wankers.mp3': 'wankers',
    'what_fkn_line.mp3': 'what fkn line',
    'what_is_that.mp3': 'what is that',
    'who_r_u.mp3': 'who r u',
    'yeah_it_is.mp3': 'yeah it is',
    'you_cunt!.mp3': 'you cunt!'
}

async def Help(ctx, client=None, args=None, commands=None):

    if len(args) < 1:
        embed = discord.Embed(title = 'Commands', color=0xff0000)
        for command in commands.keys():
            embed.add_field(name=f'`{command}`', value=commands[command], inline=False)
        await ctx.channel.send(embed=embed)
    elif args[0] == 'play':

        args.pop(0)
        quote = ' '.join(args)
                
        embed = discord.Embed(title = 'play Commands', color=0xff0000)
        for key in triggers.keys():
            embed.add_field(name=f'`{key}`', value=triggers[key], inline=False)
        await ctx.channel.send(embed=embed)

async def Info(ctx, client, args, commands):
    embed = discord.Embed(
        title = 'OdinBot',
        Description = "Odin's personal bitch to make him \n do whatever he wants."
    )
    embed.set_footer(text='Currently Running on: `Python3.8.5` code')
    await ctx.channel.send(embed=embed) 

async def Clear(ctx, client, args, commands):
    await ctx.channel.send('clear ',args,' times')

async def randStatus(client):
    while True:
        print('\n\u001b[33;1m----RandStatus Event----\u001b[0m')
        playing_status = ["Adobe After Effects", "Adobe Premiere Pro.", "OliBot", "Life.", "With someones feelings", "Escape from Tarkov",   ]
        watching_status = ["The world burn...", "Spongebob Squarepants", "The LOTR Trilogy", "You","Rick and Morty", "TikTok", "Your internet history", "The StarWars Prequels", "Anime", "Nyan Cat", "OliBot", "a 90 min cut of Avatar", "Something"]
        listen_status = ["USSR National Anthem", "Smash Mouth", "BBC Radio 1", "Skyrim bard songs", "your conversations", "Darude Sandstorm", "The NSA comms", "A Joe Rogan podcast", "Rap God", "A BSG podcast"]
        i = 0
        status_list = rand.randrange(0,3)
        if (status_list == 0):
            active_status = playing_status
            activity_type = discord.ActivityType.playing
        elif (status_list == 1):
            active_status = watching_status
            activity_type = discord.ActivityType.watching
        elif (status_list == 2):
            active_status = listen_status
            activity_type = discord.ActivityType.listening
        e = 0
        i = rand.randrange(e, len(active_status))
        activity = discord.Activity(name=active_status[i], type=activity_type)
        await client.change_presence(activity=activity)
        print(f'\u001b[33;1m----Status changed to *{active_status[i]}*----\u001b[0m')
        await asyncio.sleep(60 * 25)

async def ConvertUK(message, client, args, commands):
    amount = int(args)
    danish = 8.24
    swedish = 11.42
    us = 1.30
    uk = 1
    embed = discord.Embed(Converted)
    embed.add_field(name='Danish', value=str(danish*amount))
    embed.add_field(name='Swedish', value=str(swedish*amount))
    embed.add_field(name='US', value=str(us*amount))
    embed.add_field(name='UKs', value=str(uk*amount))
    print('calculated')
    await client.send(embed)
        
async def Watch2gether(ctx):
    r = req.post('https://w2g.tv/rooms/create', allow_redirects=False)
    roomurl = r.headers['Location']

    await ctx.channel.send(roomurl)

async def Randimg(ctx, client, args, commands):
    url = Rimg.generateUrl()
    if url == None:
        await ctx.channel.send('Image Removed. tpye `;rimg` for new img')
    else:
        await ctx.channel.send(Rimg.getimg(url))



async def joinvc(ctx, client, args, commands):
    channel = ctx.author.voice.channel
    try:
        await channel.connect()
    except Exception as e:
        print(e)

async def leavevc(ctx, client, args, commands):
    channel = ctx.guild.voice_client
    try:
        await channel.disconnect(force=True)
    except Exception as e:
        print(e)



async def play(ctx, client, args, commands):
    
    quote = ' '.join(args)

    if quote in str(triggers):
        for key in triggers.keys():
            if quote == triggers[key]:
                filename = key
                try:
                    channel = ctx.author.voice.channel
                    voice = await channel.connect()
                    voice.play(discord.FFmpegPCMAudio(f'D:/Dropbox/CODESTUFFS/Python/Odinbot/Modules/Quotes/{filename}'), after=lambda e: print('done', e))
                except Exception as e:
                    print(e)
            else:
                continue
    else:
        await ctx.channel.send('i dont know that scene.')

async def randomquote(ctx, client, args, commands):

    mp3s = []
    quotes = os.listdir('D:/Dropbox/CODESTUFFS/Python/Odinbot/Modules/Quotes/')
    for quote in quotes:
        if quote.endswith('.mp3'):
            mp3s.append(quote)
        else:  
            continue
    
    try:
        channel = ctx.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        i = rand.randrange(0,31)
        voice.play(discord.FFmpegPCMAudio(f'Modules/Quotes/{mp3s[i]}'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.15
    except Exception as e:
        print(e)
