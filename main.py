# voice_assistant/main.py
# Script principal de l’assistant vocal

from scripts.voice_input import get_voice_input
from scripts.voice_output import speak
from scripts.commands import process_command

def main():
    """Lance l’assistant vocal en boucle."""
    speak("Bonjour, je suis ton assistant vocal. Que puis-je faire pour toi ?")
    while True:
        command = get_voice_input()  # Écoute la commande
        if command:
            if "arrête" in command or "stop" in command:
                speak("Au revoir !")
                break
            process_command(command, speak)  # Traite la commande

if __name__ == "__main__":
    main()