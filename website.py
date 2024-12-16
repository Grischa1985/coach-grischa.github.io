import requests
import json

# URL deiner Google Apps Script Web-App
url = "https://script.google.com/macros/s/AKfycbyW8mWWdylDD-G3woVr8CocK3ejdaFb6ISt3qRQPOtnj-RdqYceBu-xbQyjwM9mlDwR/exec"

# Termin-Daten
data = {
    "name": "Grischa",
    "email": "grischa@example.com",
    "startTime": "2024-10-10T10:00:00",
    "endTime": "2024-10-10T10:30:00"
}

# Anfrage senden
response = requests.post(url, json=data)

# Antwort anzeigen
if response.status_code == 200:
    print("Antwort von der API:", response.json())
else:
    print("Fehler:", response.text)

