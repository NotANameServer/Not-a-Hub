"""
Bonjour,
On va essayer de voir un bot très simple
(mais en prenant de bonnes habitudes).
Vous avez un fichier requirements.txt pour faire :
`pip install -r requirements.txt` qui devraient tout installer.
ou vous pouvez installer les librairies une par une
(ça sera en commentaire de chaque import)
commençons.
"""


# On importe la librairie discord.py (personne ne s'étonne)
# On importe aussi la lib dotenv, qui nous permettra de ne pas mettre notre
# TOKEN discord en clair dans notre code.
# On le mettra dans le fichier .env, que l'on prendra soin de ne pas mettre
# sur github, grâce au fichier .gitignore qui contient une ligne .env
# Sur github, et sur le code que vous avez télécharger,
# vous ne voyez un fichier .env.public ? Renommez le en .env !

import os

import discord  # pip install discord.py
from discord.ext import commands
from dotenv import load_dotenv  # pip install python-dotenv


# On charge le fichier .env, et on récupère notre TOKEN
load_dotenv()  # pas besoin de spécifier ".env", c'est le nom par défaut
TOKEN = os.getenv("TOKEN")


# nous devons définir quels "intents" va devoir nécessiter notre bot
# généralement, je vous conseille `message_content` et `members`
# vous devez les activer dans la console développeur Discord pour votre bot.
# dans la section "Privileged intents"
intents = discord.Intents.default()
intents.message_content = True  # pour que votre bot lise les commandes
# intents.members = True  # pas utile dans cet exemple, mais ça peut servir


# Utilisez votre propre prefix, évidemment, ici ce sera !
# donc mes commandes seront du genre !ping
bot = commands.Bot(command_prefix="!", intents=intents)


# Cette fonction sera lancée quand le bot sera "ready"
# ici, je m'en sers pour voir si tout se passe bien, au lancement
# Pour l'instant elle ne fait rien de très "utile", mais c'est utile je trouve
# bien sûr, vous pouvez remplacer print par le module `logging`
@bot.event
async def on_ready():
    """Log in Discord."""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# -----------------------------------------------------------------------------
# OK, on va créer nos premières commandes
# le prefix du décorateur @bot.command, "bot" c'est parce que mon bot s'appelle
# "bot" (quand j'ai défini bot = commands.bot)
# si votre bot s'appelle mybot, vous remplacez par mybot.command

@bot.command()
async def ping(ctx):
    """Envoyer un ping"""
    await ctx.send("Pong")


@bot.command()
async def add(ctx, left: int, right: int):
    """Faire la somme de 2 nombres.
    Ex : !add 2 3
    """
    await ctx.send(left + right)


@bot.command()
async def salut(ctx):
    """Répondre avec mon nom.
    Exemple :
    je tape !salut
    il va me répondre `Ho salut, Sergei`
    """
    await ctx.send(f"Ho salut, {ctx.author.name}")


@bot.command()
async def do(ctx):
    """Bien sûr, vous pouvez effectuer des opérations
    (appeler une fonction, utiliser une API pour optenir une information, etc)
    L'exemple suivant est un peu idiot, mais vous avez l'idée.
    Vous n'êtes pas obligés de n'écrire qu'une ligne ctx.send
    """
    # ici vous pouvez appelez autant de fonctions que vous avez écrites,
    # ou qui sont des librairies, pour... je ne sais pas ?
    # consulter une API qui donne toutes les indications sur un pokemon ?
    # ci dessous est juste un exemple idiot
    my_string = "Hello the world"
    new_string = "..".join(my_string)
    await ctx.send(new_string)


# parenthèse ici. Vous voyez que nous utilisons le paramètre `ctx` pour
# chacune de nos commandes. ctx est pour "Context".
# ici, nous utilisons ctx.send, qui va automatiquement répondre dans
# le même channel, la même guilde, etc... après notre commande
# mais un context contient des informations sur l'auteur de la commande,
# le channel, la guilde (le serveur) etc...
# la documentation :
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#context
# ainsi, vous pouvez utiliser la variable ctx.author, etc...

# ------------------------------------------------------------------------------

# OK, on peut lancer notre bot
# normalement, les commandes !ping et !add 2 3 !salut et !do devraient marcher
if __name__ == "__main__":
    bot.run(TOKEN)


# OK, on ira plus loin dans le dossier 02
