#Importaciones
import discord as ds
import json as js
import random as rnd
from discord.ext import commands as cmd

#Utiles
async def gifs(ctx, tt : str, url : str, color):
    em=ds.Embed(title=tt, color=color)
    if url == "":
        pass
    else:
        em.set_image(url=url)
    await ctx.send(embed=em)

#Colores
verde = 0xFF000
rojo = 0xFF0000
azul = 0x0174DF
rosa = 0xFF00BF
blanco = 0xFFFFFF
plata = 0xD8D8D8
negro = 0x000000
amarillo = 0xF7FE2E



with open('config.json') as f:
    #Lectura json
    datos = js.load(f)
    #Sacar path links
    links = datos['links']
    #Transformaciones
    ssj = links['ssj']
    ssj2 = links['ssj2']
    ssj3 = links['ssj3']
    ssjl = links['ssjl']
    ssj4 = links['ssj4']
    ssg = links['ssg']
    ssgss = links['ssgss']
    ssgsse = links['ssgsse']
    ssgsskk = links['ssgsskk']
    ssrose = links['ssrose']
    mng = links['mng']
    ozaru = links['ozaru']
    gozaru = links['g-ozaru']
    #Creador
    dev_id = datos['dev-id']

#Inicio bot
desc=''
inicio = True

bot=cmd.Bot(command_prefix='{0}'.format(datos['prefijo']), description=desc)

#Mensaje inicio
@bot.event
async def on_ready():
    print("Soy "+bot.user.name)
    print("ID: "+str(bot.user.id))
    print("<=================>")
    print('JSON:')
    print('Prefijo: '+datos['prefijo'])
    for listaLnks in datos['links']:
        print('{0}: '.format(listaLnks))
        if listaLnks == ssj:
            for i in ssj:
                print('-'+i)
        elif listaLnks == ssj2:
            for i in ssj2:
                print('-'+i)
        elif listaLnks == ssj3:
            for i in ssj3:
                print('-'+i)
        elif listaLnks == ssj4:
            for i in ssj4:
                print('-'+i)
        elif listaLnks == ssjl:
            for i in ssjl:
                print('-'+i)
        elif listaLnks == ssg:
            for i in ssg:
                print('-'+i)
        elif listaLnks == ssgss:
            for i in ssgss:
                print('-'+i)
        elif listaLnks == ssgsse:
            for i in ssgsse:
                print('-'+i)
        elif listaLnks == ssgsskk:
            for i in ssgsskk:
                print('-'+i)
        elif listaLnks == ssrose:
            for i in ssrose:
                print('-'+i)
        elif listaLnks == mng:
            for i in mng:
                print('-'+i)
        elif listaLnks == ozaru:
            for i in ozaru:
                print('-'+i)
        elif listaLnks == gozaru:
            for i in gozaru:
                print('-'+i)

#Comandos
@bot.command(name="ssj")
async def ssj(ctx):
    gif = rnd.choice(links['ssj'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj!!'.format(ctx), url=gif, color=amarillo)
@bot.command(name='ssj2')
async def ssj2(ctx):
    gif = rnd.choice(links['ssj2'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha tranformado en ssj2!!'.format(ctx), url=gif, color=amarillo)
@bot.command(name='ssj3')
async def ssj3(ctx):
    gif = rnd.choice(links['ssj3'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj3!!'.format(ctx), url=gif, color=amarillo)
@bot.command(name='ssj4')
async def ssj4(ctx):
    gif = rnd.choice(links['ssj4'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj4!!'.format(ctx), url=gif, color=plata)
"""
<---PROXIMAMENTE SSJ5--->
"""
@bot.command(name='ssjl')
async def ssjl(ctx):
    gif = rnd.choice(links['ssjl'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssjl!!'.format(ctx), url=gif, color=verde)
@bot.command(name='ssg')
async def ssg(ctx):
    gif = rnd.choice(links['ssg'])
    await gifs(ctx=ctx, tt='')

@bot.command(name='creator')
async def creator(ctx):
    await ctx.send('Mi creador es <@'+dev_id+'>')
#Encender bot
if inicio:
    bot.run(datos['token'])
