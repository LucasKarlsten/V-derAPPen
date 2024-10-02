import vader as wa

def main():
    # API-nyckel
    api_key: str = "17f1f567d5ead14df048349b68629fb4"

    # Skapa instans från WeatherAPI klassen
    weather_api: str = wa.WeatherAPI(api_key)

    # Starta en loop som frågar efter städer och hämtar väder
    while True:
        # Hämta stad från användaren, som fortsätter i while loopen sålänge inte ens stad har angetts
        stad: str = wa.UserInput.get_stad()

        # Hämta väderdata från API:t
        väderdata: str = weather_api.get_väder(stad)

        # Om vi fick data, skriv ut väderinformationen
        if väderdata:
            väderinfo: str = wa.WeatherApp.skriv_ut_väder(väderdata, stad)
            print(väderinfo)

        # Fråga om användaren vill ange en till stad
        while True:
            userSvar: str = input("Vill du ange en till stad? (ja/nej): ").lower()
            if userSvar == 'ja':
                # Fortsätt loopen för att ange en ny stad
                break
            elif userSvar == 'nej':
                # Avsluta while-loopen och därmed programmet
                print("Programmet avslutas.")
                return
            else:
                # Felmedelande om man är inkapabel till att skriva ja eller nej
                print("Fel: Ange 'ja' eller 'nej'")

# Praxis.
if __name__ == "__main__":
    main() 
