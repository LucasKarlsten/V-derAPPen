import vader as wa

def main():
    # API-nyckel
    api_key = "17f1f567d5ead14df048349b68629fb4"

    # Skapa instans av WeatherAPI
    weather_api = wa.WeatherAPI(api_key)

    # Starta en loop som frågar efter städer och hämtar väder
    while True:
        # Hämta stad från användaren
        stad = wa.UserInput.get_stad()

        # Hämta väderdata från API:t
        väderdata = weather_api.get_väder(stad)

        # Om vi fick data, skriv ut väderinformationen
        if väderdata:
            väderinfo = wa.WeatherApp.skriv_ut_väder(väderdata, stad)
            print(väderinfo)

        # Fråga om användaren vill ange en till stad
        while True:
            svar = input("Vill du ange en till stad? (ja/nej): ").lower()
            if svar == 'ja':
                break  # Fortsätt loopen för att ange en ny stad
            elif svar == 'nej':
                print("Programmet avslutas.")
                return  # Avsluta funktionen och därmed programmet
            else:
                print("Fel: Ange 'ja' eller 'nej'")  # Felmeddelande om svar inte är giltigt

# Kontrollera om filen körs direkt
if __name__ == "__main__":
    main() 