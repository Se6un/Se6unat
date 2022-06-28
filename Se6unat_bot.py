from discord.ext import commands
import random
from random import randint, choice
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import datetime
import discord
import youtube_dl
import os

global PREFIX
PREFIX = "!"
#рандомные приветы
privet = ["https://tenor.com/view/husky-dratuti-hello-hi-dog-gif-11621293", "https://tenor.com/view/privet-privetik-medved-lapa-gif-5090152",
          "https://tenor.com/view/hello-cat-waving-trendizisst-hi-gif-21629939",
          "https://tenor.com/bamzz.gif","https://tenor.com/view/looney-tunes-daffy-duck-hello-greetings-well-hello-there-gif-17075737",
          "https://tenor.com/view/love-wide-awake-hello-gif-13245309","https://tenor.com/view/baby-hello-hello-there-hi-waving-gif-15692366",
          "https://tenor.com/view/hey-there-derp-puppy-dog-doggo-gif-15817609","https://tenor.com/view/yoda-baby-crying-cuddles-hello-there-gif-22666769",
          "https://acegif.com/wp-content/gifs/privet-6.gif","https://acegif.com/wp-content/gifs/privet-13.gif",
          "https://acegif.com/wp-content/gifs/privet-31.gif","https://acegif.com/wp-content/gifs/privet-32.gif",
          "https://acegif.com/wp-content/gifs/privet-37.gif","https://acegif.com/wp-content/gifs/privet-56.gif",
          "https://acegif.com/wp-content/gifs/privet-59.gif"]
privet_text = ["Добро пожаловать!", "Бенвенуа( Добро пожаловать на французском )",
          "Виллкоммен ( Добро пожаловать на немецком )",
          "Алоха( Добро пожаловать на гавайском )",
          "Шалом( Добро пожаловать на иврите )",
          "Биенвенуто( Добро пожаловать на итальянском )","Йокосо! ( Добро пожаловать на японском )",
          "Хвангйонг-хамнида( Добро пожаловать на корейском )"]


intents = discord.Intents.all()

#main command.Bot ( command_prefix = "!" ) #!help
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = PREFIX)


#бот включен
@client.event
async def on_ready():
    print("Бот активирован")

#привет

@client.event
async def on_member_join (member):
    channel = client.get_channel ( 991279090344673280 )
    test = discord.Embed(description=random.choice(privet_text), color=0xe74c3c)
    test.set_author(name=member.name, icon_url=member.avatar_url)
    test.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=test)  #discord.Embed(description=f'``{member.name}`` Добро пожаловать', color=0x0c0c0c))
    await asyncio.sleep(0.5)
    await channel.send(random.choice(privet))

#создание приватной комнаты
@client.event
async def on_voice_state_update( member, before, after ):
    if after.channel.id == 944507489641181235:#hots
        for guild in client.guilds:
            maincategory = discord.utils.get( guild.categories, id = 884450500865568830 )
            channel_p = await guild.create_voice_channel( name = f' Комната {member.display_name}', category = maincategory )
            await channel_p.set_permissions( member, connect = True, mute_members = True, move_members = True, manage_channels = True )
            await member.move_to( channel_p )
            def check( x, y, z ):
                return len( channel_p.members ) == 0
            await client.wait_for( 'voice_state_update', check = check )
            await channel_p.delete()
    if after.channel.id == 988115954619809874:#переговорная
        for guild in client.guilds:
            maincategory = discord.utils.get( guild.categories, id = 959843680443842660 )
            channel_p = await guild.create_voice_channel( name = f' Комната {member.display_name}', category = maincategory )
            await channel_p.set_permissions( member, connect = True, mute_members = True, move_members = True, manage_channels = True )
            await member.move_to( channel_p )
            def check( x, y, z ):
                return len( channel_p.members ) == 0
            await client.wait_for( 'voice_state_update', check = check )
            await channel_p.delete()

# secret
@client.command(brief = f'Отправить анонимное сообщение в лс пользователю [{PREFIX}secret (msg)]')
async def secret(ctx, member: discord.Member, *, message = None):
	await ctx.channel.purge(limit = 1)
	await member.send(f'{message}')



# clear удалить сообщения
@client.command(brief = 'Будет очищен чат')
@commands.has_permissions(administrator = True)
async def удалить(ctx, amount = 0):
	await ctx.channel.purge(limit = amount + 1)
	await ctx.send(f'{amount} сообщений было удалено!')
	time.sleep(5)
	await ctx.channel.purge(limit = 1)

#подключение
token = open ('token.txt','r').readline()
client.run ( token )
