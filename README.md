# Quotable Bot
Send scheduled random quotes to your Slack channel

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Instructions

1. Deploy this app to Heroku: https://heroku.com/deploy?template=https://github.com/opinionatedsoft/quotable-bot
2. Go to your app's Settings page (`https://dashboard.heroku.com/apps/<your-app-id>/settings`) and add these Config Vars:
    - **Required variables:**
        - `SLACK_WEBHOOK` - the slack webhook for your channel (here's how to set it up: https://slack.com/intl/en-ph/help/articles/115005265063-incoming-webhooks-for-slack#set-up-incoming-webhooks)
        - `SOURCE_FILE_OR_URL` - either a randomizer URL (e.g. https://c.xkcd.com/random/comic/) or the path to a text file (e.g. `perlisms.txt` for the perlisms file in this repo, but you can add your own)
    - **Optional variables you can set:**
        - `MESSAGE_PREFIX` - text before the quote, defaults to "Here's a random quote from Quotable Bot:"
        - `MESSAGE_SUFFIX` - text after the quote, defaults to blank
        - `MESSAGE_USERNAME` - the sender username, defaults to "Quotable Bot",
        - `MESSAGE_EMOJI` - the sender email, defaults to "`:speech_balloon:`"
3. Set up Heroku's Scheduler addon (https://elements.heroku.com/addons/scheduler, and add a job to run `python send_quote.py` on your preferred schedule (e.g. Daily at 1AM UTC). This requires credit card verification, but typically it won't charge you anything if this is your only project. (It will only consume a few of your free dyno hours.)
4. Extra: You can also trigger the quote-sending manually by going to Heroku Dashboard > More > Run console, and then enter `python send_quote.py`.
