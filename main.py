# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote
from multiprocessing.dummy import Pool as ThreadPool
def get_Pronounce(jp_word):
    Pronounce='none'
    url = "http://m.hujiang.com/d/dict_jp_api.ashx?w=%s&type=jc" % quote(jp_word, safe='')
    try:
        answer_json=requests.get(url).json()
    except:
        return Pronounce
    for p in answer_json:
        if p['Pronounce']!=None:
            Pronounce=p['Pronounce']
            break
    print(jp_word,Pronounce)
    return Pronounce
def make(line):
    if line[0]=='（':
        return ''
    a = line.strip().split(',')
    if a[0].find('〜')!=-1:
        return ''
    a.insert(1, get_Pronounce(a[0].strip().split('（')[0].split('/')[0]))
    return a
pool = ThreadPool(processes=10)
with open('qa.txt','w',encoding='utf-8') as qa:
    with open('n1.csv','r',encoding='utf-8') as n1:
        final=pool.map(make,n1.readlines())
        # for line in n1.readlines():
        #     make(line)
        #     a=line.strip().split(',')
        #     print(a)
        #     a.insert(1,get_Pronounce(a[0].strip().split('（')[0].split('/')[0]))
        #     print(a)
        #     qa.write(''.join(a))
        qa.write(''.join(final))


