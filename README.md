# Weather API Project

## Inspiration
This project was inspired by the need to fetch and display weather data for a given city using the OpenWeatherMap API. It's a simple, yet effective way to interact with external APIs and visualize weather information.

## What it does
- The application allows the user to input a city name.
- It fetches real-time weather data from OpenWeatherMap API.
- Displays essential weather details such as temperature, humidity, wind speed, and weather conditions.
- The data is fetched and displayed in an easy-to-read format.

## How we built it
- The project was built using **Python**.
- **Requests** library was used to send HTTP requests to the OpenWeatherMap API and fetch weather data.
- The weather data is parsed from the API response (in JSON format) and displayed to the user.
- The user inputs the name of a city, and the application provides the current weather details for that city.

### Technologies used:
- **Python** (for scripting)
- **Requests** (for API requests)
- **JSON** (for handling the API response)

## Challenges we ran into
- The biggest challenge was working with external APIs and handling the 401 (Unauthorized) error due to incorrect API keys.
- Ensuring that the API key is valid and properly integrated into the code.
- Handling edge cases such as invalid city names and API quota limits.

## Accomplishments that we're proud of
- Successfully integrated and worked with an external API.
- Learned how to handle and parse JSON data from an API.
- The application is now able to fetch and display live weather data dynamically.

## What we learned
- How to work with external APIs using Python and the `requests` library.
- Handling API responses and parsing JSON data in Python.
- Error handling in API calls, especially when dealing with invalid keys or incorrect parameters.

## What's next for Weather API Project
- Implement graphical representation of weather data, such as temperature trends over time.
- Add error handling for invalid city names and other potential issues.
- Make the application more user-friendly with a GUI using libraries like **Tkinter** or **PyQt**.
- Expand the application to include additional weather-related data like forecast, precipitation, and air quality.
