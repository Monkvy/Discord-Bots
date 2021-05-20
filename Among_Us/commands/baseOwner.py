import discord
import sys
import time
from discord.ext import commands

class BaseOwner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def muteAll(self, ctx):
            
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=True)

        await ctx.channel.purge(limit=1)
        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat seine Lobby gemuted")
        with open("log.txt", 'a') as fileW:
            fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat seine Lobby gemuted")
            fileW.close()

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def unMuteAll(self, ctx):
            
        vc = ctx.author.voice.channel
        for member in vc.members:
            await member.edit(mute=False)

        await ctx.channel.purge(limit=1)
        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat seine Lobby entmuted")
        with open("log.txt", 'a') as fileW:
            fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat seine Lobby entmuted")
            fileW.close()


def setup(client):
    client.add_cog(BaseOwner(client))