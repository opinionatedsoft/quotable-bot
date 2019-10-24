import random
from os import environ as env

import requests


def send_quote():
    source = env['SOURCE_FILE_OR_URL']
    if source.startswith('http'):
        picked = requests.get(source).url
    else:
        picked = random.choice(open(source).readlines())

    text = (
        env.get('MESSAGE_PREFIX', 'Here\'s a random quote from Quotable Bot:') +
        '\n> ' + picked + '\n' +
        env.get('MESSAGE_SUFFIX', '')
    )

    requests.post(
        env['SLACK_WEBHOOK'],
        json={
            'text': text,
            'username': env.get('MESSAGE_USERNAME', 'Quotable Bot'),
            'icon_emoji': env.get('MESSAGE_EMOJI', ':speech_balloon:'),
        },
    )


if __name__ == '__main__':
    send_quote()
