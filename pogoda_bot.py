import telebot
from tokens import TGBOT_TOKEN

from weather import show_weather


bot = telebot.TeleBot(TGBOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    print(message.text)
    content = show_weather(message.text)
    print(content)

    bot.send_message(message.chat.id, content)

print('Bot Started..')
bot.polling()
