import discord
from discord.ext import commands
import random


def get_token():
    """
    Lire le token depuis un fichier externe
    """
    try:
        with open("token.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Erreur : Le fichier 'token.txt' est introuvable.")
        exit(1)


# Configurer les intents requis
intents = discord.Intents.default()  # Active les intents de base
# Permet au bot de lire le contenu des messages
intents.message_content = True
# Création du bot avec un préfixe pour les commandes et les intents
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """
    Événement : lorsque le bot est prêt
    """
    print(f"{bot.user} est connecté et prêt à l'emploi !")


@bot.command(name="yesno")
async def yesno(ctx, *, text: str):
    """
    Commande : !yesno <texte>
    """
    choice = random.choice(["YES", "NO"])
    emojis_yes = ["\U0001F1FE", "\U0001F1EA", "\U0001F1F8"]  # Y E S
    emojis_no = ["\U0001F1F3", "\U0001F1F4"]  # N O
    reactions = emojis_yes if choice == "YES" else emojis_no
    print(f"Choix : {choice}, Emojis utilisés : {reactions}")

    message = ctx.message
    try:
        for emoji in reactions:
            await message.add_reaction(emoji)
    except discord.errors.HTTPException as e:
        await print("Erreur lors de l'ajout des réactions. Vérifiez que les emojis sont corrects.")
        print(f"Erreur : {e}")

# Commande : !roll NdM


@bot.command(name="roll")
async def roll(ctx, dice: str):
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


bot.run(get_token())
