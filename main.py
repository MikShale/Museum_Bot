from random import shuffle
from time import sleep

import telebot
from telebot import types

from questions import questions

# Токен вашего бота
TOKEN = 'TOKEN'

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

# Словарь с вопросами и ответами

# Глобальные переменные для хранения текущего вопроса и правильного ответа
current_question = None
correct_answer = None
answers = None
score = 0
question_iterator = iter(questions.items())


# Функция для начала игры
# TODO: Внутри функции сделать сообщение с приветствием, и цикл вопросов определяющий какой набор вопросов будет

@bot.message_handler(commands=['start'])
def start(message):
    global current_question, correct_answer, score, question_iterator, answers
    current_question = None
    correct_answer = None
    answers = None
    score = 0
    question_iterator = iter(questions.items())
    bot.send_message(message.chat.id, f"Добро пожаловать в этот замечательный бот! Пройдемся по вопросам.")
    sleep(3)
    ask_question(message)


# Функция для задания вопроса
def ask_question(message):
    global current_question, correct_answer, question_iterator, answers
    try:
        current_question, answers = next(question_iterator)
        correct_answer = answers[0]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        shuffled_answers = answers.copy()
        shuffle(shuffled_answers)
        markup.add(*shuffled_answers)
        bot.send_message(message.chat.id, current_question, reply_markup=markup)
    except StopIteration:
        end_game(message)


# Обработка ответа пользователя
@bot.message_handler(func=lambda message: True)
def check_answer(message):
    global current_question, correct_answer, score
    if current_question:
        if message.text == correct_answer:
            bot.send_message(message.chat.id, "Правильно! 🎉")
            score += 1
        else:
            bot.send_message(message.chat.id, f"Неправильно 😞\nПравильный ответ: {correct_answer}")
        ask_question(message)


# Функция для завершения игры
def end_game(message):
    bot.send_message(message.chat.id, f"Игра окончена! Ваш счет: {score}")


# Запуск бота
bot.polling()
