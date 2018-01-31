from slackbot.bot import Bot
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import random
import re

@listen_to('assalamualaikum', re.IGNORECASE)
def assalamualaikum(message):
    message.reply('waalaikumsalam', in_thread=True)

    message.react('blush')

@listen_to('afk', re.IGNORECASE)
def afk(message):
    message.reply(random.choice(['Hayo mau kemana???',
                                 'Udah ijin sama bosque???',
                                 'Jangan lama-lama nanti bosque kangen',
                                 'Kerjaan sudah kelar belom???']))

    message.react(random.choice(['ghost',
                                 'thinking_face',
                                 'smirk',
                                 'yum']))

@listen_to('wkw', re.IGNORECASE)
def wkw(message):
    message.reply('Wkwkwkwkw :v :v :v', in_thread=True)

    message.react('joy')

@listen_to('on')
def on(message):
    message.reply('Tumben kerja???')

    message.react('confused')

@listen_to('off', re.IGNORECASE)
def off(message):
    message.reply(random.choice(['Semoga harimu menyenangkan...',
                                 'Jangan lupa isi checkout ya',
                                 'Kerjaan sudah kelar belom???']))

    message.react('hugging_face')

@listen_to('senin', re.IGNORECASE)
def senin(message):
    message.reply('Hari masih senin ayo semangat. Jangan kasih kendor')

    message.react('hugging_face')

@listen_to('bos', re.IGNORECASE)
def bos(message):
    message.reply('Disini aku bosnya :p')

    message.react('ok_hand')

@listen_to('maaf', re.IGNORECASE)
def maaf(message):
    message.reply('Karena bosque baik, maka bosque maafin')

    message.react('kissing_heart')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()