import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Вставь сюда токен от @BotFather
BOT_TOKEN = "9176445543:AAHUKj7W6DA1ExsICHlizOXeHt-0H0TXJck"

# Ссылка на твоё веб-приложение (пока заглушка, позже поставишь свою)
WEB_APP_URL = "https://snickround.github.io/SR_Game/"

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        "Привет! Добро пожаловать в <b>SnickRound_Game</b> 🎲\n\n"
        "Мы уже подготовили для тебя стартовый запас монет. Весь движ, игры, "
        "ежедневные кейсы и колесо удачи ждут тебя внутри приложения — "
        "в чате ничего настраивать не нужно.\n\n"
        "Жми кнопку ниже, залетай в <b>SR_Game</b> и забирай свой бонус! 👇"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Играть в SR_Game",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )

    await message.answer(welcome_text, reply_markup=keyboard)


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())