from os import getenv

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("TOKEN")
dp = Dispatcher()

photo_oqtepa = 'AgACAgIAAxkBAAOzZ_eNonA55DGnmtUFZ0wE6Kb8UhUAAlTvMRuug7lLMw3DXARbJpcBAAMCAANzAAM2BA'

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏢 О компании")],
        [KeyboardButton(text="💼 Вакансии")],
        [KeyboardButton(text="📋 Меню")],
        [KeyboardButton(text="💬 Отзывы и предложения")]
    ],
    resize_keyboard=True
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Главное меню")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

only_back_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo=photo_oqtepa, reply_markup=main_menu)


@dp.message()
async def handle_all(message: Message) -> None:
    text = message.text

    if text == "🏢 О компании":
        await message.answer_photo(
            photo=photo_oqtepa,
            caption='OqTepa Lavash работает на быстрорастущем рынке Республики Узбекистан и ориентирована на удовлетворение растущего спроса рынка.Компания продемонстрировала отличные результаты за последние 10 лет и устойчиво растет за счет основного направления бизнеса: Продукты питания и напитки.Более подробно 👇\nhttps://oqtepalavash.uz'
        )

    elif text == "💼 Вакансии":
        await message.answer("Пока нет открытых вакансий. Спасибо за интерес!")

    elif text == "📋 Меню":
        await message.answer_photo(
            photo=photo_oqtepa,
            reply_markup=menu_keyboard
        )

    elif text == "💬 Отзывы и предложения":
        await message.answer("Пожалуйста, отправьте ваш отзыв или предложение. Мы ценим ваше мнение!",reply_markup=only_back_keyboard)
        return

    elif text == "Назад":
        await message.answer_photo(photo=photo_oqtepa, reply_markup=main_menu)

    elif text == "Главное меню":
        await message.answer_photo(photo=photo_oqtepa, reply_markup=main_menu)

    else:
        await message.answer("Пожалуйста, используйте кнопки меню 👇", reply_markup=main_menu)

async def main() -> None:
    bot = Bot(token=TOKEN, default_bot_properties=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Az1mbek-Xak1mov/Oqtepa-bot.git
git push -u origin main