from pyowm import OWM


with open('token.txt') as f:
    PYOWM_TOKEN = f.read()
    f.close()


owm = OWM7\



def show_weather(place):


    w = observation.weather





    temper  = w.temperature('celsius')['temp']
    temper_max = w.temperature('celsius')['temp_max']
    temper_min = w.temperature('celsius')['temp_min']

    cloud_status = w.status
    detailed_status = w.detailed_status

    return temper, temper_max, temper_min, cloud_status, detailed_status

print(show_weather(input()))
