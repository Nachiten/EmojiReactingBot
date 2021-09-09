import discord

from configs.configs import Configs

# Datos administrativos del bot
cliente = discord.Client()

# Configs
canalOutputComandosID = Configs.CANAL_OUTPUT_COMANDOS_ID
emojis = Configs.emojis
letters = Configs.letters
otherEmojis = Configs.otherEmojis

aUsed = False
bUsed = False
oUsed = False


# Evento de inicializacion
@cliente.event
async def on_ready():
    print("Bot ready")


def getEmojiForLetter(letterInput):
    global aUsed
    global bUsed
    global oUsed

    index = 0
    for letter in letters:
        if letter == letterInput:
            break
        index += 1

    if index == 0:
        if aUsed:
            return otherEmojis[1]
        aUsed = True
    if index == 1:
        if bUsed:
            return otherEmojis[2]
        bUsed = True
    if index == 14:
        if oUsed:
            return otherEmojis[3]
        oUsed = True

    if letterInput == " ":
        return otherEmojis[0]

    return emojis[index]


# Evento de mensaje recibido
@cliente.event
async def on_message(message):
    global aUsed
    global bUsed
    global oUsed

    aUsed = False
    bUsed = False
    oUsed = False

    messageContent = message.content

    # Si no me invocan no respondo
    if not messageContent.startswith("!emoji "):
        return

    mensajeCoso = messageContent.lower()

    messageToIterate = mensajeCoso[7:]

    for char_index in range(len(messageToIterate)):
        char = messageToIterate[char_index]
        emoji = getEmojiForLetter(char)
        await message.add_reaction(emoji)


# Evento de reaccion recibida
@cliente.event
async def on_reaction_add(reaction, user):
    pass


# Corre el bot
cliente.run(Configs.DISCORD_TOKEN)
