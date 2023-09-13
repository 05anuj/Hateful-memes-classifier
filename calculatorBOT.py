# # import telebot
# # import os

# # code
# from telegram.ext import Updater, CommandHandler

# # Replace 'YOUR_BOT_TOKEN' with the token provided by the BotFather
# bot_token = '6565454651:AAFunjZGPqGJ7UVcritZJwESoav8OxGpyPU'
# updater = Updater('6565454651:AAFunjZGPqGJ7UVcritZJwESoav8OxGpyPU', True)

# # Add some basic commands for your bot
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am your ML-powered bot. Send me a message!")

# def help(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="This is a help message.")

# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('help', help))

import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
