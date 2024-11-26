import discord
from discord.ext import commands
import random
from utils import log_command


class YesNoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yesno")
    async def yesno(self, ctx, *, text: str):
        """
        Commande : !yesno <texte>
        """
        choice = random.choice(["YES", "NO"])
        emojis_yes = ["\U0001F1FE", "\U0001F1EA", "\U0001F1F8"]  # Y E S
        emojis_no = ["\U0001F1F3", "\U0001F1F4"]  # N O
        reactions = emojis_yes if choice == "YES" else emojis_no

        message = ctx.message
        try:
            for emoji in reactions:
                await message.add_reaction(emoji)
        except discord.errors.HTTPException as e:
            await print("Erreur lors de l'ajout des réactions. Vérifiez que les emojis sont corrects.")
            print(f"Erreur : {e}")
        log_command(ctx, choice)


async def setup(bot):
    await bot.add_cog(YesNoCog(bot))
