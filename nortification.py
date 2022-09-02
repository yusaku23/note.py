import requests
from bs4 import BeautifulSoup

#普段読んでいるNoteの記事一覧ページをそれぞれ取得
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

#Lineで送信されるメッセージの本文の設定
def message_body():
  url = "https://note.com"
  nortification_text = "⭐️Noteが更新されました！⭐️"
  
  #固定された記事があるか判定し、対応した記事を取得する。
  if data['pinned'] == None:
  　　　　send_line_message(f"\r{nortification_text}\r\r『{data['person'].getText()}』\r\r{data['title'][0].getText()}\r{url + data['links'][0].get('href')}")
  else:
    send_line_message(f"\r{nortification_text}\r\r『{data['person'].getText()}』\r\r{data['title'][1].getText()}\r{url + data['links'][1].get('href')}")
     
#lineNotifyの設定
def send_line_message(nortification_message):
  line_notify_token = 'g8Rp8p1MUCiMQRs4SEsVfgPbqUVo6HB5FtyYWT2dbJW'
  line_notify_api = 'https://notify-api.line.me/api/notify'
  headers = {'Authorization': f'Bearer {line_notify_token}'}
  data = {'message': {notification_message}}
  requests.post(line_notify_api, headers = headers, data = data)    
     
#リンクから必要な情報を取り出し、実行する
def exec():
  data = {}
  for link in blog_link:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    date = soup.find_all('div', class_= "o-timelineFooter__date") 
    
    #記事を書いている人の名前
    data['person'] = soup.find('div', class_= "o-timelineFooter__name")
    
    #記事のタイトル
    data['title'] = soup.find_all('h3', class_= "o-textNote__title")
    
    #その記事が固定されているかの情報
    data['pinned'] = soup.find('div', class_= "o-timelinePinnedNote o-timelineNoteItem__pinned")
    
    #記事のリンク
    data['links'] = soup.find_all('a', class_ = "o-textNote__link a-link")

　　　　　　　　#1時間以内に更新されている記事があれば、メッセージを送信する。
    for element in date:
      if element.text == "1時間前":
        message_body(data)
      else:
        continue

exec()
