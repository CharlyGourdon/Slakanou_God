import discord
from discord.ext import commands
from utils import get_token, load_all_cogs
import logging


logging.basicConfig(format='%(asctime)s -- %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8',
                    level=logging.INFO)


# Configure required intent
intents = discord.Intents.default()
intents.message_content = True

# Create bot with "!" prefix for commands and intents
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """
    Event: when bot is ready
    """
    # Load cogs at bot booting
    await load_all_cogs(bot)
    logging.info(f"{bot.user} connected and ready to use!")

# Démarrer le bot
bot.run(get_token())
