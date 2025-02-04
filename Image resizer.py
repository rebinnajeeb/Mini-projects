from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import httpx
from httpx import Timeout
import asyncio

# Adjust the timeout value in the application
TIMEOUT = 30  # Timeout in seconds, you can adjust this as per your requirement

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your bot.')

async def main():
    # Set up the bot with the provided token
    application = Application.builder().token("7204255801:AAHTAG_AYNRAkYFvwgJ72hleO9Eip21dR5Q").build()

    # Add the handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Define the HTTP client with timeout to handle network issues
    async with httpx.AsyncClient(timeout=Timeout(TIMEOUT)) as client:
        # Start polling for messages
        await application.run_polling()

if __name__ == '__main__':
    # Run the main function using asyncio.run() to automatically manage the event loop
    asyncio.run(main())
