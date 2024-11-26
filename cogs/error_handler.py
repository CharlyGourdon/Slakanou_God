from discord.ext import commands
import logging


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"La commande `{ctx.invoked_with}` n'existe pas. Tapez `!help` pour la liste des commandes.")
            logging.info(
                f"CommandNotFound: #{ctx.channel} @{ctx.author}: {ctx.message.content}")
        else:
            raise error


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
