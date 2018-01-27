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

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()