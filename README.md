1.WEATHER APP

import requests

# API endpoint and parameters
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "erattupetta",  # Location (you can change this to any city)
    "appid": "your_api_key",  # Replace with your OpenWeather API key
    "units": "metric"  # For temperature in Celsius (use 'imperial' for Fahrenheit)
}

# Make the API request
response = requests.get(url, params=params)
data = response.json()

# Extract data
city = data["name"]
weather = data["weather"][0]["description"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

# Display the weather information
print(f"Weather in {city}: {weather}")
print(f"Temperature: {temperature}°C")
print(f"Feels Like: {feels_like}°C")

# Weather App

A simple weather app that fetches the current weather data for a given city using the OpenWeatherMap API. This app displays information like temperature, weather description, and the "feels like" temperature.

## Features

- Fetches current weather data for any city.
- Displays weather description (e.g., sunny, cloudy).
- Displays current temperature and "feels like" temperature.
- Easy to use and understand.

## Requirements

- Python 3.x
- `requests` library (for making HTTP requests)

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/your-username/weather-app.git

Navigate to the project directory:
cd weather-app

Install the required libraries:
pip install -r requirements.txt
Obtain an API key from OpenWeatherMap.

Replace the placeholder API key in the code with your own.

Run the script:
python weather.py
Enter the name of the city when prompted to get the weather information.

Example output:

Weather in Erattupetta: scattered clouds
Temperature: 34°C
Feels Like: 32°C
API Documentation
This app uses the OpenWeatherMap API. You can find more details about the API and its endpoints here.

Contributing
Feel free to fork this project and submit pull requests. Contributions are welcome!

License
This project is open-source and available under the MIT License.



### Instructions:
1. Create a new repository on GitHub.
2. Add the files: `weather.py`, `requirements.txt`, and `README.md`.
3. Replace `"your_api_key"` in `weather.py` with your actual OpenWeatherMap API key.
4. Commit and push your changes to GitHub.

2.IMAGE RESIZER

A simple Python script that resizes images using the Pillow library.

Requirements:
Python 3.x
Pillow library

Installation:
Clone the repository:git clone https://github.com/your-username/image-resizer.git
Install Pillow:pip install Pillow

Run the script:python resize_image.py

Enter the required information when prompted:
Input image file name (with extension)
Output image file name (with extension)
New width and height

License:
MIT License

