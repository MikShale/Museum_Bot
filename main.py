from random import shuffle

import telebot
from telebot import types

from TOKEN import TOKEN
from questions import *
from logger import error_handler

bot = telebot.TeleBot(TOKEN)


class GameData:
    def __init__(self, last_message_date):
        self.last_message_date = last_message_date
        self.museum = None
        self.difficulty = None
        self.question_iterator = None
        self.correct_answer = None
        self.score = 0
        self.answers = None

    def display_variables(self):
        print(self.__dict__)


Users = {}


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Добро пожаловать в этот замечательный бот!")
    Users[chat_id] = GameData(message.date)
    choose_museum(chat_id)


@error_handler
def choose_museum(chat_id):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*QUESTIONS.keys())
    msg = bot.send_message(chat_id, "В какой музей отправимся сегодня?", reply_markup=markup)
    bot.register_next_step_handler(msg, answer_museum)


@error_handler
def answer_museum(message):
    chat_id = message.chat.id
    if message.text in QUESTIONS.keys():
        Users[chat_id].museum = message.text
        choose_difficulty(chat_id)
    else:
        bot.send_message(chat_id, f"Нет такого Музея!")
        choose_museum(chat_id)


@error_handler
def choose_difficulty(chat_id):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(*QUESTIONS[Users[chat_id].museum].keys())
    msg = bot.send_message(chat_id, "Выберете уровень сложности:", reply_markup=markup)
    bot.register_next_step_handler(msg, answer_difficulty)


@error_handler
def answer_difficulty(message):
    chat_id = message.chat.id
    if message.text in QUESTIONS[Users[chat_id].museum].keys():
        Users[chat_id].difficulty = message.text
        Users[chat_id].question_iterator = iter(
            QUESTIONS[Users[chat_id].museum][Users[chat_id].difficulty].items())
        ask_question(chat_id)

    else:
        bot.send_message(chat_id, f"Нет такого уровня сложности")
        choose_difficulty(chat_id)


@error_handler
def ask_question(chat_id):
    try:
        question, answers = next(Users[chat_id].question_iterator)
        Users[chat_id].answers = answers
        Users[chat_id].correct_answer = answers[0]
        shuffled_answers = answers.copy()
        shuffle(shuffled_answers)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(*shuffled_answers, row_width=2)
        msg = bot.send_message(chat_id, question, reply_markup=markup)
        bot.register_next_step_handler(msg, answer_question)
    except StopIteration:
        end_game(chat_id)


@error_handler
def answer_question(message):
    chat_id = message.chat.id
    if message.text == Users[chat_id].correct_answer:
        bot.send_message(chat_id, "Правильно! 🎉")
        Users[chat_id].score += 1
    else:
        bot.send_message(chat_id,
                         f"Неправильно 😞\nПравильный ответ: {Users[chat_id].correct_answer}")
    ask_question(chat_id)


@error_handler
def end_game(chat_id):
    bot.send_message(chat_id, f"Игра окончена! Ваш счет: {Users[chat_id].score}")
    print(Users[chat_id].display_variables)
    Users.pop(chat_id)
    print(Users)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling(none_stop=True)
