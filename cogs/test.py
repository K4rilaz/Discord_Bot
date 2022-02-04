from discord import Embed
from discord.utils import get
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.menus import MenuPages, ListPageSource
from typing import Optional
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nogroup(self, ctx):
        await ctx.send('This command is not in a group.')

    @commands.group(invoke_without_command = True)
    async def group(self, ctx):
        await ctx.send('This is a group')

    @group.command()
    async def test(self, ctx):
        await ctx.send('This is a subcommandwithin the group.')


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your Help command cog')



def setup(bot):
    bot.add_cog(Test(bot))

