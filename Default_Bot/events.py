import discord
import time
from discord.ext import commands, tasks

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        startChannel = self.client.get_channel(766573949713776641)
        startEmbed = discord.Embed(
            title = 'Willkommen auf unserem Server!    :partying_face:',
            description = '**Among Us [BOT]** prefix: .\n**Rythm[BOT]** prefix: !\n**Fast echter Spieler [BOT]** prefix: *\n',
            colour = discord.Colour.greyple()
        )                                                                 
        startEmbed.add_field(name='\n__Owner__', value='\nMonkvy\n', inline=False)
        startEmbed.add_field(name='__Admin__', value='\nxlyaz\nTibor\nflowey1994\nchef\nMathies\nMr.Swag\nSAFT_Superiron29', inline=False)
        startEmbed.add_field(name=':balloon:   \n\n', value='\nReagiere mit :white_check_mark:   , um die Standart Rolle zu bekommen.', inline=False)
        
        #await startChannel.purge(limit=9)
        #await startChannel.send("https://discord.gg/MuVn9ReSQH")
        #startEmbedMsg = await startChannel.send(embed=startEmbed)
        #channelEmbedMessageObj = await startChannel.fetch_message(startEmbedMsg.id)
        #await channelEmbedMessageObj.add_reaction('<:check_mark:777201873907744800>')

    

        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Alles .-.'))


        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))}]  {self.client.user} ist on")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'**:exclamation: Unbekannter Command!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} FES]  Unbekannter Command!  {ctx.author.id}")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**:exclamation: Fülle alle Parameter aus!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} FES]  Nicht alle Parameter wurden ausgefüllt!  {ctx.author.id}")
        else:
            await ctx.send(f'**:exclamation: Unbekannter Error!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} FES]  Unbekannter Error!  {ctx.author.id}")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        defaultRole = discord.utils.get(user.guild.roles, name='═══╣  No Name   ╠═══')

        if (reaction.message.channel.id == 766573949713776641):
            await user.add_roles(defaultRole)

        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} FES]  {user.id} hat im Channel {reaction.message.channel.id} reagiert")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {user.id} hat seine Reaction im Channel {reaction.message.channel.id} entfernt")

def setup(client):
    client.add_cog(events(client))