from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())
#article = soup.find_all('article')
#print(article[0].prettify())
#print(len(article))

csv_file = open('coreyms.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow((['headline','summary','Video_link']))

for article in soup.find_all('article'):
 headline = article.h2.a.text
 print(headline)

 summary = article.find(('div',{"class":'entry-content'})).p.text
 print(summary)

 try:
  video_source = article.find('iframe',{"class":'youtube-player'})['src']
  print(video_source)
  vid_id = video_source.split('/')
  idd= vid_id[4].split('?')
  #print(idd[0])
  yt_link = f'https://youtube.com/watch?v={idd[0]}'
 except Exception as e:
     yt_link = None
 print(yt_link)
 print()
 print()

 csv_writer.writerow([headline,summary,yt_link])

csv_file.close()