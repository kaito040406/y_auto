import os

def get_api_token():
  access_token = os.environ["LINE_TOKEN"]
  return access_token