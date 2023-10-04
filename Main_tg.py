import telebot

Zbot = telebot.TeleBot('6600856546:AAENe91UZs8biRjmAnBIQUWW7joTl35W60Y')

from telebot import types

@Zbot.message_handler(commands=['back', 'start'], chat_types = ['supergroup'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>,\nЧем могу помочь?"
  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(types.InlineKeyboardButton('День рождения', callback_data='key 1'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard)

@Zbot.callback_query_handler(func=lambda call: True)
def birthday(function_call):
  import Test
  if function_call.message:
    print(function_call.data)
    if function_call.data == 'option 1':
      mess, name = Test.find_name_by_weekday('D_R_Z-Soyl.xlsx')
      Zbot.send_message(function_call.message.chat.id, mess)

@Zbot.message_handler(commands=['start'], chat_types = ['private'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЯ твой бот помощник. Очень рад с тобой познакомиться. Чем я могу тебе помочь?"
  keyboard2 = types.InlineKeyboardMarkup()
  keyboard2.add(types.InlineKeyboardButton('У кого сегодня день рождения?', callback_data='2'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard2)

@Zbot.message_handler(commands=['back'], chat_types = ['private'])
def backBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧем могу помочь?"
  keyboard3 = types.InlineKeyboardMarkup()
  keyboard3.add(types.InlineKeyboardButton('У кого сегодня день рождения?', callback_data='2'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard3)


@Zbot.callback_query_handler(func=lambda call: True)
def birthday(function_call2):
  import Test
  if function_call2.message:
    print(function_call2.data)
    if function_call2.data == 2:
      mess, name = Test.find_name_by_weekday('D_R_Z-Soyl.xlsx')
      print(name)
      Zbot.send_message(function_call2.message.chat.id, mess)


Zbot.infinity_polling()
