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