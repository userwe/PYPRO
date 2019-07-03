# 接口测试的步骤 必须掌握的

# 断言：就是判断，要不就断言通过，代码继续执行；要不失败，代码报错 assert 1 == 2



import pymysql

import requests





def query(sql):

    """

       数据库的查询功能，传入一个sql参数 

    """

    dbinfo = {

        "host": "118.24.29.59",             # 数据库的地址

        "user": "vn",                       # 用户名

        "password": "1qaz!QAZ123",          # 密码

        "db": "lux"                         # 数据库的名字

    }

    db = pymysql.connect(**dbinfo)

    cursor = db.cursor()

    cursor.execute(sql)

    res = cursor.fetchall()

    return res





# 1. 去构造请求

u = "http://118.24.29.59:5000/userLogin/"

d = {"username":"test", "password":"123456", "captcha":"123456"}

res = requests.post(url=u, json=d)



# 2. 断言http响应状态码：目的是为了判断服务器是否可以正常工作

assert res.status_code == 200                  # http响应状态码等于200的时候，服务器接口就是正常的



# 3. 断言响应值：目的是为了判断接口功能是否正常

code = res.json()["code"]

assert code == 200                             # 返回信息的code值等于200的时候，就是登录成功了



# 4. 查询数据库：去判断数据库是否存在这条数据

sql = "select * from tbl_user where username='test' and password='123456'"

db = query(sql)

assert len(db) == 1



print("登录接口测试通过！")