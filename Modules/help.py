from discord import Embed


async def help(ctx, menu= None):
    async def nav_menu():
        embed = Embed(title=" ",
                      description="""```
[ DOZ Help ] 
``` 
> 
> **help user**
>             
> **help net**
>             
> **help mod**
> 
> `d0z.xyz`
        """, color=0xa600ff)
        await ctx.send(embed=embed)

    async def user_menu():
        embed = Embed(title="", description="""``` [ User Commands ] ```
>       **help**\n
        `Brings up this menu`\n
>       **snipe [user] [message]**\n
        `Fake Message Generator`\n
>       **user [user]**\n
        `Get's Discord info for user`\n
>       **insta [username]**\n
        `Pulls an instagram user's info`\n
>       **avatar [@ or id]**\n
        `Pulls avatar of a user`\n
>       **phone [number]**\n
        `Gets basic info based on number`\n
>       **socials [email]**\n
        `Finds all accounts linked to email`\n
>       **report**\n
        `Initiates the report menu`\n
>       __**clear**__\n
        `Clears bot messages in DMs`\n
        """, color=0xa600ff)
        await ctx.send(embed=embed)

    async def mod_menu():
        embed = Embed(title="", description="""``` [ Mod Commands ] ```
        
>         **embed ["content"]**\n
         `Creates Discord embed with content`\n
>         **say ["content"]**\n
         `Regular Discord message`\n
>         **nuke**\n
         `Deletes and recreates a channel`\n
>         **purge [amount]**\n
         `Purges messages from channel`\n 
>         **latency** 
         `Bots Latency to servers`
        """, color=0xa600ff)
        await ctx.send(embed=embed)

    async def net_menu():
        embed = Embed(title="", description="""```
[ Networking Commands ] 
``` 
>       **ports**\n
        `Lists common ports per service`\n
>       **lookup [host]**\n
        `Searches for IP's info, Reverse DNS`\n
        """, color=0xa600ff)
        await ctx.send(embed=embed)


    if menu == None:
        await nav_menu()
    if menu == "user":
        await user_menu()
    if menu == "net":
        await net_menu()
    if menu == "mod":
        await mod_menu()

