import requests
import discord
import json
async def lookup(ctx, ip):
    banned = ["/", "?", ",", "$", "#", "@", "!", "*", "=", "+"]
    if ip in banned:
        await ctx.send("Want the server IP? HERE\n**1.1.1.1**\n\n go hit that fuck-boy")

    if len(ip) > 4:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.request("GET", url)
        output = response.text
        parse = json.loads(output)
        host = parse["query"]
        country = parse["country"]
        region = parse["regionName"]
        city = parse["city"]
        org = parse["org"]
        isp = parse["isp"]
        embed = discord.Embed(title="IP Lookup", description="\n", color=0xa600ff)
        embed.add_field(name="HOST:", value=f"{host}" + " ", inline=True)
        embed.add_field(name="CITY:", value=f"{city}" + " ", inline=True)
        embed.add_field(name="REGION:", value=f"{region}" + " ", inline=True)
        embed.add_field(name="COUNTRY:", value=f"{country}" + " ", inline=True)
        embed.add_field(name="ORG:", value=f"{org}" + " ", inline=True)
        embed.add_field(name="ISP:", value=f"{isp}" + " ", inline=True)
        embed.set_footer(text="Doz")
        await ctx.send(embed=embed)