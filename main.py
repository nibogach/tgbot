from mistralai import Mistral

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from aiogram.types import Message


api_key = "8OKJFW3B6MoN5dprF5Ggj69qaUy0MdNH"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

TOKEN = '8349785164:AAEgfsXXshaXIAKJP7r3pzOgUvnB6m--hb4' # ⁡⁢⁡⁢⁣⁣ПОМЕНЯЙТЕ ТОКЕН БОТА НА ВАШ⁡

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()


# ⁡⁢⁣⁡⁢⁣⁣ОБРАБОТЧИК КОМАНДЫ СТАРТ⁡⁡
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я отвечу на твои вопросы, любимая', parse_mode = 'HTML')


# ⁡⁢⁣⁣ОБРАБОТЧИК ЛЮБОГО ТЕКСТОВОГО СООБЩЕНИЯ⁡
@dp.message(lambda message: message.text)
async def filter_messages(message: Message):
    chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "system",
            "content": "Ты общаешься с моей женой, ее зовут Фрося, ты должен отвечать на все ее вопросы и писать в каждом сообщении комплименты. Здороваться не нужно, если с тобой здороваются без других запросов, то просто здоровайся и отвечай дальше, если не здороваются, то просто отвечай на запрос",
        },
        {
            "role": "user",
            "content": message.text,
        },
    ]
    )
    text = chat_response.choices[0].message.content
    await message.answer(text, parse_mode = "Markdown")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
