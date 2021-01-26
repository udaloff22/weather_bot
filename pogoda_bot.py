import time
import telebot
from telebot import types



TOKEN = '1343968249:AAGyUZofhY2v8WPeBBijYT-ZK7BHD6LP-qk'

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
    'hood': 'set up a town, brah..',
}



def weather(town):
    import pyowm as owm
    mgr = owm.OWM('9b9f3ce06294c87ce7162c7a8e0903a7').weather_manager()
    place = town
    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
        temper  = w.temperature('celsius')['temp']
        temper_max = w.temperature('celsius')['temp_max']
        temper_min = w.temperature('celsius')['temp_min']
        stts = w.status
        dtld_stts = w.detailed_status

        pogoda = [
        'temper in ' + str(place) + ' = ' + str(temper),
        'temper_max in ' + str(place) + ' = ' + str(temper_max),
        'temper_min in ' + str(place) + ' = ' + str(temper_min),
        'status in ' + str(place) + ' = ' + str(stts),
        'detailed_status in ' + str(place) + ' = ' + str(dtld_stts)
        ]

        pogoda_str = str(pogoda)

        file = open('pgd.txt', 'w')
        file.write(pogoda_str)
        file.close()
    except:
        pogoda = 'wrong hood'
        file = open('pgd.txt', 'w')
        file.write(pogoda_str)
        file.close()


# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)


# handle the "/start" command



# user can chose an image (multi-stage command example)
@bot.message_handler()
def handle_text(message):
    bot.send_message(message.chat.id, "which town? ")
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        weather(txt)

        print(txt)
        time.sleep(3)
        try:
            file = open('pgd.txt', 'r')
            bot.send_message(message.chat.id, file)
            file.close()
            bot.send_message(message.chat.id, file)
        except:
            bot.send_message(message.chat.id, 'idi naxui blya, pes')



# if the user has issued the "/getImage" command, process the answer


# default handler for every other text


bot.polling()
