import telebot

TOKEN = '1256275471:AAE5rTB_mX04NLZKehHmAUC1OzRk9RMM8ZA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def mes(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()