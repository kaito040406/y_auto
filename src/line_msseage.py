import requests


class y_auto_message:
  acces_url = "https://notify-api.line.me/api/notify"
  def __init__(self, access_token):
    self.__headers = {'Authorization': 'Bearer ' + access_token}
  def sendmessage(self,type):
    if type == "1":
      message = '処理が終了しました'
      payload = {'message': message}
      r = requests.post(y_auto_message.acces_url, headers=self.__headers, params=payload,)

    elif type == "2":
      message = 'エラーが発生しました。\n強制終了します。'
      payload = {'message': message}
      r = requests.post(y_auto_message.acces_url, headers=self.__headers, params=payload,)