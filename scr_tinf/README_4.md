# README
***
# the Specification of Scr_tinf

***
## Introductinon:
'Scr_tinf' means  scrape teachers information.Scri_tinf,a script writed by python3,expects a student account to login the campus
net and than it will scrape all teachers' contact information in the net.So,you should creat a file named 'formdate' and copy or write your request formdata in form to it before using it.
***
## 使用指南 
>rquirements.txt
环境与依赖：
python3.6
requests包，用于构造会议对象
bs4包，快速批量清洗数据
json包，格式化输出


### 1.方法1
执行mainX.py文件,按提示输入学号与密码,当前目录下得到address_book.json文件。

### 1.方法2
在包里创建'formdate'文件，以如下格式写入数据：
> username:\*\*\*\*\*\*
 
> password:\*\*\*\*\*\*

数据分别为学号及登录密码，其他参数已跟在post的url后。

最后运行mainscraper模块。即可爬取所有通讯录信息,当前目录下得到address_book.json文件。



改动 ：已上传‘formdata’文件，按格式填写用户名密码即可
***
## procedure detail

### module:
#### mainscraper.py:
Used to login the campus net and build session with it.And than which will delivery a session object to and call  scr_all mothod of address_scraper module.
#### address_scraper.py:
The importentest function module of this procedure,realizes the methods to scrape information of all pages (about 90 pages).
#### cutter.py:
A module use to format request information.
***
## realization process:
Mainscraper module calls cutter module to format the information in 'formdata' and instantiats a session object and then uses them to send a post request to a url which is mention in the js file of the campus net.By far a session with all cookies we need have been prepared well.With it you can visit all urls on the campus net.
Through observation the url we want to vist was constrcted in a regular form.So we imitate it's rule to constrcte the urls we need and get them with our session object to gain content. 
Finally,use BeautifullSoup to format content and cleanout them,write in file.
***
## major code:
#### scr_one:used to scrape the information only for a page

```python
def scr_one(url,s): 
    # 发送请求并解析 
    response=s.get(url)
    content=(response.text)
    soup = BeautifulSoup(content,'html.parser') 
    sheets = soup.find_all('p')
    # 所有p节点放入sheets列表

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
```
#### scr_all:scrape all page

```python
def scr_all(s):

    for i in range(1,100):
        url=urlf+str(i)+urlr
        if scr_one(url,s):
            print('共爬取%d页信息'%i)
        else: 
            print('爬取结束')
            break
        
```

#### imitation login


```python
#初始化
formdata=cut('formdata') 
s=requests.Session()


#访问综合服务平台，取得cookies
url='http://uis.shou.edu.cn/cas/login?isLoginService=11&service=http://ecampus.shou.edu.cn/c/portal/login'
s.post(url,formdata)
```






