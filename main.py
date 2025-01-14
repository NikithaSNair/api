import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint and your API key
API_KEY ='9a391d3cd10f9d5422e4e95d01c2df2d'
URL = 'https://api.openweathermap.org/data/2.5/weather'

# Function to fetch weather data
def fetch_weather_data(city):
    params = {
        'q': city,  # City name
        'appid': API_KEY,  # API key
        'units': 'metric'  # Units in Celsius
    }
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Function to extract relevant weather information
def extract_weather_info(data):
    weather_info = {
        'City': data['name'],
        'Temperature (°C)': data['main']['temp'],
        'Humidity (%)': data['main']['humidity'],
        'Pressure (hPa)': data['main']['pressure'],
        'Weather': data['weather'][0]['description']
    }
    return weather_info

# Function to visualize weather data
def visualize_weather(data):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [data['Temperature (°C)'], data['Humidity (%)'], data['Pressure (hPa)']]
    
    # Bar Chart
    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f"Weather in {data['City']}")
    plt.ylabel('Value')
    plt.show()

# Main function
def main():
    city = input("Enter city name: ")
    
    # Fetch weather data
    weather_data = fetch_weather_data(city)
    
    if weather_data:
        weather_info = extract_weather_info(weather_data)
        print("\nWeather Data:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
        
        # Visualize the weather data
        visualize_weather(weather_info)

if __name__ == '__main__':
    main()
