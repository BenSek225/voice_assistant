# voice_assistant/scripts/voice_input.py
# Capture et conversion de la voix en texte

import speech_recognition as sr

def get_voice_input():
    """Écoute le micro et convertit la voix en texte."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dis quelque chose...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        print(f"Tu as dit : {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Désolé, je n’ai pas compris.")
        return None
    except sr.RequestError:
        print("Erreur de connexion à l’API Google.")
        return None

if __name__ == "__main__":
    get_voice_input()