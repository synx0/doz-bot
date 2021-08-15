import discord
from Modules import log
from datetime import datetime
from discord.ext import commands
#Setup
bot = commands.Bot(command_prefix='-', intents=discord.Intents().all())
bot.remove_command("help")
report_channel = "enter_report_channelid_here"
log_channel = "enter_log_channelid_here"
server_link = ""


async def perm_menu(ctx):
    command = ctx.message.content
    embed = discord.Embed(title="",
                          description="Sorry you don't have permissions for that command. Nice try though.\n\n" + f"\u0009\u0009\u0009**{command}**\n",
                          color=0xa600ff)
    embed.set_footer(text="Doz")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():

    print(
        f"""
        -_-_-_-_-_-_-_-_-_-_-_-_-_
            DOZ IS NOW ONLINE
        {datetime.now()}
        -_-_-_-_-_-_-_-_-_-_-_-_-_
        """)

@bot.event
async def on_command_error(ctx, error):
    print(error)

@bot.event
async def on_member_join(member):
    from Modules.joins import join
    await join(member, bot)

@bot.command()
async def verify(ctx):
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name="Member")
    await member.add_roles(role)

@bot.command()
@commands.has_permissions(administrator=True)
async def status(ctx, *, args):
    activity = discord.Game(name=args)
    await bot.change_presence(activity=activity)
    embed = discord.Embed(title="Status Updated", description=args, color=0xa600ff)
    await ctx.send(embed=embed)

@bot.command()
async def restart(ctx):
    from Modules import restart
    await restart.restart(ctx, bot)
    await log.log(ctx.message, log_channel, bot)

@bot.command()
async def help(ctx, menu=None):
    from Modules import help
    await help.help(ctx, menu)

@bot.command()
async def latency(ctx):
    ping = bot.latency
    convert = round(ping, 3)
    embed = discord.Embed(title=" ", description=f"Heres that BOT -> DISCORD Latency: \n\n**{convert * 1000} ms**", color=0xa600ff)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, amount=0):
    from Modules import nuke
    await nuke.nuke(ctx, amount)

@bot.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, *, args):
    from Modules import embed
    msg = ctx.message
    await msg.delete()
    await embed.embed(ctx, args)

@bot.command()
async def phone(ctx, num):
    from Modules.phone import search
    msg = ctx.message
    await msg.delete()
    await search(ctx, num)

@bot.command()
async def purge(ctx, limit):
    await ctx.channel.purge(limit=int(limit))
    await ctx.send(f"Purged {limit} messages...")

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, args):
    from Modules import say
    msg = ctx.message
    await msg.delete()
    await say.say(ctx, args)

@bot.command()
async def snipe(ctx, call: discord.Member, *, args):
    from Modules import snipe
    msg = ctx.message
    await msg.delete()
    await snipe.snipe(ctx, call, args)

@bot.command()
async def user(ctx, name: discord.Member):
    from Modules import user
    await user.search(ctx, name)

@bot.command()
async def avatar(ctx, call: discord.Member= None):
    from Modules import user
    await user.avatar(ctx, call)

@bot.command()
async def insta(ctx, username):
    from Modules import insta
    await insta.insta(ctx, username)

@bot.command()
async def socials(ctx, emails):
    from Modules import socials
    msg = ctx.message
    await msg.delete()
    await socials.socials(ctx, emails)

@bot.command()
async def lookup(ctx, ip):
    from Modules import lookup
    await lookup.lookup(ctx, ip)

@bot.command()
async def ports(ctx):
    from Modules import ports
    await ports.ports(ctx)

@bot.command()
async def clear(ctx, lol=0):
    t = int(lol) or 100
    async for c in ctx.channel.history(limit=t):
        try:
            if c.author.id != bot.user.id:
                print("Not Bot Message")
            if c.author.id == bot.user.id:
                print("Bot message found")
                await c.delete()
        except:
            print("Fatal Error")

    await log.log(ctx.message, log_channel, bot)

@bot.command()
async def report(ctx):
    from Modules import report
    await report.bug_report(ctx, bot, report_channel)

bot.run("")