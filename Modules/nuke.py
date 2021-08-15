import discord
async def nuke(ctx, amount):
    embed = discord.Embed(title="NUKED by Doz SB", description="...", color=0xa600ff)
    embed.set_image(
        url="https://cdn.dribbble.com/users/303309/screenshots/1568411/smoke_pink.gif")
    async with ctx.typing():
        position = ctx.channel.position
        await ctx.channel.delete()
        c = await ctx.channel.clone()
        await c.edit(position=position)
    await c.send(embed=embed)