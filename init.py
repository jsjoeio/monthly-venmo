# TODOS
# Add health-check GitHub run (runs once a week)
# Get actual people's user ids and store as environment variables
# Update CRON to run once a month

from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier

from utils import get_env

load_dotenv()  # take environment variables from .env.

access_token = get_env("VENMO_ACCESS_TOKEN")
chat_id = get_env("TELEGRAM_CHAT_ID")
bot_token = get_env("TELEGRAM_BOT_TOKEN")

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
    message = "Sorry to bother you Mr. Previte, but I have unforunate news. I tried to request $" + amount + " from " + name + " but the payment failed."
    send_telegram_message(message)


def main():
  """
  The main function which initiates the script.
  """
  print("Hello world")


main
# id = get_user_by_username("Jordan Mishlove", "Jordan-Mishlove")
# print(id)

# request_money("Jordan Mishlove", id, 1.99, "friendship fee")