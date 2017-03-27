#coding:utf-8
import requests
import pandas as pd
from pandas import DataFrame

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
header = {
    'cookie':"user_trace_token=20160630171927-be240288-3ea3-11e6-a41e-5254005c3644; LGUID=20160630171927-be240780-3ea3-11e6-a41e-5254005c3644; JSESSIONID=9B75D0AEAFAB0236DA3D1F215B45EF0E; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dgt8zNr09jzEQnxxrrqQRrVLpILCD3GisZgHdEKhYKoO%26wd%3D%26eqid%3Dff347ecc002172e70000000658d870ba; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1490579651; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1490579655; _ga=GA1.2.718969917.1467278368; LGSID=20170327095407-43a7d210-1290-11e7-a33a-525400f775ce; LGRID=20170327095412-4637d5f1-1290-11e7-9570-5254005c3644; SEARCH_ID=7dda4fae6fcd4cee84e51e219c6180eb",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
}
i = 0
df = DataFrame(columns=[u'adWord', u'appShow', u'approve', u'businessZones', u'city',
       u'companyFullName', u'companyId', u'companyLabelList', u'companyLogo',
       u'companyShortName', u'companySize', u'createTime', u'deliver',
       u'district', u'education', u'explain', u'financeStage', u'firstType',
       u'formatCreateTime', u'gradeDescription', u'imState', u'industryField',
       u'jobNature', u'lastLogin', u'pcShow', u'plus', u'positionAdvantage',
       u'positionId', u'positionLables', u'positionName',
       u'promotionScoreExplain', u'publisherId', u'salary', u'score',
       u'secondType', u'workYear'])
while i <32:
    i+=1
    data = {
        'first':'true',
        'pn':i,
        'kd':'产品经理'
    }
    html = requests.post(url,headers = header,data=data).content
    html_dic = eval(html.replace('true','True').replace('null','None').replace('false','False'))
    jobs_list = html_dic['content']['positionResult']['result']
    df = pd.concat([df,DataFrame(jobs_list,columns=[u'adWord', u'appShow', u'approve', u'businessZones', u'city',
       u'companyFullName', u'companyId', u'companyLabelList', u'companyLogo',
       u'companyShortName', u'companySize', u'createTime', u'deliver',
       u'district', u'education', u'explain', u'financeStage', u'firstType',
       u'formatCreateTime', u'gradeDescription', u'imState', u'industryField',
       u'jobNature', u'lastLogin', u'pcShow', u'plus', u'positionAdvantage',
       u'positionId', u'positionLables', u'positionName',
       u'promotionScoreExplain', u'publisherId', u'salary', u'score',
       u'secondType', u'workYear'])])

print df.count()