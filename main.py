import datetime
from telegram.ext import Updater, CommandHandler
import requests
import re
import os


TOKEN = os.getenv("TOKEN")
now = datetime.datetime.now()


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def is_image(url):
    allowed_extension = ['jpg', 'jpeg', 'png']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag


def is_animation(url):
    allowed_extension = ['mp4', 'gif']
    flag = False
    for allowed_ext in allowed_extension:
        if url.lower().endswith(allowed_ext):
            flag = True
            return flag
    return flag


def bop(update, context):
    """Send an image or animation, when the command /bop is issued."""
    url = get_url()
    if is_image(url):
        update.message.reply_photo(url)
    elif is_animation(url):
        update.message.reply_animation(url)


def start(update, context):
    """Send a message when the command /start is issued."""
    name = update.message.from_user.first_name
    update.message.reply_text(f'Hey, {name}!')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
