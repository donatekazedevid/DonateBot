import os

ENV = os.environ.get("ENV")



class Var(object):
  if ENV:
    API_ID = int(os.environ.get('API_ID'))
    APP_HASH = os.environ.get('API_HASH')
    TOKEN = os.environ.get('TOKEN')
    OWNER_ID = int(os.environ.get('OWNER_ID'))
    DONATE_TEXT = os.environ.get('DONATE_TEXT')

  else:
    API_ID = int("Put you API_ID here (in the String)")
    API_HASH = "Put your API_HASH here (in the String)"
    TOKEN = "Put your Bot Token here (in the String)"
    OWNER_ID = int("Put your Telegram ID here (in the String)")
    DONATE_TEXT = "Put your Donat Text/Message to be repeated here (in the String)"
