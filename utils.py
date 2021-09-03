import os
from venmo_api import Client, PaymentPrivacy
from notifiers import get_notifier

def get_env(env):
  """
  Verfies that an environment variable exists
  and returns it.

  Exits script if not found.
  """
  if os.getenv(env):
      print(f"✅ {env} is available in the environment.")
      return os.getenv(env)
  else:
      print(f"❌ Can't find {env} in environment.")
      print("   Exiting script. Please add and run again.")
      quit()

env_vars = ["VENMO_ACCESS_TOKEN", "TELEGRAM_CHAT_ID", "TELEGRAM_BOT_TOKEN", "K_FRIEND_ID", "C_FRIEND_ID", "W_FRIEND_ID"]

def verify_env_vars(vars, numOfExpected):
  """
  Verifies the list of vars are defined in the environment.
  """

  availableEnvVars = []

  for var in vars:
    # If it returns the env, which would be True
    # then we know it's available
    if get_env(var):
        availableEnvVars.append(var)

  if len(availableEnvVars) == numOfExpected:
    return True
  else:
    # This will technically never run
    # because if one doesn't exist, then get_env quits
    # but adding here for posterity
    return False

def get_env_vars(vars):
    """
    Returns an array of the vars after getting them
    """

    allVars = []
    for var in vars:
        allVars.append(os.getenv(var))

    return allVars

def get_month(now):
    """
    Returns the current month.
    Example: April
    """

    month = now.strftime("%B")
    return month

class Venmo:
    def __init__(self, access_token):
        self.client = Client(access_token=access_token)

    def get_user_id_by_username(self, username):
        user = self.client.user.get_user_by_username(username=username)
        if (user):
            return user.id
        else:
            print("ERROR: user did not comeback. Check username.")
            return None

    def request_money(self, id, amount, description, callback = None):
        # Returns a boolean: true if successfully requested
        return self.client.payment.request_money(amount, description, id, PaymentPrivacy.PUBLIC, None, callback)

class Telegram:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.client = get_notifier('telegram')

    def send_message(self, message):
        self.client.notify(message=message, token=self.bot_token, chat_id=self.chat_id)
