# Assistant Personnel avec Reconnaissance Vocale

Ce projet est un assistant vocal simple en Python qui écoute des commandes vocales, les comprend, et exécute des actions de base comme donner l’heure ou ouvrir des applications. Il utilise la reconnaissance vocale et la synthèse vocale pour interagir avec l’utilisateur de manière naturelle.

---

## 🎯 Fonctionnalités actuelles

Cette version de l’assistant peut exécuter les tâches suivantes grâce à des commandes vocales précises :

1. **Dire l’heure actuelle** :
   - **Commande** : “Quelle heure est-il ?” ou “Quelle heure”
   - **Action** : Récupère l’heure locale de ton ordinateur et la lit à voix haute (ex. “Il est 14 heures 30.”).
   - **Exemple** : Dis “Quelle heure est-il ?” → Réponse : “Il est 15 heures 42.”

2. **Ouvrir Google Chrome** :
   - **Commande** : “Ouvre Chrome”
   - **Action** : Lance Google Chrome et confirme vocalement : “J’ouvre Chrome.”
   - **Note** : Fonctionne si Chrome est installé à son emplacement par défaut sous Windows.

3. **Ouvrir le Bloc-notes (Notepad)** :
   - **Commande** : “Ouvre Notepad” ou “Ouvre le Bloc-notes”
   - **Action** : Ouvre le Bloc-notes de Windows et dit : “J’ouvre le Bloc-notes.”

4. **Ouvrir Google dans le navigateur** :
   - **Commande** : “Ouvre Google”
   - **Action** : Ouvre `https://www.google.com` dans ton navigateur par défaut et dit : “J’ouvre Google.”

5. **Arrêter l’assistant** :
   - **Commande** : “Arrête” ou “Stop”
   - **Action** : Dit “Au revoir !” et ferme le programme.

### Exemple d’interaction
- Tu lances le programme, il dit : “Bonjour, je suis ton assistant vocal. Que puis-je faire pour toi ?”
- Tu dis : “Quelle heure est-il ?” → “Il est 14 heures 30.”
- Tu dis : “Ouvre Chrome” → Chrome s’ouvre + “J’ouvre Chrome.”
- Tu dis : “Arrête” → “Au revoir !” et le programme s’arrête.

### Logs typiques
```
Dis quelque chose...
Tu as dit : quelle heure est-il
Dis quelque chose...
Tu as dit : ouvre google
Dis quelque chose...
Tu as dit : arrête
```

---

## 🛠️ Structure du projet

```
📂 voice_assistant
├── 📂 scripts                # Modules spécifiques
│   ├── 📄 voice_input.py     # Capture et conversion voix -> texte
│   ├── 📄 voice_output.py    # Synthèse vocale (texte -> voix)
│   ├── 📄 commands.py        # Gestion des commandes
├── 📄 main.py                # Script principal
├── 📄 config.py              # Configuration (vide pour l’instant)
├── 📄 requirements.txt       # Dépendances
├── 📄 README.md              # Ce fichier
```

- **`voice_input.py`** : Utilise `SpeechRecognition` pour écouter via le micro et convertir la voix en texte avec l’API Google (gratuite).
- **`voice_output.py`** : Utilise `pyttsx3` pour transformer le texte en voix synthétique locale.
- **`commands.py`** : Contient la logique pour interpréter les commandes et déclencher les actions.
- **`main.py`** : Orchestre tout avec une boucle infinie pour écouter en continu.

---

## 📋 Prérequis

- **Python 3.12** : Téléchargeable sur [python.org](https://www.python.org/downloads/). Coche “Add Python to PATH” lors de l’installation.
- **Microphone** : Un micro intégré ou externe fonctionnel (vérifie dans Paramètres Windows > Son > Test du micro).
- **Haut-parleurs** : Pour entendre les réponses de l’assistant.

### Dépendances Python
- `SpeechRecognition==3.10.4` : Reconnaissance vocale.
- `PyAudio==0.2.14` : Accès au micro (nécessaire pour `SpeechRecognition`).
- `pyttsx3==2.91` : Synthèse vocale.
- `setuptools==75.1.0` : Contourne un problème de compatibilité avec Python 3.12.

---

## 🚀 Installation

### 1. Télécharger ou cloner le projet
- **Option 1 : Télécharger** :
  - Télécharge le ZIP du projet depuis le dépôt (ex. sur GitHub) et extrais-le dans `C:\Users\ASUS\Desktop\voice_assistant`.
- **Option 2 : Cloner (si Git est installé)** :
  ```powershell
  cd C:\Users\ASUS\Desktop\
  git clone <URL_DU_DEPOT>
  cd voice_assistant
  ```

### 2. Créer un environnement virtuel
Dans PowerShell, navigue dans le dossier du projet et crée un environnement virtuel :
```powershell
cd C:\Users\ASUS\Desktop\voice_assistant
python -m venv venv
.\venv\Scripts\activate
```

### 3. Installer les dépendances
Avec l’environnement activé (tu verras `(venv)` dans PowerShell), installe les dépendances :
```powershell
pip install -r requirements.txt
```
- **Note** : Si `PyAudio` échoue :
  - Télécharge `PyAudio-0.2.14-cp312-cp312-win_amd64.whl` sur [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).
  - Place-le dans `C:\Users\ASUS\Desktop\` et installe :
    ```powershell
    pip install C:\Users\ASUS\Desktop\PyAudio-0.2.14-cp312-cp312-win_amd64.whl
    ```

### 4. Lancer l’assistant
Une fois les dépendances installées, lance le programme :
```powershell
python main.py
```

---

## ▶️ Utilisation

1. **Lancer l’assistant** :
   ```powershell
   cd C:\Users\ASUS\Desktop\voice_assistant
   .\venv\Scripts\activate
   python main.py
   ```

2. **Interagir** :
   - L’assistant dit : “Bonjour, je suis ton assistant vocal. Que puis-je faire pour toi ?”
   - Parle clairement dans le micro avec une des commandes listées ci-dessus.
   - Pour arrêter, dis “Arrête” ou “Stop”.

---

## 🧠 Comment ça marche ?

### Reconnaissance vocale
- **`voice_input.py`** :
  - Utilise `SpeechRecognition` avec `PyAudio` pour capturer l’audio du micro.
  - Envoie l’audio à l’API Google Speech-to-Text (gratuite, pas de clé requise) pour le convertir en texte.
  - Ajuste le bruit ambiant pour une meilleure précision.

### Synthèse vocale
- **`voice_output.py`** :
  - Utilise `pyttsx3` pour générer une voix synthétique locale (pas besoin d’internet).
  - Configure la vitesse (150 mots/minute) et tente d’utiliser une voix française.

### Gestion des commandes
- **`commands.py`** :
  - Compare le texte reconnu avec des conditions (`if/elif`) pour déclencher des actions.
  - Utilise `datetime` pour l’heure, `os` pour lancer des apps, et `webbrowser` pour ouvrir des sites.

### Boucle principale
- **`main.py`** :
  - Initialise l’assistant avec un message d’accueil.
  - Écoute en continu dans une boucle `while True` jusqu’à ce que tu dises “Arrête”.

---

## 🌟 Options d’amélioration

Voici des idées pour enrichir cette base :

1. **Ajouter plus d’applications** :
   - Exemple : “Ouvre Word” :
     ```python
     elif "ouvre word" in command:
         os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
         speak_func("J’ouvre Word.")
     ```
   - Ajuste le chemin selon ton installation.

2. **Reconnaissance continue** :
   - Ajoute une commande pour activer/désactiver l’écoute (ex. “Écoute-moi”/“Pause”) :
     ```python
     listening = False
     if "écoute-moi" in command:
         listening = True
     elif "pause" in command:
         listening = False
     ```

3. **Réponses personnalisées** :
   - Ajoute des phrases amusantes :
     ```python
     elif "comment vas-tu" in command:
         speak_func("Je suis une IA, donc toujours bien ! Et toi ?")
     ```

4. **Commandes dynamiques** :
   - Permets d’ouvrir n’importe quel site :
     ```python
     elif "ouvre" in command:
         site = command.replace("ouvre ", "")
         webbrowser.open(f"https://www.{site}.com")
         speak_func(f"J’ouvre {site}.")
     ```

---

## 🛠️ Dépannage

- **Erreur “No module named 'distutils'”** :
  - Assure-toi que `setuptools` est installé. Sinon, downgrade vers Python 3.11 :
    ```powershell
    rmdir /s venv
    python -m venv venv  # Avec Python 3.11
    pip install -r requirements.txt
    ```
- **Micro ne fonctionne pas** :
  - Vérifie Paramètres Windows > Son > Microphone.
  - Teste `voice_input.py` seul :
    ```powershell
    python scripts/voice_input.py
    ```
- **Chrome ne s’ouvre pas** :
  - Vérifie le chemin dans `commands.py` ou installe Chrome à l’emplacement par défaut.

---

## 🎉 Conclusion

Cette version est une base solide pour un assistant vocal simple. Elle montre comment combiner reconnaissance vocale, synthèse vocale, et exécution de commandes sous Windows. Teste les 5 fonctionnalités, joue avec le code, et ajoute tes propres idées pour le personnaliser davantage !
