from random import shuffle
from time import sleep

import telebot
from telebot import types

from TOKEN import TOKEN
from consts import *
from questions import *


# Создание объекта бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # При начале игры обнуляем все глобальные переменные
    global GAME_DATA
    GAME_DATA.update({
        "correct_answer": None,
        "museum": None,
        "difficulty": None,
        "current_state": "Select museum",
        "score": 0,
        "questions_iterator": None,
        "states_iterator": iter(STATES.items())
    })

    bot.send_message(message.chat.id, f"Добро пожаловать в этот замечательный бот!")
    sleep(1)
    choose_museum_and_difficulty(message)


def choose_museum_and_difficulty(message):
    global GAME_DATA
    try:
        text, buttons_name = next(GAME_DATA["states_iterator"])
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(*buttons_name)
        bot.send_message(message.chat.id, text, reply_markup=markup)
    except StopIteration:
        pass


def ask_question(message):
    global GAME_DATA
    try:
        current_question, answers = next(GAME_DATA["questions_iterator"])
        GAME_DATA["correct_answer"] = answers[0]
        shuffled_answers = answers.copy()
        shuffle(shuffled_answers)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(*shuffled_answers, row_width=2)
        bot.send_message(message.chat.id, current_question, reply_markup=markup)
    except StopIteration:
        end_game(message)


# Обработка ответа пользователя
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global GAME_DATA
    if GAME_DATA.get("current_state") == "Select museum":
        GAME_DATA["current_state"] = "Select difficulty"
        GAME_DATA["museum"] = message.text
        choose_museum_and_difficulty(message)

    elif GAME_DATA.get("current_state") == "Select difficulty":
        GAME_DATA["current_state"] = "Ask questions"
        GAME_DATA["difficulty"] = message.text

        GAME_DATA["questions_iterator"] = iter(QUESTIONS[GAME_DATA["museum"]][GAME_DATA['difficulty']].items())

        ask_question(message)

    elif GAME_DATA.get("current_state") == "Ask questions":
        if message.text == GAME_DATA["correct_answer"]:
            bot.send_message(message.chat.id, "Правильно! 🎉")
            GAME_DATA["score"] += 1
        else:
            bot.send_message(message.chat.id, f"Неправильно 😞\nПравильный ответ: {GAME_DATA["correct_answer"]}")
        ask_question(message)


# Функция для завершения игры
def end_game(message):
    bot.send_message(message.chat.id, f"Игра окончена! Ваш счет: {GAME_DATA['score']}")


# Запуск бота
bot.polling()
