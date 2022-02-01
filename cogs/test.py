import discord
from discord.ext import commands
import random
from discord.ext.commands import BucketType, cooldown


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your Cheers cog')

    # CHEERS SETUP
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)

    cheers = ['Test1', 'Test2', 'Test3']
    @commands.command(aliases = cheers)
    @commands.cooldown(5, 10, BucketType.channel)
    async def on_message(self, message):
            responses = ['Test is working!', 'Kinda works', 'Nope']


            await message.channel.send(f'{random.choice(responses)}  {message.author.mention}')


def setup(client):
    client.add_cog(Test(client))