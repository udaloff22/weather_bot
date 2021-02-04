from pyowm import OWM

def show_weather(place):

    with open('pyowm_token.txt') as s:
        PYOWM_TOKEN = s.read()[:-1]
        s.close()

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

    result = 'Temperature: {} \nMax Temperature: {} \nMin Temperature: {} \nCloud Status: {} \nDetailed Status: {}'.format(
        temper,
        temper_max,
        temper_min,
        cloud_status,
        detailed_status
    )

    return result
