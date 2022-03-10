import discord
from datetime import datetime

from discord import Embed
from discord.ext import commands, tasks





class VotingSystem(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your VotingSystem cog')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def poll (self, ctx, time: int, vote: int, title, *options):
        if len(options) > 10:
            await ctx.send(':no_entry: You can only have **10 options** at maximum!')

        elif time <= 15:
            await ctx.send(':no_entry: Please provide poll end time greater than **15 minutes**!')

        elif 51 < vote:
            await ctx.send(':no_entry: Please provide poll vote max number less than ** 51**!')

        polls = ['\n'.join([f'{self.emoji[index]} {options} \n' for index, option in enumerate(options)]), False]

        embed = discord.Embed(title=title,
                              description=f':stopwatch: Poll will end in **{time} minute**!',
                              colour=0xF0000)

        embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{ctx.message.guild.id}/{ctx.message.guild.icon}.png')

        name, value = polls
        embed.add_field(name=name, value=value)

        message = await ctx.channel.send(embed=embed)

        for item in self.emoji[:len(options)]:
            await message.add_reaction(item)




def setup(client):
    client.add_cog(VotingSystem(client))