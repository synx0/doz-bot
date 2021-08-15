import discord
async def search(ctx, name):
    author = ctx.message.author
    display = name.display_name
    id = name.id
    created_on = name.created_at
    joined_on = name.joined_at
    icon = name.avatar_url
    embed = discord.Embed(title="", color=0xa600ff)
    embed.set_author(name=f"Requested By: {author.name}", icon_url=author.avatar_url)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Name: ", value=display, inline=True)
    embed.add_field(name="ID: ", value=id, inline=True)
    embed.add_field(name="Created On: ", value=created_on, inline=True)
    embed.add_field(name="Joined On: ", value=joined_on, inline=True)
    embed.set_footer(text="Doz")
    await ctx.send(embed=embed)

async def avatar(ctx, call= None):

    if call == None:
        author = ctx.message.author
        image = author.avatar_url
        name = author.name
        embed = discord.Embed(title=f"{name}'s Avatar", color=0xa600ff)
        embed.set_image(url=image)
        embed.set_footer(text="Requested by " + author.name)
        await ctx.send(embed=embed)

    else:
        author = ctx.message.author
        name = call.name
        icon = call.avatar_url
        embed = discord.Embed(title=f"{name}'s Avatar", color=0xa600ff)
        embed.set_image(url=icon)
        embed.set_footer(text="Requested by " + author.name)
        await ctx.send(embed=embed)