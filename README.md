# Use Python to capture weather data from the Hong Kong Observatory

This Python script can scrape weather data from the Hong Kong Observatory's API and log the data into a CSV file. 
You can use the library to run scripts at regular intervals so that weather data is automatically recorded.

Operating environment:Python 3.x, requests library, pandas library, schedule library

Running steps:
1.Install the required Python libraries:pip install requests pandas schedule
2.Download the script file. get_hko_weather_data.py
3.Run the script: python get_hko_weather_data.py

The script fetches 9-days weather data from the Hong Kong Observatory's API, which includes temperature,humidity, wind speed, and weather conditions. 
And then it logs the data into a file: hko_weather_data.csv
