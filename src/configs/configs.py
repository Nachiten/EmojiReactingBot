import os


class Configs:
    # ############################################################### #

    # ### Campos que deben estar seteados como Environment (bot.env.example) ### #

    # Discord Token | String | Token unico del bot de dicord
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
    CANAL_OUTPUT_COMANDOS_ID = os.environ["CANAL_OUTPUT_COMANDOS_ID"]

    # ############################################################### #

    # Emojis utilizados
    emojis = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶',
              '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣',
              '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '❓']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9', '?']

    otherEmojis = ['✴️', '🅰️', '🅱️', '🅾️']
    colorEmojis = ['🟩', '🟪', '🟥', '🟦', '🟧', '🟨', '🟫', '⬜']
