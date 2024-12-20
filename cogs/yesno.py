import discord
from discord.ext import commands
import random
from utils import log_command
import logging


class YesNoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yesno", help="Réagit au message avec Yes ou NO.")
    async def yesno(self, ctx, *, text: str):
        """
        Command: !yesno <text>
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
            logging.error(
                "Error when adding reactions. PLease verify that emojis are correct.")
            logging.error(f"Error : {e}")
        log_command(ctx, choice)

    @yesno.error
    async def yesno_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Vous devez entrer un message (ex : `!yesno <message>`).")


async def setup(bot):
    await bot.add_cog(YesNoCog(bot))
