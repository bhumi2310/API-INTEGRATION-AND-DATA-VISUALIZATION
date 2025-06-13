import requests 
import matplotlib.pyplot as plt 
 
API_KEY = "your_openweathermap_api_key"  # તતતતતત  API તત 
city = "Surat" 
url = 
f"http://api.openweathermap.org/data/2.5/forecast?q={city}& appid={API_KEY}&units=metric" 
 
response = requests.get(url)
data = response.json() 
 
dates = []
temps = [] 
 
for forecast in data['list']: 
    dates.append(forecast['dt_txt']) 
    temps.append(forecast['main']['temp']) 
 
plt.figure(figsize=(10, 5))
plt.plot(dates[:10], temps[:10], marker='o') 
plt.xticks(rotation=45) 
plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.grid()
plt.show() 
