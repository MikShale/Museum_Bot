""" Museum Bot """

from random import shuffle
from os.path import exists, join

from telebot import types, TeleBot

from TOKEN import TOKEN
from questions import QUESTIONS
import logger

bot = TeleBot(TOKEN)


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


logger.logger.info("Bot started")

Users = {}


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать в этот замечательный бот!")
    Users[chat_id] = GameData(message.date)
    choose_museum(chat_id)


@logger.error_handler
def choose_museum(chat_id):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for button in list(QUESTIONS.keys()):
        markup.add(button)

    msg = bot.send_message(chat_id, "В какой музей отправимся сегодня?", reply_markup=markup)
    bot.register_next_step_handler(msg, answer_museum)


@logger.error_handler
def answer_museum(message):
    chat_id = message.chat.id
    if message.text in QUESTIONS.keys():
        Users[chat_id].museum = message.text
        choose_difficulty(chat_id)
    else:
        bot.send_message(chat_id, "Нет такого Музея!")
        choose_museum(chat_id)


@logger.error_handler
def choose_difficulty(chat_id):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    for button in list(QUESTIONS[Users[chat_id].museum].keys()):
        markup.add(button)

    msg = bot.send_message(chat_id, "Выберете уровень сложности:", reply_markup=markup)
    bot.register_next_step_handler(msg, answer_difficulty)


@logger.error_handler
def answer_difficulty(message):
    chat_id = message.chat.id
    if message.text in QUESTIONS[Users[chat_id].museum].keys():
        Users[chat_id].difficulty = message.text
        Users[chat_id].question_iterator = iter(
            QUESTIONS[Users[chat_id].museum][Users[chat_id].difficulty].items())
        ask_question(chat_id)

    else:
        bot.send_message(chat_id, "Нет такого уровня сложности")
        choose_difficulty(chat_id)


@logger.error_handler
def ask_question(chat_id):
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        # в question лежит список с текстом и фоткой, если фотка есть
        question, answers = next(Users[chat_id].question_iterator)
        Users[chat_id].answers = answers
        Users[chat_id].correct_answer = answers[0]
        shuffled_answers = answers.copy()
        shuffle(shuffled_answers)

        for button in list(shuffled_answers):
            markup.add(button)

        if len(question) == 2:
            path_to_photo = join("photos", question[1])

            if exists(path_to_photo):
                with open(path_to_photo, "rb") as photo_file:
                    msg = bot.send_photo(chat_id, photo_file, caption = question[0], reply_markup=markup)

            else:
                logger.logger.error("Photo not found")

        else:
            msg = bot.send_message(chat_id, question[1], reply_markup=markup)

        bot.register_next_step_handler(msg, answer_question)
    except StopIteration:
        end_game(chat_id)


@logger.error_handler
def answer_question(message):
    chat_id = message.chat.id
    if message.text == Users[chat_id].correct_answer:
        bot.send_message(chat_id, "Правильно! 🎉")
        Users[chat_id].score += 1
    else:
        bot.send_message(chat_id,
                         f"Неправильно 😞\nПравильный ответ: {Users[chat_id].correct_answer}")
    ask_question(chat_id)


@logger.error_handler
def end_game(chat_id):
    bot.send_message(chat_id, f"Игра окончена! Ваш счет: {Users[chat_id].score}")

    Users.pop(chat_id)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == "__main__":
    bot.polling(none_stop=True)
