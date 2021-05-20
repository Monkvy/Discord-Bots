import discord
import time
import praw
import random
from discord.ext import commands

class Default(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):

        author = ctx.message.author

        helpEmbed = discord.Embed(
            title = 'Hilfe  :mailbox_closed:',
            description = '**:joystick:   Hier werden alle Commands aufgelistet.  :joystick:**',
            colour = discord.Colour.green()
        )
        helpEmbed.add_field(name='Commands für alle:', value='\n``.help``   Zeigt diese Nachrricht.\n``.ping``   Zeigt dir den Server Ping', inline=False)
        helpEmbed.add_field(name='Commands für admins:', value='\n``.startEmbed``   Schickt ein Start Embed\n``.channelEmbed``   Schickt ein Channel Embed.', inline=False)
        helpEmbed.add_field(name='Commands für Mods', value='\n ``.clear <anzahl der nachrichten>``   Löscht den Chatverlauf.\n``.kick <member>``   Kick einen Spieler.\n``.ban <member>``   Bannt einen Spieler.\n``.Unban``   Wer das nicht weiß ist lost.')

        await ctx.channel.purge(limit=1)
        await author.send(embed=helpEmbed)


    @commands.command()
    async def ping(self, ctx):

        await ctx.channel.purge(limit=1)
        pingEmbed = discord.Embed(
            title = f'Der Server Ping ist: {round(self.client.latency * 1000)}ms',
            description = 'Diese Nachrricht wird ungültig in 5 sek.',
            colour = discord.Colour.green()
        )

        await ctx.send(embed=pingEmbed)


    @commands.command()
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id="cNIwo7uKbWm5UA",
                            client_secret="KSGQmdqQcAeP6q9Lq_lqSDqZT196AQ",
                            username="Monkvyy",
                            password="Uha24012006",
                            user_agent="pyDCprawFES")

        subreddit = reddit.subreddit("memes")
        all_subs = []

        top = subreddit.top(limit = 150)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        memeEmbed = discord.Embed(title=name)
        memeEmbed.set_image(url=url)

        await ctx.send(embed=memeEmbed)


    @commands.command()
    async def info(self, ctx, member: discord.Member):

        infoEmbed = discord.Embed(
            title=member.name,
            discription=member.mention,
            colour=discord.Colour.green())

        infoEmbed.add_field(name='ID', value=member.id, inline=True)
        infoEmbed.set_thumbnail(url=member.avatar_url)
        infoEmbed.set_footer(icon_url=ctx.author.avatar_url, text=f'Angefragt von {ctx.author.name}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=infoEmbed)


def setup(client):
    client.add_cog(Default(client))