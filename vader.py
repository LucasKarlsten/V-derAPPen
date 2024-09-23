import requests

# Be användaren skriva in en stad
stad = input("Ange en stad: ")

# Din API-nyckel (se till att du använder din egen nyckel här)
api_key = "17f1f567d5ead14df048349b68629fb4"

# Skapa URL med användarens inmatade stad
url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={api_key}&units=metric"

# Gör en förfrågan till API:et
response = requests.get(url)

# Kontrollera om anropet var framgångsrikt (statuskod 200)
if response.status_code == 200:
    data = response.json()
    
    # Hämta specifika väderdata
    temperatur = data['main']['temp']
    luftfuktighet = data['main']['humidity']
    vederforhallanden = data['weather'][0]['description']
    
    # Skriv ut väderinformationen
    print(f"Vädret i {stad.capitalize()}:")
    print(f"Temperatur: {temperatur}°C")
    print(f"Luftfuktighet: {luftfuktighet}%")
    print(f"Väderförhållanden: {vederforhallanden}")
else:
    print("Fel:", response.status_code)
