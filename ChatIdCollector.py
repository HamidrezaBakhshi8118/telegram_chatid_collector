import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, utils
from telethon.errors import RPCError
import os

load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


async def main():
    username = input("Enter username : ").strip()

    async with TelegramClient("telegram_session", API_ID, API_HASH) as client:
        try:
            channel = await client.get_entity(username)
            print("Chat ID:", utils.get_peer_id(channel))
        except (ValueError, RPCError) as error:
            print(f"ERROR :  {error}")


if __name__ == "__main__":
    asyncio.run(main())