"""Список вопросов для квиза. Теоретически можно добавлять сколь угодно много"""



QUESTIONS = {
    "Музей Политической истории": {
        "Простой уровень": {
            ("При каком царе произошла земская реформа?", "photo_2024-05-15 17.34.38.jpeg"): ["при Иване Грозном", "при Михаиле Федоровиче", "при Петре Великом", "при Александре II"],
            ("Что такое земство?", "2.jpg"): ["Приказы", "Министерства", "Органы местного самоуправления", "Собрания"],
            ("Какой аналог этих органов существует в РФ сегодня?", "3.jpg"): ["Государственная Дума", "Органы местного самоуправления", "Правительство", "Государственный совет"]
        },
        "Средний уровень": {
            ("Какие причины безработицы представлены на данном фото?","photo_2024-05-15 18.28.10.jpeg"): ["Инфляция", "Структурные изменения", "Сезонность", "Изменения в обществе"],
            ("Кто является экономически активным населением?",): ["Безработные", "Учащиеся школы", "Пенсионеры", "Инвалиды"],
            ("Каковы современные государственные способы борьбы с безработицей?",): ["Открытие рынков", "Повышение пособия по безработице", "Повышение ключевой ставки", "Расширение государственного сектора"],
        },
        "Сложный уровень": {
            ("После какого события в России появились Советы?", "photo_2024-05-15 18.31.35.jpeg"): ["Свержение Временного правительства", "Революция 1905-1907 года", "Двоевластие", "Февральская революция 1917"],
            ("Какие были причины их появления?",): ["органы местного самоуправления", "выборные политические организации", "правительство", "партии"],
            ("Аналогом каких органов в РФ являются советы?",): ["Государственная Дума", "Органы местного самоуправления", "Правительство", "Государственный совет"],
        }
    },
    "Музей истории религии": {
        "Простой уровень": {
            ("Что из перечисленного является формой первобытной религии?", "PlD4VNkOo8I.jpg",): ["Христианство", "Родология", "Анимизм", "Даосизм"],
            ("Выберите мировую религию из списка",): ["Иудаизм", "Зороастризм", "Конфунианство", "Ислам"],
            ("Какие функции выполняет религия?",): ["Компенсаторную", "Рекрутирующую", "Прагматическую", "Политическую"],
        },
        "Средний уровень": {
            ("Что не относится к признакам мировых религий?", "AvKtgdi3KRo.jpg"): ["Большое число последователей", "Стремятся распространить своё учение", "эгалитаризм", "имеют национальную принадлежность"],
            ("На борьбу с каким процессом должно пойти золото церквей с точки зрения авторов плаката?",): ["Голод в Поволжье", "Революция", "Великие реформы", "Борьба с коллетивизацией"],
            ("Какому типу общества свойственны сословные привилегии?",): ["Традиционному", "Индустриальному", "Постиндустриальному"],
        },
        "Сложный уровень": {
            ("Как в годы Гражданской войны большевиками использовались храмы и церкви?", "photo_2024-05-15 18.37.34.jpeg"): ["В целях поклонения высшим силам", "Для проведения литургий", "Для проведения обрядов", "Для альтернативных целей"],
            ("Укажите основные принципы социализма",): ["индивидуальная свобода", "свобода мысли и слова", "равенство всех", "демократия"],
            ("Что из перечисленного относится к политическим режимам?",): ["Демократия", "Тоталитаризм", "Консерсатизм", "Авторитаризм"],
        }
    },
    "Музей истории денег": {
        "Простой уровень": {
            ("Что из перечисленного не является функцией денег?",): ["всеобщий эквивалент", "мера стоимости", "удовлетворение потребностей", "средства платежа"],
            ("В россии в период с 1898 по 1918 год было выпущено более десятка разной валюты. Чем обусловлено такой колличество валют?",): ["политическими процессами", "участием в войнах", "проведением реформ", "расширением рынков сбыта"],
            ("Как называется процесс обмена старых денежных средств на новые?",): ["Дефляция", "Эмиссия", "Инфляция", "Деноминация"],
        },
        "Средний уровень": {
            ("Что такое ассигнации и кредиты?", "photo_2024-05-15 18.39.20.jpeg"): ["Догловые документы", "Инвестиции", "Ценные бумаги", "Валюта"],
            ("Какие еще ценные бумаги вы знаете?",): ["Тенге", "Инвестиционный договор", "Облигация", "расписка"],
            ("В чем отличие акции от облигации?",): ["акция - это заемный документ", "у акционера есть доля в компании", "прибыль в процентах", "имеет срок обращения"],
        },
        "Сложный уровень": {
            ("Скольким рублям равнялась эта купюра?", "JYXN8dGnaNg.jpg"): ["0,25₽", "2,5₽", "25₽", "250₽"],
            ("О каком экономическом процессе свидетельствует эта банкнота?",): ["Дефляция", "Эмиссия", "Инфляция", "Деноминация"],
            ("Что стало причиной усиления выпуска бумажных денег в начале двадцатого века?",): ["политические процессы", "революция", "участие в войнах", "проведение реформ"],
        }
    }
}
