from discord.ext import commands
import os


class Load(commands.Cog):
    """
    Load commands.
    """
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if ctx.guild is None:
            raise commands.NoPrivateMessage()
        return True

    @commands.has_role("Celery")
    @commands.command(hidden=True, aliases=["laod"])
    async def load(self, ctx, *, module: str):
        """Loads a Cog."""
        try:
            if module[0:7] != "cogs.":
                module = "cogs." + module
            self.bot.load_extension(module)
            self.bot.loaded_cogs.append(module.split('.')[-1])
            await ctx.send('✅ Extension loaded.')
        except Exception as e:
            await ctx.send(f'💢 Failed!\n```\n{type(e).__name__}: {e}\n```')

    @commands.has_role("Celery")
    @commands.command(hidden=True, aliases=["unlaod"])
    async def unload(self, ctx, *, module: str):
        """Unloads a Cog."""
        try:
            if module[0:7] != "cogs.":
                module = "cogs." + module
            if module == "cogs.load":
                await ctx.send("❌ I don't think you want to unload that!")
            else:
                self.bot.unload_extension(module)
                await ctx.send('✅ Extension unloaded.')
        except Exception as e:
            await ctx.send(f'💢 Failed!\n```\n{type(e).__name__}: {e}\n```')

    @commands.has_role("Celery")
    @commands.command(name='reload', aliases=["relaod"])
    async def _reload(self, ctx, *, module: str):
        """Reloads a Cog."""
        if module == "all":
            module = entry in os.listdir('cogs')
        try:
            if module[0:7] != "cogs.":
                module = "cogs." + module
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
            await ctx.send('✅ Extension reloaded.')
        except Exception as e:
            await ctx.send(f'💢 Failed!\n```\n{type(e).__name__}: {e}\n```')


def setup(bot):
    bot.add_cog(Load(bot))
