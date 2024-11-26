from requests import *
import requests
from bs4 import BeautifulSoup
from bs4 import *
import codecs

base_url = 'https://www.xnxx-ru5.com/todays-selection'
catig_file = 'Бесплатное Порно, Секс, Тюб Видео, ХХХ фото, Киски в Порно Фильмах - XnXX-Ru5.COM.html'
log_post_get = 'log_get_post/log_post_get.html'

f = codecs.open(catig_file, "r", 'utf-8')
contents = f.read()
soup = BeautifulSoup(contents, 'html.parser')
li = soup.find_all('a',  attrs={ 'href': True})

progct = []

for A in li:
  c = A['href']
  b= A.text
  if b == ' ' and c == True:
    delete(b)
  progct.append({
    'title':b,
    'url':c

  })

url = []
title = []
list_none = [' ']
index = 0
for progect in progct:
  index += 1
  p = progect['url']
  b = progect['title']
  url.append({
    'url':p})
  title.append( b)
print( 'Найдено катигорий = >>> ',len(progct))

#file = open('catigories/catigories.txt', 'w')
#for progect in progct:
  #pro_str = str(progect) + '\n'
  #file.write(pro_str)

#file.close()
param = { 'Content-Type': 'text/html'}

r= requests.get(base_url, params=param)
print(r.status_code)


for url in title:
    if url == '':
        title.remove(url)
    if url == ' ':
        title.remove(url)
    print(url)
      
    #print(ur)

print(title)
title_file = open('must_be_list/list_title.txt','w', encoding="utf-8", errors='ignore')
for tit in title:
   title_file.write(tit)
   title_file.write('\n')
f.close()
#print(r.text)

#cat_file = open('catigories/catigories.txt','w', encoding="utf-8", errors='ignore')

