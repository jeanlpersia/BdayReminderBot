import secrets as keys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes\

async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Objeto UPDATE: {update}\n\n')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, check the menu for more info!!')



if __name__ == '__main__':
    application = ApplicationBuilder().token(keys.API_KEY).build()
    start_handler = CommandHandler('start', StartCommand)
    application.add_handler(start_handler)

    application.run_polling()

