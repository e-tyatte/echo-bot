import telebot

token = 'Вставить токен'

bot = telebot.TeleBot(token)

user_name = "Елена"

@bot.message_handler(content_types=["text"])
def echo(message):
    if user_name in message.text:
        bot.send_message(message.chat.id, 'Ба! Знакомые всё лица!')
    else:
        bot.send_message(message.chat.id, message.text)



bot.polling(none_stop=True)