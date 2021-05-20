import discord
import time
import sys
from discord.ext import commands, tasks

restartInputLoop = False

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        muteChannel = self.client.get_channel(776940600934662155)

        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Among Us'))


        print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))}]  {self.client.user} ist on")


        muteEmbed = discord.Embed(
            title = 'Auto Mute für Among Us   :zipper_mouth:',
            description = 'Reagiere mit :white_check_mark:, um deine Lobby zu muten.',
            colour = discord.Colour.green()
        )
        
        await muteChannel.purge(limit=999)
        muteEmbedMsg = await muteChannel.send(embed=muteEmbed)
        muteEmbedObj = await muteChannel.fetch_message(muteEmbedMsg.id)
        await muteEmbedObj.add_reaction('<:check_mark:777201873907744800>')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        global restartInputLoop


        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'**:exclamation: Unbekannter Command!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  Unbekannter Command!  {ctx.author.id}")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'**:exclamation: Fülle alle Parameter aus!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  Nicht alle Parameter wurden ausgefüllt!  {ctx.author.name}")
        
        else:
            await ctx.send(f'**:exclamation: Unbekannter Error!**\n        Gebe ``.help`` für Hilfe ein.')
            print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  Unbekannter Error!  {ctx.author.id}")

        restartInputLoop = True
        


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global restartInputLoop

        if ((reaction.message.channel.id == 776940600934662155) & 
            (user.id != 776938413890076683)):

            vc = user.voice.channel
            for member in vc.members:
                await member.edit(mute=True)
                print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {user.id} hat seine Lobby gemuted")
                
                with open("log.txt", 'w') as fileW:
                    fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {user.id} hat seine Lobby gemuted")
                    fileW.close()
                restartInputLoop = True

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        global restartInputLoop

        if ((reaction.message.channel.id == 776940600934662155) & 
            (user.id != 776938413890076683)):

            vc = user.voice.channel
            for member in vc.members:
                await member.edit(mute=False)
                print(f"\r[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {user.id} hat seine Lobby entmuted")
                
                with open("log.txt", 'w') as fileW:
                    fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {user.id} hat seine Lobby entmuted")
                    fileW.close()

                restartInputLoop = True

def setup(client):
    client.add_cog(events(client))

    