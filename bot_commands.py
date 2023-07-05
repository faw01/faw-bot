import discord
from discord.ext import commands

# cog setup here
class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # commands:

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, World!")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="info", description="faw bot", color=0x1ABC9C)
        embed.add_field(
            name="website", value="[faw.dev](https://faw.dev)", inline=False
        )
        embed.add_field(
            name="github", value="[faw01](https://github.com/faw01)", inline=False
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong! {round(self.bot.latency * 1000)} ms")