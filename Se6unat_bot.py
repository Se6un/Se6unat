import asyncio
from discord.ext import commands
from random import randint, choice
from discord.utils import get
from discord import FFmpegPCMAudio
import time
import discord
import youtube_dl
import os

zasranec = 988803599033315370

os.system('color F')


# start


#main command.Bot ( command_prefix = "!" ) #!help
client = commands.Bot(command_prefix='!')

#бот включен
@client.event
async def on_ready():
    print("Бот активирован")


@client.event
async def on_voice_state_update( member, before, after ):
    if after.channel.id == 988115954619809874:
        for guild in client.guilds:
            maincategory = discord.utils.get( guild.categories, id = 959843680443842660 )
            channel_p = await guild.create_voice_channel( name = f' Комната {member.display_name}', category = maincategory )
            await channel_p.set_permissions( member, connect = True, mute_members = True, move_members = True, manage_channels = True )
            await member.move_to( channel_p )
            def check( x, y, z ):
                return len( channel_p.members ) == 0
            await client.wait_for( 'voice_state_update', check = check )
            await channel_p.delete()
#Засранцы
@client.event
@commands.has_role(zasranec)
async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith(''):
            #await message.channel.send(random.choice(list1))
            await message.add_reaction('💩')
            #await message.add_reaction('😽')

#подключение
token = open ('token.txt','r').readline()

client.run ( token )
