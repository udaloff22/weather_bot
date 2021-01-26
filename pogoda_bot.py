import telebot
from pyowm import OWM


with open('tgbot_token.txt') as f:
    tgbot_token = f.read()[:-1]
    f.close()



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

    return temper, temper_max, temper_min, cloud_status, detailed_status








bot = telebot.TeleBot(tgbot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, show_weather(message))


bot.polling()
