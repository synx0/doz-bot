import discord
async def log(message, log_channel, bot):
    command = message.content
    author = message.author
    logs = await bot.fetch_channel(log_channel)
    embed = discord.Embed(title=" ", description=f"{command}", color=0xa600ff)
    embed.set_author(name=f"{author.name} sent command: ", icon_url=author.avatar_url)
    await logs.send(embed=embed)