import discord
import typing 
import datetime

from discord.ext import commands

Materials = {
    "Sunday":
    {
        "Weapon":
        {
            "Mondstadt":"Everything",
            "Liyue":"Everything",
            "Inazuma":"Everything",
        },
        "Talents":
        {
            "Mondstadt":"Everything",
            "Liyue":"Everything",
            "Inazuma":"Everything",
        },
    },
    "Monday":
   {
        "Weapon":
        {
            "Mondstadt":["Decarabian Fragmentsf", f"<:Item_Decarabian:876129956835508316>"],
            "Liyue":["Guyun Pillars", f"<:Item_Guyun:876130427847467090>"],
            "Inazuma":f"<Item_Distant_Sea:876130649617088582>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Freedom:876131534703312957>",
            "Liyue":f"<:Item_Prosperity:876131742552047616>",
            "Inazuma":f"<:Item_Transience:876128484831920169>",
        },
    },
    "Tuesday":
    {
        "Weapon":
        {
            "Mondstadt":f"<:Item_Boreal_Wolf:876134331322626048>",
            "Liyue":f"<:Item_Mist_Veiled:876134470636412978>",
            "Inazuma":f"<:Item_Narukami:876134580808216586>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Resistance:876134703613222953>",
            "Liyue":f"<:Item_Diligence:876134799998345226>",
            "Inazuma":f"<:Item_Elegance:876134907884224523>",
        }
    },
    "Wednesday":
    {
        "Weapon":
        {
            "Mondstadt":f"<:Item_Dandelion:876127296732405810>",
            "Liyue":f"<:Item_Aerosiderite:876127296703037440>",
            "Inazuma":f"<:Item_Mask:876127296484958289>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Ballad:876128484882280548>",
            "Liyue":f"<:Item_Gold:876128484643201025>",
            "Inazuma":f"<:Item_Light:876128484810952715>",
        },
    },
    "Thursday":
   {
        "Weapon":
        {
            "Mondstadt":f"<:Item_Decarabian:876129956835508316>",
            "Liyue":f"<:Item_Guyun:876130427847467090>",
            "Inazuma":f"<Item_Distant_Sea:876130649617088582>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Freedom:876131534703312957>",
            "Liyue":f"<:Item_Prosperity:876131742552047616>",
            "Inazuma":f"<:Item_Transience:876128484831920169>",
        },
    },
    "Friday":
    {
        "Weapon":
        {
            "Mondstadt":f"<:Item_Boreal_Wolf:876134331322626048>",
            "Liyue":f"<:Item_Mist_Veiled:876134470636412978>",
            "Inazuma":f"<:Item_Narukami:876134580808216586>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Resistance:876134703613222953>",
            "Liyue":f"<:Item_Diligence:876134799998345226>",
            "Inazuma":f"<:Item_Elegance:876134907884224523>",
        },
    },
    "Saturday":
    {
        "Weapon":
        {
            "Mondstadt":f"<:Item_Dandelion:876127296732405810>",
            "Liyue":f"<:Item_Aerosiderite:876127296703037440>",
            "Inazuma":f"<:Item_Mask:876127296484958289>",
        },
        "Talents":
        {
            "Mondstadt":f"<:Item_Ballad:876128484882280548>",
            "Liyue":f"<:Item_Gold:876128484643201025>",
            "Inazuma":f"<:Item_Light:876128484810952715>",
        },
    },
}


class Genshin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(title="hell yeah")
        embed.description = "hell yeah 2"
        await ctx.send(embed=embed)
        
    @commands.command()
    async def talents(self, ctx):
        week_day = datetime.datetime.today().strftime('%A')
        
        embed = discord.Embed(title=week_day)
        embed.add_field(name="Mondstadt", value=f"{Materials[week_day]['Talents']['Mondstadt']}", inline=True)
        embed.add_field(name="Liyue", value=f"{Materials[week_day]['Talents']['Liyue']}", inline=True)
        embed.add_field(name="Inazuma", value=f"{Materials[week_day]['Talents']['Inazuma']}", inline=True)
        
        await ctx.send(embed=embed)
        
        
        
        
def setup(bot):
    bot.add_cog(Genshin(bot))