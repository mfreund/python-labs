'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''
import requests

# response = requests.get("https://codingnomads.co/")
# print(response.text)

website = requests.get("https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=439d4b804bc8187953eb36d2a8c26a02")
weather_data = website.json()
print(weather_data.get("wind"))
