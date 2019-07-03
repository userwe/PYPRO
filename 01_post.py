# post的from-data格式的请求参数

import requests

url = "http://127.0.0.1:8080/morning/detail/shopping"
# from-data格式的请求
payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"goodsColor\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"goodsStandard\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"orderNumbe\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"goodsId\"\r\n\r\n1\r\n-----011000010111000001101001--"
#请求头
headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'cache-control': "no-cache",
    'postman-token': "2973d21f-f934-6e2c-e22d-74848ee2ba40"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)