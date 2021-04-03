from datetime import datetime
from utils import get_env, verify_env_vars, env_vars
from dotenv import load_dotenv

def main(now):
  load_dotenv()  # take environment variables from .env.
  date = now.strftime("%B %d, %Y")
  time = now.strftime("%H:%M%p")
  print(f'🕘 Monthly health check running on {date} at {time}.')

  print("   Verifying environment variables...")
  numOfExpected = 3
  areDefined = verify_env_vars(env_vars, numOfExpected)

  if areDefined:
    print(f'✅ Found all {numOfExpected} environment variables.')

  # TODO verify venmo API is working

  # TODO send telegram message


# Grab current date and passing in when running function
now = datetime.now()
main(now)