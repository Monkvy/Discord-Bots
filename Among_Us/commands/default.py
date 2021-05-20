import discord
import random
import time
from discord.ext import commands

class Default(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Help'])
    async def help(self, ctx):
        author = ctx.message.author
        helpEmbed = discord.Embed(
            title = 'Hilfe  :mailbox_closed:',
            description = '**:joystick:   Hier werden alle Commands aufgelistet.  :joystick:**',
            colour = discord.Colour.green()
        )
        helpEmbed.add_field(name='Commands für alle:', value='\n``.help``   Zeigt diese Nachrricht.\n``.randomVote <zahl>``   Wählt eine zufällige Zahl aus', inline=False)
        helpEmbed.add_field(name='Commands für admins:', value='\n``.join``   Bringt mich dazu einen Channel zu joinen.\n``.leave``   Bringt mich dazu den Channel zu leaven.\n``.muteAll``   Muted alle im Channel.\n``.unMuteAll``   Unmuted alle im Channel.', inline=False)

        await ctx.channel.purge(limit=1)
        await author.send(embed=helpEmbed)
        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat help ausgeführt")
        with open("log.txt", 'a') as fileW:
            fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat help ausgeführt")
            fileW.close()

    
    @commands.command(aliases=['RandomVote', 'randomvote', 'Randomvote'])
    async def randomVote(self, ctx, nums):
        num = random.randint(1, int(nums))

        randomEmbed = discord.Embed(
            title = 'Random-Voting',
            description = f'Der Spieler {num} muss dran glauben lol.',
            colour = discord.Colour.blue()
        )
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=randomEmbed)
        print(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat randomVote ausgeführt")
        with open("log.txt", 'a') as fileW:
            fileW.write(f"[{str(time.strftime('%d/%m/%Y %H:%M:%S'))} AU]  {ctx.author.id} hat randomVote ausgeführt")
            fileW.close()
    

def setup(client):
    client.add_cog(Default(client))
    