# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: routes.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 02, 2024 21:56
# ---
import requests

cookies = {
    'acw_sc__v2': '6740948fafd4f3eb78f543a648829a67ea60415f',
}

headers = {
    'From-Domain': '51job_web',
    'Referer': 'https://we.51job.com/pc/search?jobArea=040000&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&searchType=2&keywordType=guess_exp_tag6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sign': '058145d5f119efe8be0fc77353219f7a00909a8540e835c15e3d1cc8366120f9',
}

params = {
    'api_key': '51job',
    'timestamp': '1732285583',
    'keyword': '数据分析',
    'searchType': '2',
    'function': '',
    'industry': '',
    'jobArea': '040000',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    'issueDate': '',
    'sortType': '0',
    'pageNum': '1',
    'requestId': '',
    'keywordType': 'guess_exp_tag6',
    'pageSize': '20',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}
response = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies=cookies, headers=headers).json()
print(response)
