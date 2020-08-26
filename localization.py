buttons_loc = {
    'about_ru': 'О проекте',
    'back_ru': 'Назад',
    'selector_ru': 'Подобрать состав',
    'mafia_cards_ru': 'Карточки для игры в мафию',
    'citizen_ru': 'Мирный житель',
    'mafia_ru': 'Мафия',
    'doctor_ru': 'Доктор',
    'sheriff_ru': 'Шериф',
}
texts_loc = {
    'about_ru': 'Здесь должна быть информация о проекте. Скоро она здесь появится.',
    'main_menu_ru': 'Выбери с помощью кнопок, как я могу тебе помочь.',
    'do_not_understand_ru': 'Я тебя не совсем понимаю. Воспользуйся кнопками, пожалуйста.',
    'selector_instructions_ru': 'Я помогу тебе подобрать состав ролей для твоей игры, но для этого мне нужно узнать,'
                                + ' сколько вас всего. Напиши мне цифрой количество игроков в партии',
    'selector_error_ru': 'Будь внимателен, мне нужно только число игроков.',
    'selector_small_num_ru': 'Лучше играть в мафию компанией от 4ех человек. Введи число больше 3ех, пожалуйста.',
}


def get_selector_result_ru(number_of_members,
                           number_of_civil,
                           number_of_mafia,
                           number_of_sheriff,
                           number_of_doctor) -> str:
    return f"""Для игры c {number_of_members} участниками, распределение ролей будет следующим:\n
Мирных жителей: {number_of_civil}\n
Мафии: {number_of_mafia}\n
Докторов: {number_of_doctor}\n
Шерифов: {number_of_sheriff}"""
