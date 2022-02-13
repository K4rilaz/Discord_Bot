import discord
from discord.ext import commands, tasks
import random
import aiocron
import asyncio



class ChannelMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.printerloop.start()


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your ChannelMessages cog')


    #RANDOM MESSAGES SETUP
    @tasks.loop(seconds = 3 )
    async def printerloop(self):
        channel = self.client.get_channel(939936086782795907)
        responses = ['response 1', 'response 2', 'response 3']
        await channel.send(f'{random.choice(responses)}')



def setup(client):
    client.add_cog(ChannelMessages(client))