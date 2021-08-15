import discord
async def join(member, bot):
    try:
        embed = discord.Embed(title="", description=member.name + " has arrived!", color=0xa600ff)
        embed.set_author(name=member.guild.name, icon_url=member.guild.icon_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/824481905235329044/824535628505939988/download_1.gif")
        embed.set_footer(text=f"Welcome to {member.guild.name}.")
        id = member.guild.system_channel.id
        channel = bot.get_channel(id=id)
        await channel.send(embed=embed)
        await channel.send(f"||{member.mention}|| please verify before entering, **-verify**")

    except:
        embed = discord.Embed(title="", color=0xa600ff)
        embed.set_author(name=member.guild.name, icon_url=member.guild.icon_url)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/824481905235329044/824535628505939988/download_1.gif")
        embed.set_footer(text=f"Welcome to {member.guild.name}.")
        await member.send(embed=embed)
        await member.send("You can enter the server with -verify")
