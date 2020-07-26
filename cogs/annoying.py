import discord
import re
from discord.ext import commands
"""
this cog is good for some servers but in general you might wanna
drop some memes and yeah have fun
"""
class Antilink(): # it all makes sense now
    def __init__(self, bot):
        self.bot = bot
        self._link_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+') # is a link? 
        
    async def delete_link(self, message):
        if not message.channel: # self explanatory
            return
        if message.author == self.bot.user: # self explanatory
            return
        if re.match(message, self._link_regex): # self explanatory do i have to tell you everything?
            try:
                await message.delete()
                await message.channel.send(f'{message.author.mention}, lol i\'m annoying right? yes that\'s my purpose you dumbass') # annoys the person even more
            except:
                pass

    async def on_message(self, message):
        await self.delete_link(message)

def setup(bot):
    bot.add_cog(Antilink(bot))
    print("gay mode activated")
