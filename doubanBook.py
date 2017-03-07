#coding:utf-8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )




def findbook(url):
    html    =requests.get(url).content
    soup=BeautifulSoup(html)
    pl2=soup.find_all('div',attrs={'class':'pl2'})
    lists=[]
    for i in pl2:
        ii=i.find('a').getText()
        lists.append(ii)
    return lists
def findNext(url2):
    html_next=requests.get(url2).content
    soup_url=BeautifulSoup(html_next)
    nexts=soup_url.find('span',attrs={'class':'next'})
    url_next=nexts.find('a')['href']
    if url_next:
        return url_next
    else:pass

def main():
    with open('book','wb') as fb:
        url=' '
        while url:
            if url!=' ':
                url=findNext(url)
                lists=findbook(url)
                if url:
                    fb.write('\n'.join(lists))
                print url

            elif url==' ':
                url='https://book.douban.com/top250?start=0'
                lists=findbook(url)
                fb.write('\n'.join(lists))
        fb.close()
if __name__ == '__main__':
    main()