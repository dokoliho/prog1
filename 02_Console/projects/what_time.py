# Berechnung der Uhrzeit für Menschen

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

def main():
    sec = int(input("Wie viele Sekunden sind seit Mitternacht vergangen? "))

    hours = sec // SECONDS_PER_HOUR
    minutes = (sec % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds = sec % SECONDS_PER_MINUTE

    print (f"Es ist {hours:02}:{minutes:02}:{seconds:02}.")

main()
