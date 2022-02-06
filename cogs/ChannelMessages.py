import discord
from discord.ext import commands
import random
import aiocron


class RMessages(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your ChannelMessages cog')


    #RANDOM MESSAGES SETUP
    channel_id = 939936086782795907