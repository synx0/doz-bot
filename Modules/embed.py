import discord
async def embed(ctx, body):
    embed = discord.Embed(title=" ", description=body, color=0xa600ff)
    await ctx.send(embed=embed)