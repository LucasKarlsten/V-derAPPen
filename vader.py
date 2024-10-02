import requests

# Klassen för våran API-Nyckel och get_väder requesten från API:et
class WeatherAPI:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def get_väder(self, stad) -> dict:
        # Funktionen get_väder hämtar datan från våran OpenWeatherAPI som sen returnerar -
        # - datan i en json dict
        url: str = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        # Status_code kontrollerar ifall api requesten gick igenom (returnerar 200)
        if response.status_code == 200:
            return response.json()
        # Felhantering ifall vi inte får en godkännd status kod från api:et
        else:
            print(f"Fel vid API-anrop: {response.status_code}")
            return None

class UserInput: 
    def get_stad() -> str: 
        # Hämtar och validerar stadens namn från användaren, detta skickas tillbaka i url:en till API
        # vi får sen tillbaka datan som vi sen printar ut till användaren
        while True:
            stad: str = input("Ange en stad: ").strip()
            if not stad:
                # Felhantering ifall användaren skiver in ett tomt stadsnamn
                print ("Stadsnamnet kan inte vara tomt")
            elif " " in stad or stad.isalpha():
                # Felhantering ifall användaren skriver in en stad med nummer
                return stad
            else:
                print("Fel: Stadsnamnet kan inte innehålla nummer eller specialtecken")

                
class WeatherApp:
    def skriv_ut_väder(data, stad) -> str :
        # Vi tar emot datan från APIet som vi sen omvandlar till våra egna variabel och sen printar ut till anv.
        temperatur: str = data['main']['temp']
        luftfuktighet: str = data['main']['humidity']
        väderförhållanden: str = data['weather'][0]['description']
        väderinfo = (
            f"\nVädret i {stad.capitalize()}:\n"
            f"Temperatur: {temperatur}°C\n"
            f"Luftfuktighet: {luftfuktighet}%\n"
            f"Väderförhållanden: {väderförhållanden}\n"
        )

        return väderinfo
    
    # http://api.openweathermap.org/data/2.5/weather?q=stockholm&appid=17f1f567d5ead14df048349b68629fb4&units=metric
