# 接口测试

# 断言就是判断  要不就断言通过  代码继续执行  要不失败  代码报错
import pymysql
import requests

def query(sql):

    dbinfo = {
    "host":"118.24.29.59",
    "user":"vn",
    "password":"1qaz!QAZ123",
    "db":"lux"
    }
    db = pymysql.connect(**dbinfo)

    cursor = db.cursor()

    cursor.execute(sql)

    res = cursor.fetchall()
    
    return res



# 1. 构造请求
u = "http://118.24.29.59:5000/userLogin/"
d = {"username":"test", "password":"test", "captcha":"123456"}
res = requests.post(url=u, json=d)

# 2.断言http响应状态吗。目的是为了判断服务器是否可以正常工作
assert res.status_code == 200

code = res.json()["code"]

assert code == 200


# 4.查询数据库，判断数据库是否存在这条数据
sql = "select * from tbl_user where username='test' and password='123456'"

db = query(sql)

assert len(db) == 1

print("登陆接口测试通过！")




