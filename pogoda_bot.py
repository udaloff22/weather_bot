import telebot


from weather import show_weather


with open('tgbot_token.txt') as f:
    tgbot_token = f.read()[:-1]
    f.close()




bot = telebot.TeleBot(tgbot_token)


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    print(message.text)
    content = show_weather(message.text)
    print(content)

    bot.send_message(message.chat.id, content)

print('Bot Started..')
bot.polling()
