import discord
import random

from configs.configs import Configs

# Datos administrativos del bot
cliente = discord.Client()

# Configs
canalOutputComandosID = Configs.CANAL_OUTPUT_COMANDOS_ID
emojis = Configs.emojis
letters = Configs.letters
otherEmojis = Configs.otherEmojis
colorEmojis = Configs.colorEmojis

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


textToUse = ""
emojiToUse = None
pendingMessage = False
userMessage = None
botMessage = None


# Evento de mensaje recibido
@cliente.event
async def on_message(message):
    global emojiToUse
    global textToUse
    global aUsed
    global bUsed
    global oUsed

    aUsed = False
    bUsed = False
    oUsed = False

    global pendingMessage
    pendingMessage = True

    messageContent = message.content

    # Si es mensaje del bot no contesto
    if message.author == cliente.user:
        return

    # Si no me invocan no respondo
    if not messageContent.startswith("!emoji "):
        return

    textToUse = messageContent.lower()[7:]
    indexToUse = random.randint(0, 8)

    emojiToUse = colorEmojis[indexToUse]

    global userMessage
    global botMessage

    userMessage = message
    botMessage = await message.channel.send(f"Please use this emoji: {emojiToUse} "
                                            f"and react to the message where I should add your text.")


# Evento de reaccion recibida
@cliente.event
async def on_reaction_add(reaction, user):
    global pendingMessage

    # Si es mensaje del bot no contesto
    if user == cliente.user or not pendingMessage or not reaction.emoji == emojiToUse:
        print("No es mensaje para mi")
        return

    # Remuevo la reaccion generada por el usuario
    await reaction.remove(user)

    print("Procesando mensaje")

    for char_index in range(len(textToUse)):
        char = textToUse[char_index]
        emoji = getEmojiForLetter(char)
        await reaction.message.add_reaction(emoji)

    await botMessage.delete()
    await userMessage.delete()

    pendingMessage = False

# Corre el bot
cliente.run(Configs.DISCORD_TOKEN)
