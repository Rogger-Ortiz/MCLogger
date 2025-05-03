import discord
from discord.ext import commands

import os

defaultEmbedColor=discord.Color(0xb253d6)
green = discord.Color(0x00FF00)
red = discord.Color(0xFF0000)
checkmark = ":white_check_mark:"
xmark = ":x:"


class Logging(commands.Cog):
    description=""
    def __init__(self,bot):
        self.bot = bot

    # Print code here
    @commands.command(name="printlog", help="Print the current logs or a crash report")
    async def printLog(self, ctx, service=None):
        if ctx.author.id not in [248440677350899712, 751491520254967909, 199813904883384320]:
            return
        if service == None:
            # crash_reports = os.listdir("/home/captain/projects/ker")
            logEmbed = discord.Embed(title='Log Files', description="List of Log Files to read:", color=defaultEmbedColor)
            logEmbed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar.url)
            logEmbed.set_footer(text="** Call a log to be shown by using $printlog [log name]! **")
            logEmbed.add_field(name="Logs", value="latest.log\ndebug.log", inline=False)
            # for file in crash_reports:
                ## TODO WHEN A FOLDER/FILE STRUCTURE IS CREATED ON FIRST CRASH
            await ctx.reply(embed=logEmbed)
            return
        if service in ["latest.log", "debug.log"]:
            filepath=f"/home/captain/projects/ker/logs/{service}"
            await ctx.reply(file=discord.File(filepath))
            return
        if service != None and service not in ["latest.log", "debug.log"]:
            await ctx.reply(f"No file named {service}! Use $printlog to view available logs.")
            return
        

async def setup(bot):
	await bot.add_cog(Logging(bot))
