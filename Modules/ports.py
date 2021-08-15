from discord import Embed
async def ports(ctx):
    embed = Embed(title="", description="""
__**VERIZON 4G LTE:**__
UDP - 1900
UDP - 53, 123, 500, 4500, 52248
TCP - 2859, 5000
TCP - 53

__**AT&T Wi-Fi HOTSPOTS
ATTACK PORTS:**__
UDP - 137, 138, 139, 445, 8053
TCP - 1434, 8053, 8083, 8084

__**STANDARD PORTS:**__
HOME: 80, 53, 22, 8080
XBOX: 3074
PS4: 9307

__**PS3:**__
UDP:3478, 3479
TCP:3478, 3479, 3480, 5223

__**Other:**__
HOTSPOT: 9286
VPN: 7777
NFO: 1192
OVH: 992
HTTP: 80, 8080,443
699 - Good For Hotspots
5060 - Router Reset Port

    """, color=0xa600ff)
    embed.set_footer(text="Doz")
    await ctx.send(embed=embed)