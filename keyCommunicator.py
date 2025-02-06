import evdev
import time
#from pythonosc.udp_client import SimpleUDPClient
from pythonosc import udp_client

# 🎛️ PiSonic-Server läuft auf localhost:4560
client = udp_client.SimpleUDPClient("127.0.0.1", 4560)

# 🖮 Dein Keyboard-Gerät (Finde es mit `ls /dev/input/event*` und `sudo evtest`)
device = evdev.InputDevice('/dev/input/event2')

# 🎹 Mapping für verschiedene Tasten zu Noten (z.B. Schreibmaschinen-Sound oder Synth-Pads)
# [Note, amp, pan]
key_map = {
    'q':(50,1.0,-1.0),
    'w':(50,1.0,-0.8),
    'e':(50,1.0,-0.6),
    'r':(50,1.0,-0.4),
    't':(50,1.0,-0.2),
    'a':(51,1.0,-1.0),
    's':(51,1.0,-0.8),
    'd':(51,1.0,-0.6),
    'f':(51,1.0,-0.4),
    'g':(51,1.0,-0.2),
    'y':(52,1.0,-1.0),
    'x':(52,1.0,-0.8),
    'c':(52,1.0,-0.6),
    'v':(52,1.0,-0.4),
    'b':(52,1.0,-0.2),
    'z':(50,1.0,0.2),
    'u':(50,1.0,0.4),
    'i':(50,1.0,0.6),
    'o':(50,1.0,0.8),
    'p':(50,1.0,1.0),
    'ü':(50,1.0,0.2),
    'h':(51,1.0,0.4),
    'j':(51,1.0,0.6),
    'k':(51,1.0,0.8),
    'l':(51,1.0,1.0),
    'ö':(51,1.0,0.2),
    'ä':(51,1.0,0.4),
    'n':(52,1.0,0.6),
    'm':(52,1.0,0.8),
    'dot':(61,1.0,0.5),
    '-':(50,1.0,0.5),
    'space':(55,1.0,0.0),       # Space-Taste
    'rightbrace':(56,1.0,-0.4),  # *+ Taste
    'backslash':(57,1.0,0.4),   # #'  Taste
    #'esc':(58,1.0,0,0),
    'tab':(59,1.0,0.0),
    'apostrophe':(60,1.0,0.0),   # ä Tast '.':(61,1.0,0.0),
    'comma':(62,1.0,-0.5),
    'enter':(63,1.0,0.0),
    'up':(64,1.0,0.0),
    'down':(65,1.0,0.0),
    'left':(66,1.0,-1.0),
    'right':(67,1.0,1.0),
    'backspace':(68,1.0,0.5),
    '1':(70,1.0,-1.0),
    '2':(71,1.0,-0.8),
    '3':(72,1.0,-0.6),
    '4':(73,1.0,-0.4),
    '5':(74,1.0,-0.2),
    '6':(75,1.0,0.2),
    '7':(76,1.0,0.4),
    '8':(77,1.0,0.6),
    '9':(78,1.0,0.8),
    '0':(79,1.0,1.0),
    'slash':(80,1.0,1.0)
}

print("🎶 Type los! Jeder Tastendruck erzeugt einen Sound...")

# 🎼 Event-Loop für Keyboard-Tasten
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value == 1:  # Taste gedrückt
        try:
            key = evdev.ecodes.KEY[event.code].lower().replace("key_", "")
            if key in key_map:
                note, amp, pan = key_map[key]
               # print(f"🔊 Taste {key.upper()} → Note {note}")

                # 🛠 Sound mit PiSonic triggern
                client.send_message("/trigger/prophet", [note,amp,pan])
            
            else:
                print(f"🚫 Keine Note für Taste {key}")
        
        except KeyError:
            pass  # Falls die Taste keinen Eintrag hat, einfach ignorieren

