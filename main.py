import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="im a bot to make you rage lmaooooooo")
bot.remove_command("help")

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
    await ctx.guild.ban(ctx.author, reason="lmao bye")
    await ctx.send("ok bye")

bot.run("nah")
