# V-derAPPen
Grupp 6 Lucas, Johan, Johan, Claire, Omar, Nick.

---

### 1. **Väderapp med API och användarinput**

**Beskrivning:**  
En enkel väderapplikation som hämtar väderinformation från en extern API (t.ex. OpenWeatherMap). Användaren matar in en stad, och programmet visar aktuella väderdata som temperatur, luftfuktighet och väderförhållanden.

**Objektorienterad struktur:**

- **Klasser:**
  - **WeatherApp:** Huvudklassen som samlar all logik för väderapplikationen.
  - **WeatherAPI:** Klass som hanterar anrop till den externa väder-API:n.
  - **UserInput:** Klass för att hämta och validera användarens input (t.ex. kontrollera att staden inte är tom eller innehåller olämpliga tecken).
  - **ErrorHandler:** Klass som hanterar fel, som misslyckade API-anrop eller ogiltig användarinput.

**Extern indata:**
- **API-anrop:** Till OpenWeatherMap (eller annan vädertjänst).
- **Användarinput:** Stadsnamn som skickas till API för att hämta väderdata.

**Validering av indata:**
- **Användarinput:** Stadsnamnet kontrolleras så att det inte är tomt eller innehåller ogiltiga tecken.
- **API-svar:** Validera att API-svaret är korrekt och innehåller förväntade väderdata, t.ex. temperatur och luftfuktighet.

**Felhantering:**
- Vid ogiltig stad (ingen stad hittad i API) eller ogiltigt svar från API, meddelar **ErrorHandler** användaren om felet och tillåter ny input utan att krascha programmet.

**Relevans:**  
Användarinput och API-hantering separeras i olika klasser för att göra koden mer modulär och enkel att felsöka eller utöka.

--- 

Denna struktur visar tydligt hur klasserna relaterar till varandra och hur applikationen uppfyller kraven för validering, felhantering och extern datahantering.
