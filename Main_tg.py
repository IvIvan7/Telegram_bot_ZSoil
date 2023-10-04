import telebot

Zbot = telebot.TeleBot('6600856546:AAENe91UZs8biRjmAnBIQUWW7joTl35W60Y')

from telebot import types

@Zbot.message_handler(commands=['back', 'start'], chat_types = ['supergroup'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>,\nЧем могу помочь?"
  keyboard1 = types.InlineKeyboardMarkup()
  keyboard1.add(types.InlineKeyboardButton('День рождения', callback_data='birthday_grup'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard1)

@Zbot.callback_query_handler(func=lambda call: True)
def birthday(function_call):
  import Test
  mess, name = Test.find_name_by_weekday('D_R_Z-Soyl.xlsx')
  if function_call.message:
    if function_call.data == 'birthday_grup':
      Zbot.send_message(function_call.message.chat.id, mess)
    elif function_call.data == 'birthday':
      Zbot.send_message(function_call.message.chat.id, name)



@Zbot.message_handler(commands=['start'], chat_types = ['private'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЯ твой бот помощник. Очень рад с тобой познакомиться. Чем я могу тебе помочь?"
  keyboard2 = types.InlineKeyboardMarkup()
  keyboard2.add(types.InlineKeyboardButton('У кого сегодня день рождения?', callback_data='birthday'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard2)

@Zbot.message_handler(commands=['back'], chat_types = ['private'])
def backBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nЧем могу помочь?"
  keyboard3 = types.InlineKeyboardMarkup()
  keyboard3.add(types.InlineKeyboardButton('У кого сегодня день рождения?', callback_data='birthday'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard3)






Zbot.infinity_polling()
