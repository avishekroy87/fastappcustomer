import requests

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        'q': city,
        'appid': 'bd5e378503939ddaee76f12ad7a97608',
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        return response.json() # Check if the request was successful

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


city_name = input("Enter the city name: ")
weather_data = get_weather(city_name)

if weather_data:
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:    print("Could not retrieve weather data.")



