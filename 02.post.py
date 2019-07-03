# 传递的参数也是json的
import requests

u = "http://118.24.29.59:5000/userLogin/"
d = {"username":"test", "password":"test", "captcha":"123456"}
res = requests.post(url=u,json=d)
print(res.json())
