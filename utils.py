import os
from datetime import datetime
import logging


def get_token():
    try:
        with open("token.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.error("Error : File 'token.txt' not found.")
        exit(1)


async def load_all_cogs(bot):
    """
    Async function to load all cogs
    """
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            logging.info(f"Cog {filename} loaded!")


def log_command(ctx, output=None):
    extra = f" -- {output}" if output else ""
    logging.info(
        f"#{ctx.channel} @{ctx.author}: {ctx.message.content}{extra}")
