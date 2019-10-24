# Quotable Bot
Send scheduled random quotes to your Slack channel

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Instructions

1. Deploy this app to Heroku: https://heroku.com/deploy?template=https://github.com/opinionatedsoft/quotable-bot
2. Go to your app's Settings page (`https://dashboard.heroku.com/apps/<quotable-bot>/settings`) and add these Config Vars:
    - Required:
        - SLACK_WEBHOOK - the slack webhook for your channel (here's how to set it up: https://slack.com/intl/en-ph/help/articles/115005265063-incoming-webhooks-for-slack#set-up-incoming-webhooks)
        - SOURCE_FILE_OR_URL - either a randomizer URL (e.g. https://c.xkcd.com/random/comic/) or the path to a text file (e.g. `perlisms.txt` for the perlisms file in this repo, but you can add your own)
    - Optional Config Vars you can set:
        - MESSAGE_PREFIX - text before the quote, defaults to "Here's a random quote from Quotable Bot:"
        - MESSAGE_SUFFIX - text after the quote, defaults to blank
        - MESSAGE_USERNAME - the sender username, defaults to "Quotable Bot",
        - MESSAGE_EMOJI - the sender email, defaults to "`:speech_balloon:`"
3. Set up Heroku's Scheduler addon (verification required, but no charges if this is your only project), and add a job to run `python send_quote.py` on your preferred schedule (e.g. Daily at 1AM UTC).
4. You can also trigger it manually by going to Heroku Dashboard > More > Run console, and then enter `python send_quote.py`.
