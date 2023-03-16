import random

print("Willkommen beim Witzemaster. Ich werde dir die Weltbesten Witze erzählen")
print("")

while True:

    Witze = ["Hast du ein Bad genommen?“ – Warum, fehlt eins?",
"Egal, wie gut du schläfst: Albert schläft wie Einstein",
"Wissenschaftler haben herausgefunden – und sind wieder reingegangen.",
"Sitzt einer im Stehcafé.",
"Wie heißt der Schutzpatron der Vergesslichen? – Dings",
"Hast du was zu trinken? – Wasser. – Nee, was Härteres! – Ok, Eis.",
"Was ist rot und steht im Wald? – Ein Kirsch",
"Was ist weiß und rollt den Berg rauf? – Eine Lawine mit Heimweh",
"Wie nennt man einen Bumerang, der nicht zurückkommt? – Stock",
"Was ist das Gegenteil von Reformhaus? – Reh hinterm Haus",
"Wie nennt man ein Delfin in Unterhose? – Slipper",
"Egal wie voll du bist, Rudi war Völler."]

    print (random.choice(Witze))

    print("")

    play_again = input("Möchtest du noch einen Witz (j/n)? ").lower()
    if play_again != "j":
        break

print("Danke für deine Zeit!")
input("Zum Beenden beliebige Taste drücken.")