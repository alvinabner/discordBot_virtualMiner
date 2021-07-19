import discord
from discord.ext import commands
import random as rand

class Games:
    def __init__(self, level, coal, xp):
        self.level = level
        self.coal = coal
        self.xp = xp

    @commands.command()
    async def inv(self,ctx):
        await ctx.send('Your Inventory\n\nLevel: {}'.format(self.level))

    @commands.command()
    async def mine(self, coal, xp, ctx):
        self.coal = rand.randrange(4,16)
        self.xp = coal * 1

        await ctx.send('You got {} coal\n+{} XP'.format(self.coal, self.xp))

def setup(client):
    client.add_cogs(Games(client))