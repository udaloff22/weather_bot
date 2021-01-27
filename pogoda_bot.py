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

    result = 'Temperature: {} \nMax Temperature: {} \nMin Temperature: {} \nCloud Status: {} \nDetailed Status: {}'.format(
        temper,
        temper_max,
        temper_min,
        cloud_status,
        detailed_status
    )

    return result








bot = telebot.TeleBot(tgbot_token)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    print(message.text)
    content = show_weather(message.text)
    print(content)

    bot.send_message(message.chat.id, content)


bot.polling()
