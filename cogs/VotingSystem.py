import discord
from datetime import datetime
from discord.ext import commands, tasks




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
    async def poll (self,ctx, *, message):





        embed = discord.Embed(title="poll",
                              description=f'{message}',
                              colour=0xF000)
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/icons/{ctx.message.id}/{ctx.message.guild.icon}.png')

        message = await ctx.channel.send(embed=embed)
        await message.add_reaction('yaay')
        await message.add_reaction('nooo')











def setup(client):
    client.add_cog(VotingSystem(client))