# TODOS
# Add Telegram notifications
# Refactor os.getenv into array with loop
# Add health-check GitHub run (runs once a week)
# Get actual people's user ids and store as environment variables
# Update CRON to run once a month
import os

from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier

load_dotenv()  # take environment variables from .env.

if os.getenv('VENMO_ACCESS_TOKEN'):
    print('✅ Venmo access token is available in the environment.')
else:
    print("❌ Can't find VENMO_ACCESS_TOKEN in environment.")
    print("   Exiting script. Please add and run again.")
    quit()

if os.getenv('TELEGRAM_BOT_TOKEN'):
    print('✅ Telegram bot token is available in the environment.')
else:
    print("❌ Can't find TELEGRAM_BOT_TOKEN in environment.")
    print("   Exiting script. Please add and run again.")
    quit()

if os.getenv('TELEGRAM_CHAT_ID'):
    print('✅ Telegram chat id is available in the environment.')
else:
    print("❌ Can't find TELEGRAM_CHAT_ID in environment.")
    print("   Exiting script. Please add and run again.")
    quit()

chat_id = os.getenv('TELEGRAM_CHAT_ID')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
access_token = os.getenv('VENMO_ACCESS_TOKEN')
venmo = Client(access_token=access_token)
telegram = get_notifier('telegram')

def get_user_by_username(name, username):
  user = venmo.user.get_user_by_username(username=username)
  print(name + "'s user id is " + user.id)
  return user.id

def send_telegram_message(message):
  telegram.notify(message=message, token=bot_token, chat_id=chat_id)

def request_money(name, id, amount, description):
  successfullyRequested = venmo.payment.request_money(amount, description, id)
  if successfullyRequested:
    print("Successfully requested " + str(amount) + " for " + description + " from " + name)
    send_telegram_message("Hello Joe! Letting you know that I have successfully requested money from " + name)
  else:
    print("Payment request failed")
    # TODO funny failure comment
    # TODO look into formatting comments and adding emojis

id = get_user_by_username("Jordan Mishlove", "Jordan-Mishlove")
print(id)

# request_money("Jordan Mishlove", id, 1.99, "friendship fee")