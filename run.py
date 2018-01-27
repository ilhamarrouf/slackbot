from slackbot.bot import Bot
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import random
import re

@listen_to('afk', re.IGNORECASE)
def afk(message):
    message.reply(random.choice(['Hayo mau kemana???',
                                 'Udah ijin sama bosque???',
                                 'Jangan lama-lama nanti aku kangen']))

    message.react('kissing_heart')

@listen_to('wkw', re.IGNORECASE)
def wkw(message):
    message.reply('Wkwkwkwkw :v :v :v', in_thread=True)

    message.react('joy')

@listen_to('off', re.IGNORECASE)
def off(message):
    message.reply('Semoga harimu menyenangkan...')

    message.react('hugging_face')

@listen_to('senin', re.IGNORECASE)
def senin(message):
    message.reply('Hari masih senin ayo semangat. Jangan kasih kendor')

    message.react('hugging_face')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()