from datetime import datetime
from utils import get_env, verify_env_vars, env_vars, get_env_vars, Telegram, Venmo
from dotenv import load_dotenv

def main(now):
  load_dotenv()  # take environment variables from .env.
  date = now.strftime("%B %d, %Y")
  time = now.strftime("%H:%M%p")
  print(f'🕘 Monthly health check running on {date} at {time}.\n')

  print("🔍 Verifying environment variables...")
  numOfExpected = 3
  envVarsAreDefined = verify_env_vars(env_vars, numOfExpected)

  if envVarsAreDefined:
    print(f'✅ Found all {numOfExpected} environment variables.')

  access_token, chat_id, bot_token = get_env_vars(env_vars)

  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  print("🤑 Verifying Venmo client is working...\n")
  userId = venmo.get_user_id_by_username("Joe-Previte")

  if userId:
    print('✅ Venmo client is working as expected.')
  else:
    print('❌ Failed to get userId using Venmo client.')

  returnedUserId = bool(userId)

  if envVarsAreDefined and returnedUserId:
    message = f"""
      Hello old sport! 👋

      Checking in from your Monthly Venmo script.

      According to my calculations, everything looks in order.
      You money should be requested per usual this month.

      Cheerio!

      — Efron 🤵🏻‍♂️
    """
    telegram.send_message(message)
  elif envVarsAreDefined:
    telegram.send_message("env var defined")
  elif returnedUserId:
    telegram.send_message("user id defined")
  else:
    telegram.send_message('oh no')

# Grab current date and passing in when running function
now = datetime.now()
main(now)
