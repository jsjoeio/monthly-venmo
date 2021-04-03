# TODOS
# add GitHub Actions workflow every 2 mins
# Get actual people's user ids and store as environment variables
# Run script on actual schedule (check PayPal receipts)
import os

from venmo_api import Client
from dotenv import load_dotenv

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

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
access_token = os.getenv('VENMO_ACCESS_TOKEN')
venmo = Client(access_token=access_token)

def request_money(name, id, amount, description):
  successfullyRequested = venmo.payment.request_money(amount, description, id)
  if successfullyRequested:
    print("Successfully requested " + str(amount) + " for " + description + " from " + name)
  else:
    print("Payment request failed")

def get_user_by_username(name, username):
  user = venmo.user.get_user_by_username(username=username)
  print(name + "'s user id is " + user.id)
  return user.id

id = get_user_by_username("Jordan Mishlove", "Jordan-Mishlove")
print(id)

# request_money("Jordan Mishlove", id, 1.99, "friendship fee")