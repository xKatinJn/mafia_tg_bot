import os
import database
from database import User
from localization import buttons_loc, texts_loc
from chatting import *
from keyboards import *

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    user_id = update.message.from_user.id

    if user_id not in User.get_all_users_ids():
        current_user = User(user_id=user_id)
        current_user.save()
    else:
        current_user = User.get(User.user_id == user_id)
    print(current_user.id, current_user.user_id, current_user.wait_for_selector)

    if text == buttons_loc['back_ru']:
        return start_main_menu(update, context, keyboard_main_ru)
    elif current_user.wait_for_selector:
        try:
            number_of_members = int(update.message.text)
            if number_of_members > 3:
                send_selector_result(update, context, number_of_members, keyboard_main_ru)
                User.update(wait_for_selector=0).where(User.user_id == current_user.user_id).execute()
            else:
                send_message(update, context, texts_loc['selector_small_num_ru'])
        except ValueError:
            send_message(update, context, texts_loc['selector_error_ru'])
    elif text == buttons_loc['about_ru']:
        return about_handler(update, context)
    elif text == buttons_loc['selector_ru']:
        User.update(wait_for_selector=1).where(User.user_id == current_user.user_id).execute()
        return send_message(update, context, texts_loc['selector_instructions_ru'], remove_keyboard)
    elif text == buttons_loc['mafia_cards_ru']:
        User.update(wait_for_card=1).where(User.user_id == current_user.user_id).execute()
        return send_message(update, context, buttons_loc['mafia_cards_ru'], keyboard_mafia_cards_ru)
    elif current_user.wait_for_card:
        if update.message.text in [buttons_loc['citizen_ru'], buttons_loc['mafia_ru'],
                                   buttons_loc['doctor_ru'], buttons_loc['sheriff_ru']]:
            User.update(wait_for_card=0).where(User.user_id == current_user.user_id).execute()
            return send_chosen_card(update, context, keyboard_main_ru)
        else:
            return send_message(update, context, texts_loc['do_not_understand_ru'])
    else:
        return send_message(update, context, texts_loc['do_not_understand_ru'])


def start() -> None:
    updater = Updater(
        token=os.getenv('token'),
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
