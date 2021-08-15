from Modules.toutatis import *
import discord
async def insta(ctx, username):
    sessionId = "4987630288%3AKHd6oPVUc9i5wY%3A27"
    response = getInfo(username, sessionId)
    name = response["full_name"]
    private = response["is_private"]
    pfp = response["profile_pic_url"]
    followers = response["follower_count"]
    following = response["following_count"]
    bio = response["biography"]
    url = response["external_url"]
    embed = discord.Embed(title="Instagram Search", color=0xa600ff)
    embed.set_thumbnail(url=pfp)
    embed.add_field(name="Name", value=f"{name}.", inline=True)
    embed.add_field(name="Private?", value=f"{private}", inline=True)
    embed.add_field(name="Followers", value=f"{followers}", inline=False)
    embed.add_field(name="Following", value=f"{following}", inline=False)
    embed.add_field(name="Bio", value=f"{bio}.", inline=True)
    embed.add_field(name="Url", value=f"{url}.", inline=False)
    await ctx.send(embed=embed)