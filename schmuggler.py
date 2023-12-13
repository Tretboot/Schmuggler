import random
import tkinter as tk

# Spieleinstellungen

PLANETEN = [
    ("Tatooine", "Wüstenplanet", ["Metall", "Wasser", "Treibstoff", "Nahrung", "Technologie", "Handelswaren"]),
    ("Alderaan", "Grüner Planet", ["Nahrung", "Technologie", "Handelswaren"], ["Spezialwaren", "Kriminalware", "Waffen"]),
    ("Yavin IV", "Waldplanet", ["Spezialwaren", "Kriminalware", "Waffen"], ["Technologie", "Handelswaren", "Nahrung"]),
]

WAREN = [
    ("Metall", 100),
    ("Wasser", 50),
    ("Treibstoff", 75),
    ("Nahrung", 25),
    ("Technologie", 125),
    ("Handelswaren", 150),
    ("Spezialwaren", 200),
    ("Kriminalware", 250),
    ("Waffen", 300),
]

# Spieler

SPIELER = []

class Spieler:

    def __init__(self, planet, schiffsname):
        self.planet = planet
        self.schiff = Schiff()
        self.einkommen = 0
        self.standing = {}

        # Schiffsname
        self.schiff.name = schiffsname

class Schiff:

    def __init__(self):
        self.waren = {}
        for ware in WAREN:
            self.waren[ware] = 0

class Spielfenster:

    def __init__(self):
        # Erstelle ein neues Fenster
        self.window = tk.Tk()
        self.window.title("Schmugglerspiel")
        self.window.geometry("800x600")

        # Erstelle ein Label für den Spieltitel
        self.label_titel = tk.Label(self.window, text="Schmugglerspiel")
        self.label_titel.pack()

        # Erstelle eine Spielfläche
        self.spielfläche = tk.Canvas(self.window, width=800, height=600)
        self.spielfläche.pack()

        # Erstelle Steuerelemente
        self.button_start = tk.Button(self.window, text="Start", command=self.start_spiel)
        self.button_start.pack()

        # Erstelle Steuerelemente
        self.button_info = tk.Button(self.window, text="Info", command=self.info)
        self.button_info.pack()

    def start_spiel(self):
        # Erstelle drei Spieler
        for i in range(3):
            spieler = Spieler(random.choice(PLANETEN), input("Wie möchtest du dein Schiff nennen? "))
            SPIELER.append(spieler)

        # Spielschleife
        run = True
        while run:
            # Runde starten
            for spieler in SPIELER:
                spieler.planet = random.choice(PLANETEN)

            # Spieleraktionen verarbeiten
            for spieler in SPIELER:
                spieler.aktion()

            # Runde abschließen
            for spieler in SPIELER:
                spieler.einkommen = 0

            # Beenden?
            for spieler in SPIELER:
                if spieler.einkommen < 0:
                    run = False
                    break

        # Spiel beenden
        self.window.destroy()

    def info(self):
        # Info-Fenster erstellen
        self.info_fenster = tk.Tk()
        self.info_fenster.title("Info")
        self.info_fenster.geometry("400x200")

        # Info-Label erstellen
        self.label_info = tk.Label(self.info_fenster, text="Dieses Spiel wurde mit der Bard AI von Google programmiert.")
        self.label_info.pack()

        # Info-Fenster anzeigen
        self.info_fenster.mainloop()


if __name__ == "__main__":
    # Erstelle ein neues Spielfenster
    spielfenster = Spielfenster()

    # Starte das Spielfenster
    spielfenster.window.mainloop()
