import requests
from bs4 import BeautifulSoup

blog_link = [
    "https://note.com/kira_se/all"
  , "https://note.com/horiday018/all"
  , "https://note.com/tsukishimacoffee/all"
  , "https://note.com/mypro1/all"
  , "https://note.com/manunitact/all"
  , "https://note.com/akisuke0925/all"
  , "https://note.com/hitohira_aka_2/all"
  , "https://note.com/kotyatv/all"
]

def message_body(data):
  url = "https://note.com"
  nortification_text = "⭐️Noteが更新されました！⭐️"
  if data['pinned'] == None:
    send_line_message(f"\r{nortification_text}\r\r『{data['person'].getText()}』\r\r{data['title'][0].getText()}\r{url + data['links'][0].get('href')}")
  else:
    send_line_message(f"\r{nortification_text}\r\r『{data['person'].getText()}』\r\r{data['title'][1].getText()}\r{url + data['links'][1].get('href')}")

def send_line_message(nortification_message):
  line_notify_token = 'g8Rp8p1MUCiMQRs4SEsVfgPbqUVo6HB5FtyYWT2dbJW'
  line_notify_api = 'https://notify-api.line.me/api/notify'
  headers = {'Authorization': f'Bearer {line_notify_token}'}
  data = {'message': {nortification_message}}
  requests.post(line_notify_api, headers = headers, data = data)

def exec():
  data = {}
  for link in blog_link:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    date = soup.find_all('div', class_= "o-timelineFooter__date") 

    data['person'] = soup.find('div', class_= "o-timelineFooter__name")
    data['title'] = soup.find_all('h3', class_= "o-textNote__title")
    data['pinned'] = soup.find('div', class_= "o-timelinePinnedNote o-timelineNoteItem__pinned")
    data['links'] = soup.find_all('a', class_ = "o-textNote__link a-link")

    for element in date:
      if element.text == "1時間前":
        message_body(data)
      else:
        continue

exec()
