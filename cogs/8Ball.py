import discord
from discord.ext import commands
import random
from discord.ext.commands import BucketType, cooldown

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #Function decorator in the Cog, so if we wanna create an 'event' in the cogs we need this decorator.
    async def on_ready(self):
        print('Hello there Im your 8Ball cog')

    # 8BALL SETUP
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance (error, commands.CommandOnCooldown):
            msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)

    @commands.command(aliases=['8Ball'])
    @commands.cooldown(1, 10, BucketType.channel)
    async def _8Ball(self, ctx, *, question): #ctx represents the command(.8Ball) and the * allows you to take multiple arguments as one argument so the question can be a whole sentence.
        """
        8Ball game which tells the outcome of the current match
        Commands: .Go Team Empire!
                  .Go G2!
        """
        responses = ['Yes', 'No', 'kinda']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):  #Setup function what will allow us to connect this cog to our bot
    client.add_cog(Example(client))