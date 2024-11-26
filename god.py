import discord
from discord.ext import commands
from utils import get_token, load_all_cogs


# Configurer les intents requis
intents = discord.Intents.default()
intents.message_content = True

# Création du bot avec un préfixe pour les commandes et les intents
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """
    Événement : lorsque le bot est prêt
    """
    # Charger les cogs au démarrage du bot
    await load_all_cogs(bot)
    print(f"{bot.user} est connecté et prêt à l'emploi !")

# Démarrer le bot
bot.run(get_token())
