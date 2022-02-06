import discord
import random
import time
import asyncio
import logging
import platform
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord import Member, Embed




TOKEN = ""
client = commands.Bot(command_prefix = '.', case_insensitive = True, owner_id = 664233463477698571)
status = cycle(['Status 1', 'Status 2'])
logging.basicConfig(level = logging.INFO)
owner_id = 664233463477698571

#Maybe dump codes!
# LINE 28 under Change_status.start: await client.change_presence(status = discord.Status.online, activity = discord.Game('Assembling myself beep boop'))
# await self.client.process_commands(message)

#Scheduled clear message tasks?
#Creator info message
#Random scheduled room messages

@client.event
async def on_ready():
    change_status.start()
    channel = client.get_channel(935513160960581675)
    await channel.send('Hello')
    print('R6 Event Bot is online')

@client.event
async def on_disconnect():
    print('R6 Event Bot is offline')

@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))


#COG Clients
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')  #This command will go into the cogs folder and look for the example file.
    await ctx.send(f'Extension loaded')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded')


for filename in os.listdir('./cogs'): #Look into the directory where cogs in and give me all the files in the directory
    if filename.endswith('.py') and not filename.startswith("_"): #Check the files only with .py so we dont accidentally load other kind of files.
        client.load_extension(f'cogs.{filename[:-3]}') #(:-3) with this we load 'cogs.example'


#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command used.')

#CLEAR SETUP
@client.command()
@commands.is_owner()
@commands.has_permissions(manage_messages = True)  #This restricts to specific users to be able to use BOT commands
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)


#Logout command setup
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    if ctx.author.id == owner_id:
        """
        If user is running the command and owns the bot then this will disconnect the bot from discord.
        """
        await ctx.send(f"Hey {ctx.author.mention}, I am logging out :wave:")
        await ctx.bot.logout()

@shutdown.error
async def logout_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('dummy')
    else:
        raise error




client.run(TOKEN)