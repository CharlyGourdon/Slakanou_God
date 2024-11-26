from discord.ext import commands
import random
from utils import log_command


class RollCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx, dice: str):
        """
        Lance des dés au format NdM (N = nombre de dés, M = nombre de faces).
        """
        try:
            # Séparation du format NdM
            num_dice, num_faces = map(int, dice.lower().split('d'))
            if num_dice <= 0 or num_faces <= 0:
                raise ValueError

            # Lancers et calcul des résultats
            rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
            total = sum(rolls)

            # Répondre avec le résultat
            await ctx.send(f"🎲 Résultat : {rolls} (Total : {total})")
        except ValueError:
            await ctx.send("Format invalide ! Utilise `!roll NdM`, où N est le nombre de dés et M le nombre de faces.")
        log_command(ctx, f"{rolls} ({total})")


async def setup(bot):
    await bot.add_cog(RollCog(bot))
