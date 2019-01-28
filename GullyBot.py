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
    
@bot.command(pass_context=True)
async def test(ctx):
    await ctx.channel.send('The bot is being programmed and this is a test :)')

@bot.command(pass_context=True)
async def clear(ctx, number=100):
    mgs = [] 
    number = int(number) + 1
    async for x in ctx.channel.history(limit = number):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    await ctx.channel.send(f'`{number} messages have been deleted!`')

    
@bot.command(pass_context=True)
async def gully(ctx):
    await ctx.channel.send(f'{ctx.author.mention}, Gully\'s twitch is: \nhttps://twitch.tv/imgully\nHis twitter is:\nhttps://twitter.com/ImGullyTV\nHis YouTube channel is coming soon!')

bot.run("NTM3NjI4MDIzNzUxNDQyNDUz.DypeTA.lYbx_vwiFjtQZT754IxkE8WD1BU")

