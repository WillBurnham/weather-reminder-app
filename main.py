import pyowm
import schedule
import time
from city import City


# ------- The desktop version of my weather application, without SMTP functionality -------------


#cities to be monitored
dal = City('Dallas')
hou = City('Houston')
aus = City('Austin')

city_list = [dal, hou, aus]

#send email when find_bad_weather = true
def send():
    message = "It's going to rain tomorrow in "
    cities = []
    for city in city_list:
        if city.find_bad_weather() == True:
            cities.append(city.name)
        else:
            print("Weather is fine tomorrow in " + city.name + ".")
    message += str(cities)
    message += ". Give Jackson his medicine if you will be here tomorrow."
    print(message)


if __name__ == "__main__":
    send()



