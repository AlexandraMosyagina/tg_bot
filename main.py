import telebot
from telebot import types

TOKEN = '6041548049:AAEvExz7ykJOTwWF2crh0oaDfGe7r8j1lFU'

bot = telebot.TeleBot(TOKEN)

keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)

btn_info = types.KeyboardButton("About bot")
btn_cancel = types.KeyboardButton("Hide")
btn_test = types.KeyboardButton("Test keyboard")

keyboard_start.add(btn_info, btn_test)
keyboard_cancel.row(btn_cancel)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.from_user.id, f'Hello, {message.from_user.username}')
    bot.send_message(message.from_user.id, 'Please, choose an option!', reply_markup=keyboard_start)


@bot.message_handler(commands=['user'])
def user_info(message):
    bot.send_message(message.from_user.id, f'Hello, {message.from_user.username}\n Your ID: {message.from_user.id}')


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == "About bot":
        bot_info(message)
    if message.text == 'Test keyboard':
        test_keyboard(message)


def bot_info(message):
    bot.send_message(message.from_user.id, 'This bot do nothing!')


def test_keyboard(message):
    keyboard = types.InlineKeyboardButton('Lol', callback_data='message_1')
    reply_markup = types.InlineKeyboardMarkup()
    reply_markup.add(keyboard)
    bot.send_message(message.from_user.id, "Push the button!", reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: 'message_' in call.data)
def callback_func(call):
    bot.send_message(call.message.chat.id, 'Shit, here we go again...')


if __name__ == '__main__':
    print('Bot is running...')
    bot.polling()
    print('Stopping your bot...')
