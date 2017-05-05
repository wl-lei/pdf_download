import urllib2,cookielib
import requests
from bs4 import BeautifulSoup
import os
url = 'https://www.waset.org/conference/2016/01/zurich/ICCV/'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#all = soup.select('.selectedPapers')
#all_paper = all.select('a')
#print(all_paper)
for paper in soup.select('.selectedPapers'):
	paper.select('a')
num=len(paper.select('a'))
#print(paper.select('a')[0].text)
title=[]
url_1=[]
r=range(0,num)
#print(paper.select('a')[14].text)
#print(r)
for i in r:
    title.append(paper.select('a')[i].text)
    url_1.append(paper.select('a')[i]['href'])
#print(title)
#print(url_1)
url_pdf=[]
for j in range(0,len(url_1)):
	id = url_1[j].split('/')[-1]
	head = url_1[j].split('/')[-2]
	url_pdf.append('http://waset.org/publications/'+str(id)+'/'+head+'.pdf')
#print(url_pdf)
#site="http://waset.org/publications/10006024/evaluating-factors-influencing-information-quality-in-large-firms.pdf"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}
os.mkdir('ldf_download')
os.chdir(os.path.join(os.getcwd(), 'ldf_download'))
for url_r in url_pdf[:]:
	req = urllib2.Request(url_r, headers=hdr)
	file_name = url_r.split('/')[-1]
	page = urllib2.urlopen(req)
	#print(2)
	#except urllib2.HTTPError, e:
	f = open(file_name, 'wb')
	#print(1)
	block_sz = 8192
	while True:
		buffer = page.read(block_sz)
		if not buffer:
			break

		f.write(buffer)
	f.close()
	print("Sucessful to download" + " " + file_name)
