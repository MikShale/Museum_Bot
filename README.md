This is a small Telegram bot for Diploma Work of a student at Herzen University.
Firstly, bot greets you. Then, you must choose one of the museums. After that, you need to choose the difficulty level.
Next, you will have 3 questions about this museum. If you answer is correct, you will get one point for each question.
Otherwise, you will received 0 and a message with the correct answer.
At the end of the game you will see how many points you received.

Bot writed with telebot lib.

The bot implements a logger that reports when a certain function has been triggered.
Additionally, the bot supports the simultaneous operation of multiple users.

For the successful operation of the bot, it is necessary to create a file named TOKEN.py in the bot's directory. 
In this file, specify your bot token from Bot_father in the format TOKEN = "YOUR TOKEN".

The file questions.py contains questions with file names and answers. It is possible to add any number of museums, levels of difficulty, questions, or answers. The main thing is to maintain the original structure. The comma after the question enclosed in parentheses is IMPORTANT!
Example: ("What are the causes of unemployment depicted in this photo?",)
This won't work: ("What are the causes of unemployment depicted in this photo?")

In the file main.py, some lines of interaction between the bot and the user are hardcoded.
For example: f"Wrong 😞\nCorrect answer: {Users[chat_id].correct_answer}".
