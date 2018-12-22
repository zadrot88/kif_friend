from telegram import  ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import constants, texts, base_work
import logging
import random
mail = cit = lol = lol1 = False
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=constants.token)

dispatcher = updater.dispatcher


def start(bot, update):
    message = update.message
    base_work.user_init(message.chat.id, message.chat.username, message.chat.first_name)
    bottons = [['Одесса', 'Днепр'], ['Киев', 'Винница'],['Харьков', 'Николаев']]
    if message.chat.id in constants.admins:
        bottons.append(['Рассылка', 'Все пользователи'])
    keyboard = ReplyKeyboardMarkup(bottons)
    bot.send_message(message.chat.id, texts.hello_text, reply_markup=keyboard)

def answer(bot, update):
    global mail, city, cit, rayon,lol, tovari, lol1, tovar
    message = update.message
    if (message.chat.id in constants.admins) and message.text == 'Рассылка':
        mail = True
        bot.send_message(message.chat.id, 'Напишите сообщение!')
    elif mail == True:
        mail = False
        text = base_work.all_id()
        bot.send_message(message.chat.id, 'В течении 3 секунд, отправиться всем пользователям!')
        for i in text:
            try:
                bot.forward_message(i, message.chat.id, disable_notification=True, message_id=message.message_id)
            except:
                pass
        bot.send_message(message.chat.id, 'Все')
    elif (message.chat.id in constants.admins) and message.text == 'Все пользователи':
        text = base_work.all_about_user()
        for i in text:
            bot.send_message(message.chat.id, texts.user_text %(i[0], i[1],i[2]))
    elif message.text == 'Одесса':
        city = message.text
        bottons = [['Фонтан', 'Таирово'], ['Центр']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Днепр':
        city = message.text
        bottons = [['Караван', 'Калиновая'], ['Центр', 'Гагарина']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Киев':
        city = message.text
        bottons = [['Лукьяновка', 'КПИ'], ['Троещина', 'Дружба Народов']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Харьков':
        city = message.text
        bottons = [['ХГ', 'ХТЗ'], ['Салтовка', 'Героев Труда']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Николаев':
        city = message.text
        bottons = [['Заводской', 'Ингульский']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Винница':
        city = message.text
        bottons = [['Вишенка', 'Центр'], ['Замостье']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Караван':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Амф'], ['Гашиш']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Калиновая':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Марка'], ['Амф']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Центр' and city == 'Днепр':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Марка'], ['Амф']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Гагарина':
        cit = True
        rayon = message.text
        bottons = [['Гашиш', 'Кокаин'], ['Экстази', 'Шишки']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'ХГ':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Амф'], ['Гашиш']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'ХТЗ':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Марка'], ['Амф']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Салтовка':
        cit = True
        rayon = message.text
        bottons = [['Кристалы MDMA', 'Кокаин'], ['Шишки', 'Экстази']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Героев Труда':
        cit = True
        rayon = message.text
        bottons = [['Гашиш', 'Кокаин'], ['Экстази', 'Шишки']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Героев Труда':
        cit = True
        rayon = message.text
        bottons = [['Гашиш', 'Кокаин'], ['Экстази', 'Шишки']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'КПИ':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Марка'], ['Амф']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Лукьяновка':
        cit = True
        rayon = message.text
        bottons = [['Гашиш', 'Кокаин'], ['Экстази', 'Шишки']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Троещина':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Амф'], ['Гашиш']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Дружба Народов':
        cit = True
        rayon = message.text
        bottons = [['Кристалы MDMA', 'Кокаин'], ['Шишки','Экстази']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Вишенка':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Шишки'], ['Экстази','Кристалы MDMA']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Центр' and city == 'Винница':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Шишки'], ['Экстази','Кристалы MDMA']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Замостье':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Гашиш'], ['Кокаин']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Заводской':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Гашиш'], ['Кокаин']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Ингульский':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Шишки'], ['Экстази','Кристалы MDMA']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Фонтан':
        cit = True
        rayon = message.text
        bottons = [['Шишки', 'Амф'], ['Гашиш']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Таирово':
        cit = True
        rayon = message.text
        bottons = [['Амф', 'Гашиш'], ['Кокаин']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif message.text == 'Центр' and city == 'Одесса':
        cit = True
        rayon = message.text
        bottons = [['Гашиш', 'Кокаин'], ['Экстази','Шишки']]
        bottons.append(['Назад'])
        keyboard = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, texts.city_text, reply_markup=keyboard)
    elif cit == True:
        cit = False
        try:
            ans = base_work.select_one(message.text)
            if ans == 'NO':
                message.text = 'Назад'
                bot.send_message(message.chat.id, 'Что-то пошло не так...')
                city = tovari = rayon = tovar = ''
                mail = cit = lol = lol1 = False
                answer(bot, update)
            else:
                bottons = []
                qq = []
                tovar = message.text
                for i in range(1, len(ans)-1):
                    qq.append(ans[i])
                bottons.append(qq)
                bottons.append(['Назад'])
                keyboard = ReplyKeyboardMarkup(bottons)
                bot.send_message(message.chat.id, texts.choose %(city, rayon), reply_markup=keyboard)
                lol = True
        except:
            message.text = 'Назад'
            bot.send_message(message.chat.id, 'Что-то пошло не так...')
            city = tovari = rayon =tovar= ''
            mail = cit = lol = lol1 = False
            answer(bot, update)

    elif lol == True:
        lol = False
        if message.text == 'Назад':
            message.text = 'Назад'
            bot.send_message(message.chat.id, 'Назад')
            city = tovari = rayon =tovar= ''
            mail = cit = lol = lol1 = False
            answer(bot, update)
        else:
            tovari = message.text
            bottons = [['Bitcoin'], ['EasyPay'], ['Сим Карта'], ['Назад']]
            keyboard = ReplyKeyboardMarkup(bottons)
            lol1 = True
            bot.send_message(message.chat.id, texts.metho %(tovar, city,tovari ,rayon), reply_markup=keyboard)

    elif lol1 == True:
        lol1 = False
        if message.text == 'Bitcoin':
            bot.send_message(message.chat.id, '13ThtQ5ZngJxgthcTfVibAEVbd5MrWzqfD')
            bottons = [['Проверить оплату']]
            keyboard = ReplyKeyboardMarkup(bottons)
            bot.send_message(message.chat.id,
                             texts.tov % (tovar, city, rayon, str(tovari), random.randint(1, 100000)),reply_markup=keyboard)
            try:
                bot.send_message(constants.admins[0], texts.tov % (tovar, city, rayon, tovari, random.randint(1, 100000)))
                bot.send_message(constants.admins[0], str(message.chat.username))
            except:
                pass
        elif message.text == 'EasyPay':
            bot.send_message(message.chat.id, '15171577')
            bottons = [['Проверить оплату']]
            keyboard = ReplyKeyboardMarkup(bottons)
            bot.send_message(message.chat.id,
                             texts.tov % (tovar, city, rayon, tovari, random.randint(1, 100000)), reply_markup=keyboard)
            try:
                bot.send_message(constants.admins[0], texts.tov % (tovar, city, rayon, str(tovari), random.randint(1, 100000)))
                bot.send_message(constants.admins[0], str(message.chat.username))
            except:
                pass
        elif message.text == 'Сим Карта':
            bot.send_message(message.chat.id, '+380688479975')
            bottons = [['Проверить оплату']]
            keyboard = ReplyKeyboardMarkup(bottons)
            bot.send_message(message.chat.id, texts.tov %(tovar, city, rayon, str(tovari), random.randint(1, 100000)), reply_markup=keyboard)
            try:
                bot.send_message(constants.admins[0], texts.tov % (tovar, city, rayon, tovari, random.randint(1, 100000)))
                bot.send_message(constants.admins[0], str(message.chat.username))
            except:
                pass
        else:
            message.text = 'Назад'
            bot.send_message(message.chat.id, 'Назад')
            city = tovari = rayon =tovar =''
            mail = cit = lol = lol1 = False
            answer(bot, update)

    elif message.text == 'Назад' or message.text == 'Отмена':
        message = update.message
        bottons = [['Одесса', 'Днепр'], ['Киев', 'Винница'], ['Харьков', 'Николаев']]
        if message.chat.id in constants.admins:
            bottons.append(['Рассылка', 'Все пользователи'])
        keyboard = ReplyKeyboardMarkup(bottons)
        city = tovari = rayon = ''
        mail = cit = lol = lol1 = False
        bot.send_message(message.chat.id, texts.hello_text, reply_markup=keyboard)
    elif message.text == 'Проверить оплату':
        bot.send_message(message.text, '''К сожалению не хватает денег для оплаты товара.
Оплатите их и попробуйте еще раз''')
    else:
        message.text = 'Назад'
        bot.send_message(message.chat.id, 'Что-то пошло не так...')
        city = tovari = rayon = tovar =''
        mail = cit = lol = lol1 = False
        answer(bot, update)

        





start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, answer)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
updater.start_polling(clean=True, timeout=5 )
