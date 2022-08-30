import requests
from bs4 import BeautifulSoup
import datetime
import os

date = datetime.datetime.now()

blog_link = [https://note.com/kira_se/n/nd9706317963d,https://note.com/horiday018/all,https://note.com/tsukishimacoffee/all,
https://note.com/mypro1/all,https://note.com/manunitact/all,https://note.com/akisuke0925/all,https://note.com/hitohira_aka_2/all,
https://note.com/kotyatv/all,https://note.linuc.org/all]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

def send_line_message(nortification_message):
  line_notify_token = 'g8Rp8p1MUCiMQRs4SEsVfgPbqUVo6HB5FtyYWT2dbJW'
  line_notify_api = 'https://notify-api.line.me/api/notify'
  headers = {'Authorization': f'Bearer {line_notify_token}'}
  data = {'message': {notification_message}}
  requests.post(line_notify_api, headers = headers, data = data)
  
def message_body():
  send_line_message(f"【Noteが更新されました！】")
