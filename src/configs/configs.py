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
              '🇷', '🇸', '🇹', '🇺', '🇻', '🇼', '🇽', '🇾', '🇿', ]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    otherEmojis = ['✴️', '🅰️', '🅱️', '🅾️']
