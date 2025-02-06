
# 🎹 KeySonic – Coole, individuelle Typing-Sounds mit SonicPi

**KeySonic** ist ein 🖥️ **OSC-Client für Python**, der mithilfe von `evdev` auf Keyboard-Events lauscht und diese als **OSC-Messages** an Sonic Pi sendet. Das bedeutet, dass du jeder Taste (oder Tastengruppen) deines Keyboards einen individuellen Sound zuweisen kannst. 🎼✨

Dank der einfachen Skriptbarkeit von Sonic Pi ist das ein Kinderspiel! 🎮🎶

## 📥 Installation

Damit **KeySonic** funktioniert, benötigst du eine **laufende Sonic Pi-Instanz**, in der du deine Sounds definierst. 🎵

Sonic Pi ist offiziell verfügbar für:  
✅ Windows  
✅ macOS  
✅ Raspberry Pi

Auf **Linux** ist Sonic Pi in einigen `apt`-Repositories enthalten, kann aber auch über **Flatpak** installiert werden.

### 🐧 Installation von Sonic Pi unter Ubuntu

In einigen Distributionen kannst du Sonic Pi direkt über `apt` installieren:

```bash
sudo apt install sonic-pi
```

> ⚠️ **Achtung:**  
> Die `apt`-Version ist oft **veraltet**. Um die **neueste Version** zu installieren, solltest du **Flatpak** nutzen.

#### 🚀 Installation mit Flatpak

Falls du **Flatpak** noch nicht installiert hast, kannst du es mit folgendem Befehl einrichten:

```bash
sudo apt install flatpak flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Dann kannst du Sonic Pi mit folgendem Befehl installieren:

```bash
flatpak install flathub net.sonic_pi.SonicPi
```

Und schließlich startest du es mit:

```bash
flatpak run net.sonic_pi.SonicPi
```


## 🐍 Python-Umgebung

Stelle sicher, dass **Python** auf deinem System installiert ist. Das kannst du mit folgendem Befehl testen:

```bash
python3 --version
```

Falls Python nicht installiert ist, solltest du es über den Paketmanager deines Systems nachinstallieren.

---

## 🚀 Erste Schritte

### 📂 Repository klonen

Kopiere das Repository auf dein System:


```bash
git clone https://github.com/SpiritBits/KeySonic.git
```

### 🔧 Virtuelle Umgebung einrichten

Öffne ein Terminal und navigiere in das KeySonic-Verzeichnis:

```bash
cd ~/KeySonic
```

Erstelle eine virtuelle Umgebung:

```bash
python3.10 -m venv venv
```

Aktiviere die virtuelle Umgebung:

```bash
source venv/bin/activate
```

Falls du die benötigten Bibliotheken noch nicht installiert hast, kannst du sie jetzt hinzufügen:


```bash
pip install python-osc evdev
```

> ❌ **Virtuelle Umgebung beenden**:  
> Falls du die virtuelle Umgebung später verlassen möchtest, kannst du dies mit:

```bash
deactivate
```

---

## 🎵 KeySonic starten

Sobald alles eingerichtet ist, kannst du KeySonic starten. **Stelle sicher, dass Sonic Pi bereits läuft!**

```bash
python3.10 keySonic.py
```

Wenn du eine Taste drückst, die nicht definiert ist, zeigt die Log-Ausgabe Folgendes an (Beispiel: `leftshift`):

🚫 **Keine Note für Taste leftshift**

Falls du bestimmte Tasten hinzufügen möchtest, kannst du diese in die `key_mapping`-Tabelle eintragen, zusammen mit Standardwerten für **Lautstärke (`amp`)** und **Position (`pan`)**.

---

## 🎼 Sonic Pi verbinden

Wenn KeySonic läuft und Sonic Pi gestartet ist:

1️⃣ **Öffne die Datei `spCode.py`**  
2️⃣ **Kopiere den Code** in Sonic Pi  
3️⃣ **Starte die Live-Loop** mit ▶️ **Play**

Wenn alles funktioniert, solltest du nun **ultracoole Typing-Sounds in Stereo** hören! 🎧🎶✨

---

## 🎉 Viel Spaß, Tasten-DJ! 🎛️🎚️🎶

Falls du Fragen hast oder Verbesserungen vorschlagen möchtest, erstelle gerne ein **Issue** auf GitHub oder schicke eine **Pull-Request**. 🚀

## 🎛️ Tipps für den perfekten Sound

Dank der **Leichtgewichtigkeit** und **Flexibilität** von Sonic Pi kannst du nicht nur einfache Klänge, sondern auch **komplexe Synths, Effekte und Modulationen** ansteuern. 🎚️🎶
Du kannst auch eigene Samples einbinden, lese dazu das Sonic-Pi Tutorial. 

Aber **Vorsicht**! ⚠️ Da Tastendrücke sehr schnell hintereinander ausgelöst werden können, solltest du darauf achten, **nur kurze Sounds** zu definieren. **Länger ausklingende Samples** können sich sonst schnell überlagern und einen **chaotischen Klangmatsch** erzeugen. 🎵💥🎵

