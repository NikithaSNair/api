import requests
import matplotlib.pyplot as plt

API_KEY ='fca6f0cce730843ca8a24c6960632e64'
URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        # API returns cod 200 even if city not found sometimes check
        if data.get("cod") != 200 and data.get("message"):
            print(f"Error: {data['message']}")
            return None
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def extract_weather_info(data):
    weather_info = {
        'City': data['name'],
        'Temperature (°C)': data['main']['temp'],
        'Humidity (%)': data['main']['humidity'],
        'Pressure (hPa)': data['main']['pressure'],
        'Weather': data['weather'][0]['description'].capitalize()
    }
    return weather_info

def visualize_weather(data):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [data['Temperature (°C)'], data['Humidity (%)'], data['Pressure (hPa)']]

    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f"Weather in {data['City']}")
    plt.ylabel('Value')
    plt.show()

def main():
    city = input("Enter city name: ")

    weather_data = fetch_weather_data(city)
    if weather_data:
        weather_info = extract_weather_info(weather_data)
        print("\nWeather Data:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")

        visualize_weather(weather_info)
    else:
        print("No data to display.")

if __name__ == '__main__':
    main()
