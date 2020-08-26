from localization import buttons_loc, texts_loc, get_selector_result_ru
from helper import RoleSelector

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext


def send_message(update: Update, context: CallbackContext, text: str, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )


def send_photo(update: Update, context: CallbackContext,
               photo_dir: str, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_photo(
        photo=open(photo_dir, 'rb'),
        reply_markup=reply_markup
    )


def about_handler(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=texts_loc['about_ru'],
        reply_markup=reply_markup,
    )


def start_main_menu(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup = None) -> None:
    update.message.reply_text(
        text=texts_loc['main_menu_ru'],
        reply_markup=reply_markup
    )


def send_selector_result(update: Update, context: CallbackContext,
                         number_of_members: int, reply_markup: ReplyKeyboardMarkup = None) -> None:
    result = RoleSelector(number_of_members).to_dict()
    text = get_selector_result_ru(result['number_of_members'],
                                  result['number_of_civil'],
                                  result['number_of_mafia'],
                                  result['number_of_sheriff'],
                                  result['number_of_doctor'])
    update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )


def send_chosen_card(update: Update, context: CallbackContext, reply_markup: ReplyKeyboardMarkup):
    chosen_card = update.message.text
    if chosen_card == 'Мирный житель':
        return send_photo(update, context, 'photos/civil.jpg', reply_markup)
    elif chosen_card == 'Мафия':
        return send_photo(update, context, 'photos/mafia.jpg', reply_markup)
    elif chosen_card == 'Доктор':
        return send_photo(update, context, 'photos/doctor.jpg', reply_markup)
    elif chosen_card == 'Шериф':
        return send_photo(update, context, 'photos/sheriff.jpg', reply_markup)
