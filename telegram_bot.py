# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
from vk_functions import *

verified_users = [677594685, 1388614078]
access_denied_message = 'Я работаю только для своих. Для получения доступа напишите vk.com/fedya_nelubin\nВаш ID: {id}'

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater('1717505411:AAE3OCVeoifIq83By3Hbl7mOciXbndxWp9w', use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("possible", possible))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('requests', requests)],
        states={
            1: [MessageHandler(Filters.text, get_yesorno)],
            2: [MessageHandler(Filters.text, get_howmuch)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler(text_handler)
    updater.start_polling(timeout=0)
    updater.idle()


def start(update, context):
    reply_keyboard = [['/help'], ['/requests'], ['/possible']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Привет! Я создан для управления функциями Python скрипта!\n/help - посмотреть мой функционал.",
        reply_markup=markup)


def help(update, context):
    reply_keyboard = [['/help'], ['/requests'], ['/possible']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        "Бот создан для управления функциями Python скрипта.\nКоманды:\n/help - информация о боте.\n/requests - "
        "посмотреть заявки в друзья.\n/possible - посмотреть возможных друзей.", reply_markup=markup)


def requests(update, context):
    if update.message.from_user.id in verified_users:
        data = get_friendlist()
        reply_keyboard = [['Да', 'Нет']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            "У вас {count} входящих заявок, хотите их автопринять?\nОтветы: 'да' или 'нет'.".format(count=data['count']), reply_markup=markup)
        return 1
    else:
        update.message.reply_text(
            access_denied_message.format(id=update.message.from_user.id))


def possible(update, context):
    if update.message.from_user.id in verified_users:
        data = get_suggestionslist()
        update.message.reply_text(
            'В данный момент имеется {count} рекомендаций.'.format(count=data['count']))
    else:
        update.message.reply_text(
            access_denied_message.format(id=update.message.from_user.id))


def get_yesorno(update, context):
    answer = update.message.text.lower()
    if answer == 'да':
        update.message.reply_text(
            'Сколько должно быть общих друзей с теми, кого мы примем?')
        return 2
    if answer == 'нет':
        update.message.reply_text(
            'Возращаемся из сценария.')
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Необходимо ответить "да" или "нет".')
        return 1

def get_howmuch(update, context):
    answer = update.message.text.lower()
    update.message.reply_text(
        'Принемаем тех, с кем у нас {count} общих друзей'.format(count=answer))
    return ConversationHandler.END

def stop(update, context):
    update.message.reply_text(
        'Возращаемся из сценария.')
    return ConversationHandler.END

if __name__ == '__main__':
    main()