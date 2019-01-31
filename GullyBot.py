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
async def on_member_join(ctx, member):
    await member.add_roles("537626518566862849")
    
@bot.command(pass_context=True)
async def test(ctx):
    await ctx.channel.send('The bot is being programmed and this is a test :)')

@bot.command(pass_context=True)
@commands.has_any_role('Gully', "Moderators")
async def clear(ctx, number=100, silent='a'):
    mgs = [] 
    number = int(number) + 1
    async for x in ctx.channel.history(limit = number):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    silent = str(silent)
    if silent == 'a':
        await ctx.channel.send(f'`{number} messages have been deleted!`')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('`You must be a moderator to do this command!`')

@bot.command(pass_context=True)
@commands.has_any_role('Gully', "Moderators")
async def announce(ctx, *args):
    mgs = [] 
    async for x in ctx.channel.history(limit = 1):
        mgs.append(x)
    await ctx.channel.delete_messages(mgs)
    say = ' '.join(args)
    await ctx.send(say)
    
@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('`You must be a moderator to do this command!`')


    
@bot.command(pass_context=True)
async def gully(ctx):
    await ctx.channel.send(f'{ctx.author.mention}, Gully\'s twitch is: \nhttps://twitch.tv/imgully\nHis twitter is:\nhttps://twitter.com/ImGullyTV\nHis YouTube channel is coming soon!')

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.author
    help = discord.Embed(color=discord.Color.gold())
    help.set_author(name='Heres all the commands')
    help.add_field(name='Commands', value='!clear - This is a moderator only command that clears a certain amount of messages!\n!gully - Show\'s all of gully\'s social\'s\nThat\'s it so far!')

    try:
        await ctx.author.send(embed=help)
    except discord.Forbidden:
        await ctx.send(f'{ctx.author.mention}, I couldn\'t send a message to you.')

bot.run("NTM3NjI4MDIzNzUxNDQyNDUz.DypeTA.lYbx_vwiFjtQZT754IxkE8WD1BU")


