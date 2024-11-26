import os
from datetime import datetime

def get_token():
    try:
        with open("token.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Erreur : Le fichier 'token.txt' est introuvable.")
        exit(1)


async def load_all_cogs(bot):
    """
    Fonction asynchrone pour charger tous les cogs
    """
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Cog {filename} chargé !")

def log_command(ctx, output):
    print(f"{datetime.now()} -- #{ctx.channel} @{ctx.author}: {ctx.message.content} -- {output}")