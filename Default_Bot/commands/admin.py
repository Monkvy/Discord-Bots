import discord
import os
import sys
import time
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='startEmbed')
    @commands.has_guild_permissions(administrator=True)
    async def startEmbed(self, ctx):

        startEmbed = discord.Embed(
            title = 'Willkommen auf unseren Server!    :partying_face:',
            description = '**Among Us [BOT]** prefix: .\n**Rythm[BOT]** prefix: !\n**Fast echter Spieler [BOT]** prefix: *\n',
            colour = discord.Colour.greyple()
        )                                                                 
        startEmbed.add_field(name='\n__Owner__', value='\nMonkvy\n', inline=False)
        startEmbed.add_field(name='__Admin__', value='\nxlyaz\nTibor\nflowey1994\nchef\nMathies\nMr.Swag\nSAFT_Superiron29', inline=False)
        startEmbed.add_field(name=':balloon:   \n\n', value='\nReagiere mit :white_check_mark:   , um die Standart Rolle zu bekommen.', inline=False)


        await ctx.channel.purge(limit=1)
        await ctx.send("https://discord.gg/MuVn9ReSQH")
        startEmbedMsg = await ctx.send(embed=startEmbed)

        channelEmbedMessageObj = await ctx.channel.fetch_message(startEmbedMsg.id)

        await channelEmbedMessageObj.add_reaction('<:check_mark:777201873907744800>')

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def quit(self, ctx):
        if (ctx.message.channel.id != 768514950674382868):
            return

        quitEmbed = discord.Embed(
            title = 'Ich verlasse jetzt den Server',
            description = '',
            colour = discord.Colour.red()
        )

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=quitEmbed)
        sys.exit()

    


    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def commandChannelEmbed(self, ctx):
        commandChannelEmbed = discord.Embed(
            title = 'Info',
            description = 'Bitte schalte diesen Channel stumm ',
            colour = discord.Colour.red()
        )

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=commandChannelEmbed)


    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def helpEmbed(self, ctx):
        
        helpEmbed = discord.Embed(
            title = 'Hilfe und Info  🚩',
            description = ' ',
            colour = discord.Colour.red()
        )
        helpEmbed.set_footer(text='Bitte verwende die dazugehörigen Channels.  💬')
        helpEmbed.add_field(name='**Fast echter Spieler [BOT]  🤖**\n', 
                            value='``.help``   Zeigt eine Help Nachrricht.\n' + 
                                  '``.ping``   Zeigt dir den Server Ping.\n' + 
                                  '``.createChannel <name>``   Erstelle dir deinen VoiceChannel.\n' + 
                                  '``.info <member>``   Zeigt dir Spieler infos.', inline=False)
        helpEmbed.add_field(name='**Among Us [BOT]  🔪**\n', 
                            value='``.help``   Zeigt eine Help Nachrricht.\n' + 
                                  '``.randomVote <max>``   Randomvoted Jmd.', inline=False)


        await ctx.channel.purge(limit=1)
        await ctx.send(embed=helpEmbed)

def setup(client):
    client.add_cog(Admin(client))