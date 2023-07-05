import discord
from discord.ext import commands
from bot_commands import BotCommands

intents = discord.Intents.default()
intents.message_content = True

# set up prefix for bot, prefix is /faw so an example command would be: '/faw ping'
bot = commands.Bot(command_prefix="/faw ", intents=intents)


@bot.event
async def on_ready():
    print("faw bot online!")
    await bot.add_cog(BotCommands(bot))
    for guild in bot.guilds:
        await manage_bot_role(guild)


# when bot is added - adds role
@bot.event
async def on_guild_join(guild):
    await manage_bot_role(guild)


# when bot is removed - removes role
@bot.event
async def on_guild_remove(guild):
    await manage_bot_role(guild, create=False)


# manages the role for the bot
async def manage_bot_role(guild, create=True):
    role = discord.utils.get(guild.roles, name="faw bot")
    if create:
        if role is None:
            role = await guild.create_role(name="faw bot")

        bot_member = guild.get_member(bot.user.id)
        if role not in bot_member.roles:
            await bot_member.add_roles(role)
    elif role is not None:
        await role.delete()