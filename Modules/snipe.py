from discord import Embed
async def snipe(ctx, call, quote):
    name = call.display_name
    icon = str(call.avatar_url)
    embed = Embed(description=str(quote), color=0xa600ff)
    embed.set_author(name=name, icon_url=icon)
    await ctx.send(embed=embed)