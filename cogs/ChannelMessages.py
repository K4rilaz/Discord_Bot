import discord
from discord.ext import commands, tasks
import random
import aiocron
import asyncio



class ChannelMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.printerloop.start()

    def cog_unload(self):
        self.printerloop.cancel()


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your ChannelMessages cog')


    #RANDOM MESSAGES SETUP
    @tasks.loop(seconds = 3 )
    async def printerloop(self):
        channel = self.client.get_channel(939936086782795907)
        responses = ['response 1', 'response 2', 'response 3']
        await channel.send(f'{random.choice(responses)}')

    @printerloop.before_loop
    async def before_printerloop(self):
        print('waiting...')
        await self.client.wait_until_ready()




def setup(client):
    client.add_cog(ChannelMessages(client))