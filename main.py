from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
import asyncio
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
bot.parse_mode = ParseMode.HTML

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "<b>Это предложка 99 школы!</b>\n\n"
        "Отправляй сюда что-нибудь интересное и мы постараемся выложить это в основной канал)"
    )

@dp.message(F.chat.type == "private")
async def forward(message: types.Message):
    if message.text:
        await bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"<b>Новое сообщение от подписчика💕</b>\n\n<blockquote>{message.html_text}</blockquote>"
        )
    else:
        await bot.copy_message(
            chat_id=ADMIN_CHAT_ID,
            from_chat_id=message.from_user.id,
            message_id=message.message_id,
            caption="<b>Новое сообщение от подписчика💕</b>"
        )
    await message.answer("Мы приняли твое сообщение✅")

async def main():
    print("Бот 99 школы запущен на Render 24/7!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
