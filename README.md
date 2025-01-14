
# Use API - Project

## Inspiration
The inspiration behind this project came from the need to fetch and display weather data dynamically using an API. With the rise of using APIs in modern applications, I wanted to explore how APIs work, how to fetch real-time data, and how to process and display that data effectively.

## What it does
This project allows users to:
- Input a city name.
- Fetch real-time weather information from the OpenWeatherMap API.
- Display essential weather details such as temperature, humidity, wind speed, and weather conditions.

## How we built it
- **Python** was used to build the application.
- We utilized the **Requests** library to interact with the OpenWeatherMap API and fetch weather data in JSON format.
- The data is parsed from the API response and presented to the user in a readable format.
- The program takes user input for the city name, then fetches and displays the relevant weather information.

### Technologies used:
- **Python** for the backend.
- **Requests** for making API calls.
- **JSON** to handle and parse the data from the API.

## Challenges we ran into
- Initially, we encountered the **401 Unauthorized error** due to an incorrect API key or misconfiguration. Solving this required careful verification of the API key and ensuring proper integration.
- Handling edge cases like invalid city names and managing API rate limits was another challenge that needed to be addressed.

## Accomplishments that we're proud of
- Successfully fetched and displayed real-time weather data.
- Gained hands-on experience working with APIs in Python.
- Managed to troubleshoot the 401 error, and ensure proper authentication with OpenWeatherMap's API.

## What we learned
- How to interact with an API using Python and the **requests** library.
- How to handle and parse **JSON** data received from an API.
- The importance of API key management and handling errors such as **401 Unauthorized**.

## What's next for Use API
- Enhance the user experience by adding a graphical interface with **Tkinter** or **PyQt**.
- Incorporate additional features like a 7-day forecast or displaying weather data in charts.
- Add error handling for invalid city names or other potential issues (e.g., network failures).
- Explore integrating more APIs to provide additional data, such as air quality or UV index.
