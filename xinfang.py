#coding:utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://channelsales.tao.fang.com/Business/GetMenu.do'
data = {
    'cookie':"global_cookie=48l5r483g7985d4dtbluqwttq3vircso8yx; FangUserType=1; city=www; newhouse_user_guid=73443268-5881-4C97-3329-5E4D9A793679; vh_newhouse=1_1470131292_6623%5B%3A%7C%40%7C%3A%5Df5c0bf949fb3a3656a22c1778ca6d8b8; __utma=147393320.1598416029.1470133321.1478596198.1482394907.9; __utmz=147393320.1482394907.9.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; global_wapandm_cookie=3ai5dgmns1x47dnyr9y9qonyi2zirg21yhf; fangwork=4781f2931b52f4fefd0dae420eb4e03d; oa_token=204403|MyiZrr7A%2Fsp0n83vCvU4lE4VovR6f6YTWWrT0gQW%2B7hP6Y1kgaJ3qg%3D%3D; unique_cookie=U_pvuxypa6nn1yapurzg43owgoq2xizt4vfq2*1; new_zcb=204403|liujiaxun|001a0827d68840579320cc1193c37f1f|0; ASP.NET_SessionId=j5uditqo5zdu4um00vfloi5v; channelsales_username=DbiZ/5+RaZV/VTBD3p2dwgRG4PXwdt6I@7ADC205F94E07C479A048955E1BCC988@89DbiZ/5+RaZV/VTBD3p2dwgRG4PXwdt6I; channelsales_userid=DbiZ/5+RaZV/VTBD3p2dwmTt1fWaYSFm@573D109825BC95C1@89DbiZ/5+RaZV/VTBD3p2dwmTt1fWaYSFm; counttest=a3f9874ef6d8012ae012b47618ea78fb; __ads_session=/NUwLDNH3whBmC4cAgA=",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0"
}
html = requests.get(url,headers = data)
soup = BeautifulSoup(html.content)
title = soup.find_all("li",attrs={"class":"li level1_li"})[7].find_all('a',attrs={'class':"submenu"})
# title = soup.select("li[class='li level1_li cur'] > ul > li > a")
url_list = []
classes = []
for i in title:
    url_list.append('http://channelsales.tao.fang.com/'+i['data-url'])
    classes.append(i.getText())
def getTag(list):
    lists = []
    for i in list:
        try:
            html = requests.get(i, headers=data)
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        soup = BeautifulSoup(html.content)
        tag = soup.find_all('td',attrs={'style':"width:12%;border:solid #ddd; border-width:0px 1px 1px 0px"})
        listss = []
        print tag
        for ii in tag:
            listss.append(ii.getText())
    lists.append(listss)
    return lists

print getTag(url_list)
print classes
print url_list



#拿指标名称  先给出页面的url
# http://channelsales.tao.fang.com/Statistics/Index.html
# for i in title:
#     print i.getText()
# li.li:nth-child(6)