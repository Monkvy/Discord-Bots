import os
from discord.ext import commands

def Among_Us_main():

    if (__name__ == "__main__"):
        client = commands.Bot(command_prefix= '.')
        client.remove_command("help")

        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                client.load_extension(f'commands.{filename[:-3]}')

        client.load_extension('events')


        client.run('<TOKEN>')

if (__name__ == "__main__"):
    Among_Us_main()