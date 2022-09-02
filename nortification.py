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

for link in blog_link:
  response = requests.get(link)
  soup = BeautifulSoup(response.content, "html.parser")
  person = soup.find('div', class_= "o-timelineFooter__name")
  date = soup.find_all('div', class_= "o-timelineFooter__date") 
  title = soup.find_all('h3', class_= "o-textNote__title")
  pinned = soup.find('div', class_= "o-timelinePinnedNote o-timelineNoteItem__pinned")
  links = soup.find_all('a', class_ = "o-textNote__link a-link")

def send_line_message(nortification_message):
  line_notify_token = 'g8Rp8p1MUCiMQRs4SEsVfgPbqUVo6HB5FtyYWT2dbJW'
  line_notify_api = 'https://notify-api.line.me/api/notify'
  headers = {'Authorization': f'Bearer {line_notify_token}'}
  data = {'message': {notification_message}}
  requests.post(line_notify_api, headers = headers, data = data)
  
def message_body():
  send_line_message(f"【Noteが更新されました！】\r\r『{person.getText()}』\r\r{title[0].getText()}")
