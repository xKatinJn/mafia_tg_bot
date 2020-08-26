from localization import buttons_loc

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


remove_keyboard = ReplyKeyboardRemove(
    remove_keyboard=True
)

keyboard_back_ru = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=buttons_loc['back_ru'])]],
    resize_keyboard=True
)

keyboard_main_ru = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=buttons_loc['selector_ru']),
                   KeyboardButton(text=buttons_loc['about_ru'])],
                  [KeyboardButton(text=buttons_loc['mafia_cards_ru'])]],
        resize_keyboard=True
)

keyboard_mafia_cards_ru = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=buttons_loc['citizen_ru']),
               KeyboardButton(text=buttons_loc['mafia_ru'])],
               [KeyboardButton(text=buttons_loc['doctor_ru']),
                KeyboardButton(text=buttons_loc['sheriff_ru'])]],
    resize_keyboard=True
)
