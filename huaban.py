import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://mjrpt.fang.com/OrderStat1/Index?userid=e0c32ae0-0a65-425e-9455-6e0fb709310f&title=1.0%25E9%259D%25A2%25E7%25AD%25BE%25E9%2587%258F&tabCategory=1.0%25E4%25B8%259A%25E5%258A%25A1&dateType=%25E4%25BB%258A%25E6%2597%25A5&city=%25E5%2585%25A8%25E9%2583%25A8'
data = {
    'cookie':"global_cookie=48l5r483g7985d4dtbluqwttq3vircso8yx; FangUserType=1; city=www; newhouse_user_guid=73443268-5881-4C97-3329-5E4D9A793679; vh_newhouse=1_1470131292_6623%5B%3A%7C%40%7C%3A%5Df5c0bf949fb3a3656a22c1778ca6d8b8; __utma=147393320.1598416029.1470133321.1478596198.1482394907.9; __utmz=147393320.1482394907.9.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; global_wapandm_cookie=3ai5dgmns1x47dnyr9y9qonyi2zirg21yhf; fangwork=9bda94814d7db6f3c573cad47aff39d1; oa_token=204403|MyiZrr7A%2Fsp0n83vCvU4lA2V2GvVk%2FRVtB8vw4ZTpWcht8EtUzqMjw%3D%3D; unique_cookie=U_m5kbo98p6uz15v4gr7midi0tq2xizryjry4*4; new_zcb=204403|liujiaxun|319bbfdde6684d49947be8193c0db643|0; .fang=476F79BF40749DD7A465532BAECC67A396F8501511C21D1338FDCFF9079937F65DB07413FFAB9639E75FDF3D557BF66A774DCA4AB6948B029E2984B6E3958C4E7C590FF6BECA70E85556A58B6855AF3B7B6A24771473C0DA46E1221DEDAA84EBF0B55E3B75CDECB2D9C45313F17F380CDF6FC85824CE60E209FBF59C90F6EF701BAC58DBD1AE6536F91A15441F74CE1D0EB378AB1134076E094AE6585EF2D513E620F34E39E1C58950A64BDAE0877BD6662223DFC5D9629695E2B5919D9B2D07C68CC3624846154DD31E741859DD3602713A8483; __ads_session=nPmUGNIw3wjJNqwbAgA=",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0"
}

html = requests.get(url,headers = data)
soup = BeautifulSoup(html.content)
title = soup.find_all('li',attrs={'class':'leftnav-tit'})
def getTitle(soup):
    title = soup.find_all('li', attrs={'class': 'leftnav-tit'})
    lists = []
    for i in title:
        lists.append(i.find('font').getText())
    return lists

def getTag(data):
    set = {}
    for i in getTitle(data):
        tag = soup.find_all('li',attrs={'businesstype':i})
        lists = []
        for ii in tag:
            lists.append(ii['tt'])
        while len(lists)<6:
            lists.append(None)
        print len(lists)
        set[i] = lists
    return set

df = pd.DataFrame(getTag(soup)).T
print df
with open('C:\txt.csv','r'):
    df.to_csv(r'C:\txt.csv')