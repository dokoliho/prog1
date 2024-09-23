# Berechnung der Uhrzeit für Menschen

sec = int(input("Wie viele Sekunden sind seit Mitternacht vergangen? "))

hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60

print (f"Es ist {hours:02}:{minutes:02}:{seconds:02}.")