
import asyncio
import logging

from aiogram.handlers import message
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError


session = "check_bot"
api_id = 21251279
api_hash = '40aa5369202c4906ad656ad92a8d8427'
d = []
client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(pattern='Проверка запущена'))
async def handle_message(event):
    # Выводим в консоль данные о текущем пользователе, для проверки
        sender_username =  event.get_sender()

        if sender_username == "Start Checker":
            d.append(message.Message)
            print(d)
        await client.run_until_disconnected()

    # Бот будет запущен пока мы сами не завершим его работ



async def handle_messages_to_send():
       print("pdfr")

async def main():
    await handle_messages_to_send()

    await client.run_until_disconnected()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(
            main()
        )