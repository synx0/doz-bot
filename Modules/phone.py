import requests
import discord
import json

async def search(ctx, num):
    try:
        response = requests.request("GET", f"https://demo.phoneinfoga.crvx.fr/api/numbers/{num}/scan/numverify")
        output = response.text
        parse = json.loads(output)
        row = parse["result"]
        formatted_num = row["international_format"]
        carrier = row["carrier"]
        type = row["line_type"]
        area = row["location"]
        country = row["country_name"]
        embed = discord.Embed(title="Phone Search", description="\n", color=0xa600ff)
        embed.add_field(name="NUMBER:", value=f"{formatted_num}" + " ", inline=False)
        embed.add_field(name="CARRIER:", value=f"|{carrier}|" + " ", inline=False)
        embed.add_field(name="TYPE:", value=f"{type}" + " ", inline=False)
        embed.add_field(name="AREA:", value=f"{area}" + " ", inline=False)
        embed.add_field(name="COUNTRY:", value=f"{country}" + " ", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Invalid Number. Make sure to add country code.")

