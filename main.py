import asyncio
import logging
import random
import config

from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = [
    [KeyboardButton(text="Купити білет", )],
    [KeyboardButton(text="Афіша кіно на сьогодні")],
    [KeyboardButton(text="Поповнити карту")],
    [KeyboardButton(text="Попкорн та його вартість")],
    [KeyboardButton(text="Адреси наших кінотеатрів")],
    [KeyboardButton(text="Розробники цього бота")],
    [KeyboardButton(text="Баланс карти")],
    [KeyboardButton(text="Купити попкорн")],
    [KeyboardButton(text="Напої та їх вартість")],
    [KeyboardButton(text="Купити напій")],
    [KeyboardButton(text="Підтримати розробників бота")]
]
keyboard = ReplyKeyboardMarkup(keyboard=kb)


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6942397056:AAGh4AOjlkAqqbfTtILRrDzKFBDaV_TONto")
dp = Dispatcher()


@dp.message(F.text == "Поповнити карту")
async def cmd_answer(message: types.Message):
    buttons2 = [
        [
            InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
        ],
        [
            InlineKeyboardButton(text="Поповнити на 250 грн", callback_data="nuц_decr")
        ],
        [
            InlineKeyboardButton(text="Поповнити на 100 грн", callback_data="nuу_decr")
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

    await message.answer(
        "На скільки ви хочете поповнити карту?",
        reply_markup=keyboard)


@dp.callback_query(F.data == "nuй_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", "r")
    number = int(file.read())
    file.close()

    number += 500

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 500 грн, ваш баланс тепер складає {number}")


@dp.callback_query(F.data == "nuц_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    number += 250

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 250 грн, ваш баланс тепер складає {number}")


@dp.callback_query(F.data == "nuу_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    number += 100

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 100 грн, ваш баланс тепер складає {number}")


@dp.message(Command("start"))
async def send_random_value(message: types.Message):
    with open("result.txt", "a") as file:
        file.write(f"_______________________________\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"ChatID: {message.chat.id}\n")
        file.write(f"Name: {message.chat.first_name}\n")
        file.write(f"Last name: {message.chat.last_name}\n")
        file.write(f"Full name: {message.chat.full_name}\n")
    await message.answer("Привіт, я твій бот для кіно. Обери функцію яку ти хочеш", reply_markup=keyboard)


@dp.message(Command("start"))
async def cmd_answer(message: types.Message):
    await message.answer("Привіт, я твій бот для кіно. Обери функцію яку ти хочеш", reply_markup=keyboard)


@dp.message(Command("help"))
async def cmd_answer(message: types.Message):
    await message.answer("Якщо вам щось незрозуміло або хочете щось уточнити, то не соромтесь і задавайте питання сюди: @sheremetkaaaa", reply_markup=keyboard)


@dp.message(F.text == "Купити білет")
async def cmd_answer(message: types.Message):
    buttons1 = [
        [
            InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)", callback_data="num_decr")
        ],
        [
            InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_incr")
        ],
        [
            InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
        ],
        [
            InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decь")
        ],
        [
            InlineKeyboardButton(text="На фільм Шалений Макс: Дорога гніву (170 грн)", callback_data="num_decа")
        ],
        [
            InlineKeyboardButton(text="На фільм У центрі уваги (190 грн)", callback_data="num_decі")
        ],
        [
            InlineKeyboardButton(text="На фільм Аутсайдери (150 грн)", callback_data="num_decш")
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)

    await message.answer(
        "Оберіть фільм, на який ви хочете придбати квиток",
        reply_markup=keyboard)


@dp.callback_query(F.data == "num_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 230:

        number -= 230
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей")


@dp.callback_query(F.data == "num_incr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 200:

        number -= 200
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer(
            "Ви купили білет на фільм Паразити за 200 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "num_decе")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 210:

        number -= 210
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм Недоторканні за 210 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "num_decь")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 220:

        number -= 220
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм Найкращий стрілець: Маверік за 220 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "num_decа")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 170:

        number -= 1700
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм Шалений Макс: Дорога гніву за 170 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "num_decі")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 190:

        number -= 190
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм У центрі уваги за 190 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "num_decш")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 150:

        number -= 150
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили білет на фільм на фільм Аутсайдери за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.message(F.text == "Адреси наших кінотеатрів")
async def cmd_answer(message: types.Message):
    await message.answer("""
Наші кінотеатри знаходяться за адресами:
вул. Пушкіна 13
вул. Кільцева 9б
вул. Новорічна 48
вул. Сумська 230
проспект Героїв Харкова 86
Чекаємо саме на вас!
""")


@dp.message(F.text == "Афіша кіно на сьогодні")
async def cmd_answer(message: types.Message):
    await message.answer("""
Інтерстеллар - 14:20
Паразити - 15:20
Недоторканні - 18:30
Найкращий  стрілець: Маверік - 17:40
Шалений Макс: Дорога гніву - 20:00
У центрі уваги - 16:40
Аутсайдери - 21:30
""")


@dp.message(F.text == "Розробники цього бота")
async def cmd_answer(message: types.Message):
    await message.answer("Рома, Саша")


@dp.message(F.text == "Підтримати розробників бота")
async def cmd_answer(message: types.Message):
    await message.answer("""
5168752021570554 або 5168755906406224
(на покушать)
""")


@dp.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Це стікер! Будь ласка, виберіть якусь функцію з меню можливих варіантів.")


@dp.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Це GIF, я таке не сприймаю:(")


@dp.message(F.video)
async def message_with_video(message: Message):
    await message.answer("""
Це відео! Замість цього відео, ви можете скористатися функцією з меню, а я зможу вас погрузити у світ кіно!
Дозвольте мені допомогти вам розширити ваш кіно-досвід)
""")


@dp.message(F.photo)
async def message_with_sticker(message: Message):
    await message.answer("Дуже красива фотографія) Але якщо ви хочете користуватись ботом на тему кіно, то будь ласка, виберіть якусь функцію з меню можливих варіантів.")


@dp.message(F.text == "Попкорн та його вартість")
async def cmd_answer(message: types.Message):
    await message.answer("""
Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
З беконом маленький - 70грн    середній - 120грн    великий - 180грн\n
Сирний маленький - 65грн    середній - 100грн    великий - 170грн\n
Шоколадний маленький - 75грн    середній - 105грн    великий - 165грн
""")


@dp.message(F.text == "Напої та їх вартість")
async def cmd_answer(message: types.Message):
    await message.answer("""
Пепсі: 0.3л - 25грн    0.4л - 35грн    0.5л - 50грн\n
Фанта: 0.3л - 25грн    0.4л - 40грн    0.5л - 55грн\n
Спрайт: 0.3л - 30грн    0.4л - 40грн    0.5л - 60грн\n
Вода негазована: 0.5л - 40грн    1л - 70грн\n
Вода газована: 0.5л - 45грн    1л - 75грн
""")


@dp.message(F.text == "Купити напій")
async def cmd_answer(message: types.Message):
    buttons2 = [
        [
            InlineKeyboardButton(text="Пепсі 0.3л (25 грн)", callback_data="а")
        ],
        [
            InlineKeyboardButton(text="Пепсі 0.4л (35 грн)", callback_data="б")
        ],
        [
            InlineKeyboardButton(text="Пепсі 0.5л (50 грн)", callback_data="в")
        ],
        [
            InlineKeyboardButton(text="Фанта 0.3л (25 грн)", callback_data="г")
        ],
        [
            InlineKeyboardButton(text="Фанта 0.4л (40 грн)", callback_data="д")
        ],
        [
            InlineKeyboardButton(text="Фанта 0.5л (55 грн)", callback_data="е")
        ],
        [
            InlineKeyboardButton(text="Спрайт 0.3л (30 грн)", callback_data="є")
        ],
        [
            InlineKeyboardButton(text="Спрайт 0.4л (40 грн)", callback_data="ж")
        ],
        [
            InlineKeyboardButton(text="Спрайт 0.5л (60 грн)", callback_data="з")
        ],
        [
            InlineKeyboardButton(text="Вода негазована 0.5л (40 грн)", callback_data="и")
        ],
        [
            InlineKeyboardButton(text="Вода негазована 1л (70 грн)", callback_data="і")
        ],
        [
            InlineKeyboardButton(text="Вода газована 0.5л (45 грн)", callback_data="ї")
        ],
        [
            InlineKeyboardButton(text="Вода газована 1л (75 грн)", callback_data="й")
        ],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

    await message.answer(
        "Виберіть напій, який ви хочете купити",
        reply_markup=kb)


@dp.callback_query(F.data == "а")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 25:

        number -= 25
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили пепсі 0.3л за 25 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "б")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 35:

        number -= 35
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили пепсі 0.4л за 35 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "в")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 50:

        number -= 50
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили пепсі 0.5л за 50 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "г")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 25:

        number -= 25
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили фанту 0.3л за 25 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "д")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 40:

        number -= 40
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили фанту 0.4л за 40 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "е")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 55:

        number -= 55
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили фанту 0.5л за 55 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "є")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 30:

        number -= 30
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили спрайт 0.3л за 30 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "ж")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 40:

        number -= 40
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили спрайт 0.4л за 40 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "з")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 60:

        number -= 60
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили спрайт 0.5л за 60 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "и")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 40:

        number -= 40
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили негазовану воду 0.5л за 40 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "і")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 70:

        number -= 70
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили негазовану воду 1л за 70 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "ї")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 45:

        number -= 45
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили газовану воду 0.5л за 45 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "й")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 75:

        number -= 75
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили газовану воду 1л за 75 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")




@dp.message(F.text == "Купити попкорн")
async def cmd_answer(message: types.Message):
    buttons2 = [
        [
            InlineKeyboardButton(text="карамельний маленький (60 грн)", callback_data="a")
        ],
        [
            InlineKeyboardButton(text="карамельний середній (100 грн)", callback_data="b")
        ],
        [
            InlineKeyboardButton(text="карамельний великий (150 грн)", callback_data="c")
        ],
        [
            InlineKeyboardButton(text="з беконом маленький (70 грн)", callback_data="d")
        ],
        [
            InlineKeyboardButton(text="з беконом середній (120 грн)", callback_data="e")
        ],
        [
            InlineKeyboardButton(text="з беконом великий (180 грн)", callback_data="f")
        ],
        [
            InlineKeyboardButton(text="сирний маленький (65 грн)", callback_data="g")
        ],
        [
            InlineKeyboardButton(text="сирний середній (100 грн)", callback_data="h")
        ],
        [
            InlineKeyboardButton(text="сирний великий (170 грн)", callback_data="i")
        ],
        [
            InlineKeyboardButton(text="шоколадний маленький (75 грн)", callback_data="j")
        ],
        [
            InlineKeyboardButton(text="шоколадний середній (105 грн)", callback_data="k")
        ],
        [
            InlineKeyboardButton(text="шоколадний великий (165 грн)", callback_data="l")
        ],
    ]

    kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

    await message.answer(
        "Виберіть попкорн, який ви хочете купити",
        reply_markup=kb)


@dp.callback_query(F.data == "a")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 60:

        number -= 60
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі за 60 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "b")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 100:

        number -= 100
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили середній попкорн зі смаком карамелі за 100 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "c")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 150:

        number -= 150
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили великий попкорн зі смаком карамелі за 150 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "d")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 70:

        number -= 70
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили маленький попкорн зі смаком бекону за 70 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "e")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 120:

        number -= 120
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили середній попкорн зі смаком бекону за 120 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "f")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 180:

        number -= 180
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили великий попкорн зі смаком бекону за 180 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "g")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 65:

        number -= 65
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили маленький попкорн зі смаком сиру за 65 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "h")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 100:

        number -= 100
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили середній попкорн зі смаком сиру за 100 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "i")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 170:

        number -= 170
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили великий попкорн зі смаком сиру за 170 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "j")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 75:

        number -= 75
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили маленький попкорн зі смаком шоколаду за 75 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "k")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 105:

        number -= 105
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили середній попкорн зі смаком шоколаду за 105 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.callback_query(F.data == "l")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    if number >= 165:

        number -= 165
        file = open("Баланс.txt", 'w')
        file.write(str(number))
        file.close()
        await callback.message.answer("Ви купили великий попкорн зі смаком шоколаду за 165 грн")
    else:
        await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


@dp.message(F.text == "Баланс карти")
async def cmd_answer(message: types.Message):
    file1 = open("Баланс.txt", 'r')
    balans = file1.read()
    await message.answer(f"Ваш баланс зараз - {balans} грн")


@dp.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Мені подобається ваше текстове повідомлення, але цей бот пов'язаний з кіно, тому виберіть щось з меню можливих варіантів.")


@dp.message(Command("start"))
async def send_random_value(message: types.Message):
    with open("result.txt", "a") as file:
        file.write(f"_______________________________\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"ChatID: {message.chat.id}\n")
        file.write(f"Name: {message.chat.first_name}\n")
        file.write(f"Last name: {message.chat.last_name}\n")
        file.write(f"Full name: {message.chat.full_name}\n")
    await message.answer("Hello " + str(message.chat.full_name))



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())