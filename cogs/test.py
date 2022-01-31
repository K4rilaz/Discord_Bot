import discord
from discord.ext import commands
import random

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your Cheers cog')

    # CHEERS SETUP
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        responses = ['Test is working!', 'Kinda works', 'Nope']
        Test = ['Test1', 'Test2', 'Test3']


        if any(word in message.content for word in Test):
            await message.channel.send(f'{random.choice(responses)}  {message.author.mention}')

def setup(client):
    client.add_cog(Test(client))