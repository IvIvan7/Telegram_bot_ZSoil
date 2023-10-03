import telebot

Zbot = telebot.TeleBot('6600856546:AAENe91UZs8biRjmAnBIQUWW7joTl35W60Y')

from telebot import types

@Zbot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nДобро пожаловать в беседу сотрудников компании ООО 'З-Сойл'"
  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(types.InlineKeyboardButton('День рождения', callback_data='option 1'))
  Zbot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=keyboard)

@Zbot.callback_query_handler(func=lambda callback: callback.data)
def birthday(message):
  import Test
  mess = Test.find_name_by_weekday('D_R_Z-Soyl.xlsx')
  Zbot.send_message(message.chat.id, mess)

Zbot.infinity_polling()
