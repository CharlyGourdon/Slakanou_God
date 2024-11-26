from discord.ext import commands
import random
from utils import log_command


class RollCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", help="Lance un dé au format XdY (ex : 1d20 pour un dé à 20 faces).")
    async def roll(self, ctx, dice: str):
        """
        Roll dices to format XdY (X = number of dices, Y = number of sides).
        """
        try:
            # split of XdY format
            num_dice, num_faces = map(int, dice.lower().split('d'))
            if num_dice <= 0 or num_faces <= 0:
                raise ValueError

            # Roll + results
            rolls = [random.randint(1, num_faces) for _ in range(num_dice)]
            total = sum(rolls)

            # Send results
            await ctx.send(f"🎲 Résultat : {rolls} (Total : {total})")
        except ValueError:
            await ctx.send("Format invalide ! Utilise `!roll XdY`, où X est le nombre de dés et Y le nombre de faces.")
        log_command(ctx, f"{rolls} ({total})")

    @roll.error
    async def roll_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Vous devez spécifier le format du dé, comme `1d20`.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Format incorrect. Utilisez le format `XdY` (ex : 1d20).")


async def setup(bot):
    await bot.add_cog(RollCog(bot))
