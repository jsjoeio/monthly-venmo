from datetime import datetime
from utils import get_env, verify_env_vars, env_vars, get_env_vars, Telegram, Venmo
from dotenv import load_dotenv

def main(now):
  load_dotenv()
  date = now.strftime("%B %d, %Y")
  time = now.strftime("%H:%M%p")
  print(f'🕘 Monthly health check running on {date} at {time}.\n')

  print("🔍 Verifying environment variables...")
  numOfExpected = 3
  envVarsAreDefined = verify_env_vars(env_vars, numOfExpected)

  if envVarsAreDefined:
    print(f'✅ Found all {numOfExpected} environment variables.\n')
  else:
    print('❌ Failed to verify environment variables.')

  access_token, chat_id, bot_token = get_env_vars(env_vars)

  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  print("🤑 Verifying Venmo client is working...\n")
  userId = venmo.get_user_id_by_username("Jordan-Mishlove")

  if userId:
    print('✅ Venmo client is working as expected.')
  else:
    print('❌ Failed to get userId using Venmo client.')

  returnedUserId = bool(userId)

  if envVarsAreDefined and returnedUserId:
    print('✅ Everything looks good in the health check')
    message = """Hello old sport! 👋

Checking in from your Monthly Venmo script.

According to my calculations, everything looks in order.
You money should be requested per usual this month.

Cheerio!

— Efron 🤵🏻‍♂️
    """
    telegram.send_message(message)
  elif envVarsAreDefined:
    print('❌ Venmo client might not be working. 1/2 checks failed in health script.')
    message = """Oh hello old sport...

As you can tell by the hesitation in my voice (or rather writing...), I don't have great news.

According to my calculations, the environment variables in your Monthly Venmo script are working, but the Venmo client isn't.

If I were smarter, I would fix it myself, but you know, I'm just an assistant. That's beyond my paygrade.

Good luck fixing it!

— Efron 🤵🏻‍♂️
    """
    telegram.send_message(message)
  elif returnedUserId:
    print('❌ Envrionment variables check did not pass. 1/2 checks failed in health script.')
    message = """It's me again, old sport...

As you can tell by the hesitation in my voice (or rather writing), I don't have great news.

According to my calculations, the Venmo client in your Monthly Venmo script is working, but there is a problem with the environment variables.

You know this stuff is beyond my level of expertise. I'll defer to you, sir.

Good luck!

— Efron 🤵🏻‍♂️
    """
    telegram.send_message(message)
  else:
    print('❌ Venmo client and environment variables did not pass. 2/2 checks failed in health script.')
    message = """Oh dear...

I thought the other day was bad, but this is worse.

According to my calculations, the Venmo client and the environment variables are both failing in your Monthly Venmo script.

I have no idea what could be wrong. I promise I didn't break it.

You may want to go to GitHub and take a look.

— Efron 🤵🏻‍♂️
    """
    telegram.send_message(message)

# Grab current date and passing in when running function
now = datetime.now()
main(now)
