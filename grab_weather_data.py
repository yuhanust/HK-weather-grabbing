# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:08:59 2024

@author: 于涵
"""
import pandas as pd
import requests
import schedule
import time
import csv

# function to get weather data from HKO API
def get_weather_data():
    url = 'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&Iang=en'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        get_days=data['weatherForecast']
        temp={}
        hum = {}
        winds = {}
        weather = {}
        for i in range(len(get_days)):
            temp[get_days[i]['forecastDate']]=get_days[i]['forecastMaxtemp']['value']
            hum[get_days[i]['forecastDate']]=get_days[i]['forecastMaxrh']['value']
            winds[get_days[i]['forecastDate']]=get_days[i]['forecastWind']
            weather[get_days[i]['forecastDate']]=get_days[i]['forecastWeather']
            
        temperature=pd.DataFrame.from_dict(temp, orient='index', columns=['temperature'])
        humidity=pd.DataFrame.from_dict(hum, orient='index', columns=['humidity'])
        wind_speed=pd.DataFrame.from_dict(winds, orient='index', columns=['wind_speed'])
        weather1=pd.DataFrame.from_dict(weather, orient='index', columns=['weather'])
        return temperature, humidity, wind_speed, weather1
    else:
        print('Error getting weather data:', response.status_code)
        return None

# function to log weather data to a CSV file
def log_weather_data():
    weather_data = get_weather_data()
    if weather_data:
        with open('hko_weather_data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time.time(), *weather_data])

#log_weather_data()
#Here we use it to tese our data, and it can work

# schedule the job to run every day
schedule.every().day.do(log_weather_data)

# run the job continuously
while True:
    schedule.run_pending()
    time.sleep(1)