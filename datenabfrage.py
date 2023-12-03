print("Willkommen bei deiner Datenabfrage")
""
print("Wie ist dein Nachname?")
name = input()
print("hallo " + name )

print("Und wie ist dein Vorname?")
vorname = input()
print("Freut mich " + vorname )

print("Wie alt bist du?")
alter = input()
print("Du bist " + alter )

print("Verrate mir doch bitte deine Postleizahl")
plz = input()
print("Deine Postleizahl ist" + plz )

print("Zum Schluss möchte ich noch wissen, in welchem Ort du wohnst.")
ort = input()
print("Du wohnst in" + ort )

""
print("Danke für deine Antworten")
print( vorname.capitalize() + " " + name.capitalize() + "ist" + alter + " Jahre alt und wohnt in " + plz + " " + ort + "." )
