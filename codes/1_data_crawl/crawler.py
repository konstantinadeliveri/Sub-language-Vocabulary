#libraries
import wikipedia
import requests
import bs4


wiki_page = 'Agriculture' #change name on each crawl
res=requests.get(f'https://en.wikipedia.org/wiki/{wiki_page}')
wiki=bs4.BeautifulSoup(res.text,"html.parser")

with open(wiki_page+".txt", "w", encoding="utf-8") as f:  #write file with the contained paragraphs
	for i in wiki.select('p'):
		f.write(i.getText())
