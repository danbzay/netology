import random

from telebot import types, TeleBot, custom_filters
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup

from englishcards.database import EnglishCardsDB
#import englishcards.database

print('Start telegram bot...')

state_storage = StateMemoryStorage()
db = EnglishCardsDB()
#token_bot = '7107066093:AAHEuNUFakBFIHYTejwMShSZkZWgcmOBv94'
bot = TeleBot(db.get_token('telegram'), state_storage=state_storage)

active_users = []
userStep = {}
buttons = []
    
class Command:
    ADD_WORD = 'Добавить слово ➕'
    DELETE_WORD = 'Удалить слово🔙'
    NEXT = 'Дальше ⏭'


class MyStates(StatesGroup):
    target_word = State()
    translate_word = State()
    another_words = State()

def get_user_step(uid):
    if uid not in active_users:
        step = active_users.append(uid)

    if uid in userStep:

        return userStep[uid]
    else:
        db.select('teleusers', 'uid', long(cid))
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


@bot.message_handler(commands=['cards', 'start'])
def create_cards(message):
    uid = message.chat.id
    if uid not in active_users:
        bot.send_message(uid, 'Здравствуйте, ' 
            + message.from_user.first_name + ', let study English...')
        db.insert('teleusers', 'uid', long(uid))
        active_users.append(uid)
        step = db.get_one(sql.SQL(
            'SELECT step FROM teleusers WHERE uid = {};').format(
                sql.Literal(uid)))
        if step == None:
            # устанавливаем дефолтные значения для нового пользователя
            step = 0
            words[uid] = db.get_all("""
                SELECT words.en, words.ru, words.example, teleusers_words.step
                FROM words, teleusers WHERE teleuser.uid = 0;""")
            db.set(sql.SQL("""
                INSERT INTO teleusers VALUES ({}, 0);
                INSERT INTO teleusers_words VALUES {};""").format(
                    sql.Literal(uid), sql.Literal(words)))
        userStep[uid] = get_user_step(uid)

    markup = types.ReplyKeyboardMarkup(row_width=2)

    target_word = 'Peace'
    translate = 'Мир'
    target_word_btn = types.KeyboardButton(target_word)
    buttons.append(target_word_btn)
    others = ['Green', 'White', 'Hello', 'Car']
    other_words_btns = [types.KeyboardButton(word) for word in others]
    buttons.extend(other_words_btns)
    random.shuffle(buttons)
    next_btn = types.KeyboardButton(Command.NEXT)
    add_word_btn = types.KeyboardButton(Command.ADD_WORD)
    delete_word_btn = types.KeyboardButton(Command.DELETE_WORD)
    buttons.extend([next_btn, add_word_btn, delete_word_btn])

    markup.add(*buttons)

    greeting = f"Выбери перевод слова:\n🇷🇺 {translate}"
    bot.send_message(message.chat.id, greeting, reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.target_word, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['target_word'] = target_word
        data['translate_word'] = translate
        data['other_words'] = others


@bot.message_handler(func=lambda message: message.text == Command.NEXT)
def next_cards(message):
    create_cards(message)


@bot.message_handler(func=lambda message: message.text == Command.DELETE_WORD)
def delete_word(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        print(data['target_word'])


@bot.message_handler(func=lambda message: message.text == Command.ADD_WORD)
def add_word(message):
    cid = message.chat.id
    userStep[cid] = 1


@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def save_new_word(message):
    pass


@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_reply(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        target_word = data['target_word']
    markup.add(*buttons)
    bot.send_message(message.chat.id, target_word, reply_markup=markup)



def run_bot():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling(skip_pending=True)
    print('finised')
