#! /usr/bin/env python
'''
Created on 2018年7月29日

@author: 54564
'''
import requests
from bs4 import BeautifulSoup
import json


#自定义类，用于储存信息。
class inf(object):
    def __init__(self):
        self.name = 'name'
        self.department = 'department'
        self.phonenum='phonenum'
        self.callnum='callnum'
        self.mail='mail'
#对象转字典函数。
    def todict(self):
        return {
            '姓名': self.name,
            '部门':self.department,
            '手机':self.phonenum,
            '电话':self.callnum,
            '邮箱':self.mail
            }
       
#初始化信息
urlf='http://ecampus.shou.edu.cn/web/guest/addressbook?p_p_id=shouAddressList_WAR_shouAddressListportlet&p_p_lifecycle=0&p_p_state=exclusive&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_shouAddressList_WAR_shouAddressListportlet_action=load&_shouAddressList_WAR_shouAddressListportlet_cur='
urlr='&_shouAddressList_WAR_shouAddressListportlet_delta=20'
# url=urlf+'n'+urlr
    
inf=inf() 
#实例化一个信息类
addr_list=[]
#声明一个用于存信息类的列表 
    
#单页爬取函数    
def scr_one(url,s):    
    #发送请求并解析
    response=s.get(url)
    content=(response.text)
    soup = BeautifulSoup(content,'html.parser') 
    sheets = soup.find_all('p')
    #所有p节点放入sheets列表
   
    for i,p in enumerate(sheets):#遍历sheet列表及其枚举下标
        print(p)#输出，给用户一点交互信息
        if i%5==0:
            inf.name=p['title']
        elif i%5==1:
            inf.department=p['title']
        elif i%5==2:
            inf.phonenum=p['title']
        elif i%5==3:
            inf.callnum=p['title']
        else :
            inf.mail=p['title']
            addr_list.append(inf.todict())
    
    return len(sheets)!=0


#循环爬取
def scr_all(s):
    for i in range(1,100):
        url=urlf+str(i)+urlr
        if scr_one(url,s):
            print('共爬取%d页信息'%i)
        else: 
            print('爬取结束')
            break

    with open('address_book.json', 'w') as f:
        #将address list格式化存入文档
        json.dump(addr_list, f, sort_keys=False, ensure_ascii=False, indent=4)

 
