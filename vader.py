import requests

class WeatherAPI:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def get_väder(self, stad):
        """Hämtar väderdata från OpenWeather API"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Fel vid API-anrop: {response.status_code}")
            return None

class UserInput:
    def get_stad():
        """Hämtar och validerar stadens namn från användaren"""
        while True:
            stad = input("Ange en stad: ")
            if not stad:
                print ("Stadsnamnet kan inte vara tomt")
            elif " " in stad or stad.isalpha():
                return stad
            else:
                print("Stadsnamnet får inte innehålla nummer eller tecken")
                
class WeatherApp:
    def skriv_ut_väder(data, stad):
        """Returnerar väderinformationen för den angivna staden som en sträng."""
        temperatur = data['main']['temp']
        luftfuktighet = data['main']['humidity']
        väderförhållanden = data['weather'][0]['description']

        väderinfo = (
            f"\nVädret i {stad.capitalize()}:\n"
            f"Temperatur: {temperatur}°C\n"
            f"Luftfuktighet: {luftfuktighet}%\n"
            f"Väderförhållanden: {väderförhållanden}\n"
        )

        return väderinfo
