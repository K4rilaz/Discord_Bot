import discord
from datetime import datetime
from discord.ext import commands, tasks




client = commands.Bot(command_prefix = '.', case_insensitive = True, owner_id = 664233463477698571)
owner_id = 664233463477698571
class VotingSystem(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.emoji = ['1/u20e3', '2/u20e3', '3/u20e3', '4/u20e3', '5/u20e3'
                      '6/u20e3', '7/u20e3', '8/u20e3', '9/u20e3', '/U0001F51F']


    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello there Im your VotingSystem cog')


    @commands.command()
    @commands.is_owner()
    async def VotingSystem (self, ctx, time: int, vote: int, title, *options):
        if len(options) > 10:
            await ctx.send(':no_entry: You can only have **10 options** at maximum!')

        elif time <= 15:
            await ctx.send(':no_entry: Please provide poll end time greater than **15 minutes**!')

        elif 1000000 < vote:
            await ctx.send(':no_entry: Please provide poll vote max number less than **million**!')

        embed = discord.Embed(title=title,
                              description=f':stopwatch: Poll will end in **{time} minutes**',
                              colour=0xF000)
        embed.set_thumbnail(url = f'https://cdn.discordapp.com/icons/{ctx.message.id}/{ctx.message.guild.icon}.png')

        for name, value, inline in VotingSystem:
            embed.add_field(name=name, value=value, inline=inline)

        message = await ctx.send(embed=embed)

        for item in self.emoji[:len(options)]:
            await message.add_reaction(item)




























def setup(client):
    client.add_cog(VotingSystem(client))