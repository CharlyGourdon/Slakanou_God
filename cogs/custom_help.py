from discord.ext import commands
import discord
from utils import log_command


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Affiche la liste des commandes disponibles.")
    async def help(self, ctx, command_name: str = None):
        """
        Display the list of available commands.
        """
        if command_name:
            command = self.bot.get_command(command_name)
            if command:
                await ctx.send(f"**Aide pour `!{command.name}`**\n{command.help}")
            else:
                await ctx.send(f"commande `!{command.name} introuvable.")
        else:
            embed = discord.Embed(
                title="Liste des commandes",
                description="Voici les commandes disponibles.",
                color=discord.Color.blue()
            )
            for command in self.bot.commands:
                if not command.hidden:
                    embed.add_field(
                        name=f"!{command.name}",
                        value=command.help or "Pas de description",
                        inline=False
                    )
            embed.set_footer(text="Tapez !help pour afficher cette aide.")
            await ctx.send(embed=embed)
        log_command(ctx)


async def setup(bot):
    await bot.add_cog(Help(bot))
