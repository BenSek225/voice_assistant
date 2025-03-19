# voice_assistant/scripts/voice_output.py
# Synthèse vocale pour répondre

import pyttsx3

def speak(text):
    """Convertit le texte en voix et le lit."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("lang", "fr-FR")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Bonjour, je suis ton assistant vocal !")
    speak("Que puis-je faire pour vous ?")