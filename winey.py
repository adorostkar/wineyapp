import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "358433791:AAGovZQX0V8iOa1050MiRGtt2SGTHX4x9Xs"


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def start(bot, update):
    update.message.reply_text('Hello World!')


def hello(bot, update):
    update.message.reply_text(
        'Hello {0}, {1}'.format(update.message.from_user.first_name, update.message.text))


if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '5000'))
    updater = Updater(TOKEN)
    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.bot.setWebhook("https://rocky-tor-62618.herokuapp.com/" + TOKEN)
    updater.idle()
