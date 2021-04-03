# TODOS
# Add photo for Efron
# Update CRON to run once a month

from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Telegram

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, k_friend_id, c_friend_id, w_friend_id, j_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": "KRam",
      "id": k_friend_id,
    },
    {
      "name": "Chrissy",
      "id": c_friend_id,
    },
    {
      "name": "Will",
      "id": w_friend_id,
    },
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "Spotify for the month of " + month + "— Sent by Joe's Assistant Efron 🤵🏻‍♂️"
    amount = 3.00
    message = f"""Good news old sport!

I have successfully requested money from {name}.

— Efron 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

    if len(successfulRequests) == expectedRequests:
      print("✅ Ran script successfully and sent " + expectedRequests + " Venmo requests.")
    else:
      print("❌ Something went wrong. Only sent " + successfulRequests + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
