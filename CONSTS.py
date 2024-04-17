STATES = {
    "В какой музей отправимся сегодня?": [
        "Музей Политической истории",
        "Музей религии",
        "Музей денег"],

    "Выбери уровень сложности": [
            "Просто",
            "Средне",
            "Сложно"]
}

GAME_DATA = {

    "correct_answer": None,
    "museum": None,
    "difficulty": None,
    "current_state": "Select museum",
    "score": 0,
    "questions_iterator": None,
    "states_iterator": iter(STATES.items())
}
