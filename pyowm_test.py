from pyowm import OWM


with open('pyowm_token.txt') as f:
    PYOWM_TOKEN = f.read()[:-1]
    f.close()


def show_weather(place):


    owm = OWM(PYOWM_TOKEN)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(place)

    except:
        return 'Wrong Hood, brah..'

    w = observation.weather


    temper  = w.temperature('celsius')['temp']
    temper_max = w.temperature('celsius')['temp_max']
    temper_min = w.temperature('celsius')['temp_min']

    cloud_status = w.status
    detailed_status = w.detailed_status

    return temper, temper_max, temper_min, cloud_status, detailed_status

print(show_weather(input()))
