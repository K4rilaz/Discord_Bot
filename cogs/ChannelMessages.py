import discord
from discord.ext import commands, tasks
import random
import aiocron



class ChannelMessages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_messages.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your ChannelMessages cog')


    #RANDOM MESSAGES SETUP
    @tasks.loop(seconds =  3)
    async def channel_messages(self, message):
        channel_id = 939936086782795907
        channel = tasks.get_channel(channel_id)
        responses = ['response 1', 'response 2', 'response 3']
        await message.channel.send(f'{random.choice(responses)}') #FIXXXXXX

    @channel_messages.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.client.wait_until_ready()




def setup(client):
    client.add_cog(ChannelMessages(client))