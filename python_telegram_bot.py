import telebot
import logging
from telebot import types

bot = telebot.TeleBot("491326980:AAEAG7Q0nBiqMSb1Ln7qqdhAGw6_SZJUfMA")


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


##inline keyboard
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)
bot.send_message(415492693, "Choose one letter:", reply_markup=markup)

'''
markup = types.ForceReply(selective=False)
bot.send_message(415492693, "Send me another word:", reply_markup=markup)
'''

"""
##inline keyboard

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
bot.send_message(415492693, "Choose one letter:", reply_markup=markup)"""


@bot.message_handler(commands=['help'])
def function_name(message):
        bot.reply_to(message, "Howdy, how are you doing?")
        
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
 
