import pymysql
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
a = "select * from tbl_admin;"
res = query(a)
print(res)




