import datetime
from telegram.ext import Updater, CommandHandler
import requests
import os


TOKEN = os.getenv("TOKEN")
now = datetime.datetime.now()


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(update, context):
    url = get_url()
    if url.endswith('.jpg') or url.endswith('.png'):
        update.message.reply_photo(url)
    elif url.endswith('.mp4'):
        update.message.reply_animation(url)


def start(update, context):
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat_id
    update.message.reply_text('Hi!')



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
