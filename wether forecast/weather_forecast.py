import requests
import json

API_KEY = 'acd6313c14f05f021f0f6cf2c883244f'

def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        temperature = int(data['main']['temp'])
      
        a=temperature-273
        temperature=a
        weather_condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print('the weather report by reporter abinav is:')
        print(f'Weather forecast for {city}:')
        print(f'Temperature: {temperature} C')
        print(f'Weather Condition: {weather_condition}')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print('Error occurred while fetching weather data.')

# Prompt the user to enter a city name
city_name = input('Enter the city name: ')

# Call the function to get the weather forecast for the specified city
get_weather_forecast(city_name)

