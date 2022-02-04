import discord
import random
import time
import asyncio
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord import Member, Embed




TOKEN = ""
client = commands.Bot(command_prefix = '.')
status = cycle(['Status 1', 'Status 2'])
# await self.client.process_commands(message)
#Add embeds and titles for Bot commands?
#Scheduled clear message tasks?

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status = discord.Status.online, activity = discord.Game('Assembling myself beep boop'))
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
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')  #This command will go into the cogs folder and look for the example file.
    await ctx.send(f'Extension loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension unloaded')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Extension reloaded')

#Custom Help command setup
class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):   #This line triggers the .help function
        for cog in mapping:
            await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')

    async  def send_cog_help(self, cog):   #This will run the HelpCommands cog itself
        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

    async def send_group_help(self, group):
        await self.get_destination().send(f'{group.name}: {[command.name for index, commandd in enumerate(group.commandds)]}')

    async def send_command_help(self, command):
        await self.get_destination().send(command.name)

bot = commands.Bot(command_prefix = '.', help_command = CustomHelpCommand())

for filename in os.listdir('./cogs'): #Look into the directory where cogs in and give me all the files in the directory
    if filename.endswith('.py'): #Check the files only with .py so we dont accidentally load other kind of files.
        client.load_extension(f'cogs.{filename[:-3]}') #(:-3) with this we load 'cogs.example'


#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command used.')

#CLEAR SETUP
@client.command()
@commands.has_permissions(manage_messages = True)  #This restricts to specific users to be able to use BOT commands
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)




client.run(TOKEN)