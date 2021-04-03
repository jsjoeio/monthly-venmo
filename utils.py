import os

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

env_vars = ["VENMO_ACCESS_TOKEN", "TELEGRAM_CHAT_ID", "TELEGRAM_BOT_TOKEN"]

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