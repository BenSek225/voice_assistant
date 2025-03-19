# voice_assistant/scripts/commands.py
# Gestion des commandes vocales

import datetime
import os
import webbrowser

def process_command(command, speak_func):
    """Traite les commandes vocales et exécute les actions."""
    if not command:
        return

    # Commande : Dire l’heure
    if "quelle heure" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak_func(f"Il est {current_time}.")

    # Commande : Ouvrir Chrome
    elif "ouvre chrome" in command:
        try:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak_func("J’ouvre Chrome.")
        except FileNotFoundError:
            speak_func("Chrome n’est pas installé à cet emplacement.")

    # Commande : Ouvrir Notepad
    elif "ouvre notepad" in command:
        os.startfile("notepad.exe")
        speak_func("J’ouvre le Bloc-notes.")

    # Commande : Ouvrir Google
    elif "ouvre google" in command:
        webbrowser.open("https://www.google.com")
        speak_func("J’ouvre Google.")

    # Commande : Arrêter
    elif "arrête" in command or "stop" in command:
        speak_func("Au revoir !")
        raise SystemExit  # Ferme proprement le programme

    else:
        speak_func("Je ne comprends pas cette commande.")

if __name__ == "__main__":
    from voice_output import speak
    process_command("quelle heure", speak)