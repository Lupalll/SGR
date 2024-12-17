import os
import random
import webbrowser
#SteamID Array
games = [...]#Insert your Steam Game Id's here

random_game = random.choice(games)

steam_command = f"steam://run/{random_game}"

webbrowser.open(steam_command)

print(f"Starte Spiel mit App-ID: {random_game}")
