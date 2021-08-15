import subprocess
import discord
async def socials(ctx, emails):
    embed = discord.Embed(title=" ", description=f"Fetching socials for __**{emails}**__ , this could take 10-20 seconds", color=0xa600ff)
    embed.set_footer(text="Doz")
    c = await ctx.send(embed=embed)
    fetch = "holehe --only-used --no-color " + str(emails)
    output = subprocess.Popen(fetch, shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    await c.delete()
    embed = discord.Embed(title=" ", description=output, color=0xa600ff)
    await ctx.send(embed=embed)