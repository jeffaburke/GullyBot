import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.AutoShardedBot(command_prefix='!', activity=discord.Streaming(name='Being programmed :) Gully Fan Bot', url='http://www.twitch.tv/imgully'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("---Bot---")
    print(bot.user.id)
    print("---is ready!---")

@bot.event
async def on_member_join(member):
    await member.add_roles("537626518566862849")
    
@bot.command
async def test():
    await bot.say('The bot is being programmed and this is a test :)')

bot.run("NTM3NjI4MDIzNzUxNDQyNDUz.DypeTA.lYbx_vwiFjtQZT754IxkE8WD1BU")
