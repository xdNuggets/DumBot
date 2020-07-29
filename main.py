import discord
from discord.ext import commands

initial_extensions = ['cogs.annoying']

bot = commands.Bot(command_prefix="lmao ", description="im a bot to make you rage lmaooooooo")
bot.remove_command("help")

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

"""
not case insensitive
most used prefix
ya see what i did there
no help command, have fun
"""

@bot.event
async def on_ready():
    print("lmao hi")


@bot.command()
async def hi(ctx):
    user = ctx.author
    await ctx.guild.ban(ctx.author, reason="lmao bye")
    await ctx.send("hi and goodbye")
    await user.send("Sorry about that, I am DumBot which means I am dumb. I think hi means bye so BYE LMAOALAMAOLAAMAOALAM")
    
@bot.group()
async def help(ctx):
    embed = discord.Embed(title="Here is my help menu!", description="Click on that link to direct u to the help menu and see his commands, url="https://pornhub.com")
    await ctx.send(embed=embed)

bot.run("nah")
