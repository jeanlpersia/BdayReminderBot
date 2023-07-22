import keys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes\

async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, check the menu for more info!!')

async def HandleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'dont understand you, please use the command menu to interact with me")




if __name__ == '__main__':
    application = ApplicationBuilder().token(keys.API_KEY).build()
    start_handler = CommandHandler('start', StartCommand)

    #ASSIGNING HANDLERS
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.ALL, HandleMessage))

    #PULLING UPDATES
    application.run_polling()