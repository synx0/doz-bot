import discord
async def bug_report(ctx, bot, report_channel):
    embed = discord.Embed(title="Bug Report Menu", description="Please explain the Bug that you have found and a brief description of how to recreate this bug.", color=0xa600ff)
    m = await ctx.send(embed=embed)
    bug = await bot.wait_for("message", check=lambda message: message.author == ctx.message.author)
    await m.delete()
    embed = discord.Embed(title="Bug Successfully Reported:", description=f"\n{bug.content}", color=0xa600ff)
    await ctx.send(embed=embed)
    report = await bot.fetch_channel(report_channel)
    embed = discord.Embed(title="BUG", description=bug.content, color=0xa600ff)
    await report.send(embed=embed)