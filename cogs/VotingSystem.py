import discord
from datetime import datetime

from discord import Embed
from discord.ext import commands, tasks


def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)


class VotingSystem(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your VotingSystem cog')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def poll(self, ctx, time: int, title, *options: str):
        embed = discord.Embed(title=title,
                              colour=0xF0000)
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{ctx.message.guild.id}/{ctx.message.guild.icon}.png')

        if len(options) > 10:
            await ctx.send(':no_entry: You can only have **10 options** at maximum!')

        elif time <= 15:
            await ctx.send(':no_entry: Please provide poll end time greater than **15 minutes**!')

        choices = [(to_emoji(e), v) for e, v in enumerate(options)]
        body = "\n".join(f"{key}: {c}" for key, c in choices)
        embed.description = f':stopwatch: Poll will end in **{time} minute**!\n\n {body}'

        poll = await ctx.send(embed=embed)
        for emoji, _ in choices:
            await poll.add_reaction(emoji)



def setup(client):
    client.add_cog(VotingSystem(client))