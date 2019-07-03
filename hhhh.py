'''

testv = {'username':'test','password':'123456'}
def add_user(dic):
    e =[]
    for v in dic.values():
        e.append(v)
    print(e)
    return e

if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
    add_user(testv)
    
'''
'''
def add_user(sql):#方法
    for i in sql.values():#用for循环转换为values，只显示值
        v.append(i)#新增，用变量v新增到变量i
    print(v)#v显示值
      #  v = [] cuo
r = {'username':'test','password':'123456'}#定义
v = []#list
#print(v) cuo
add_user(r)#调用
'''


import requests

url = "https://www.baidu.com/"
res = requests.get(url)#发送请求并且获得响应值
#print(res.text)#获取相应信息
#print(res.status_code)    #http状态吗

# 
# #
url = ""# 接口地址
res1 = requests.get(url)
a = res1.json()#解析响应信息为字典，接口是返回值必须是json格式
# print(type(a)) 打印解析后的结果的类型

print(a["success"])
print(a["message"])


