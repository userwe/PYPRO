import requests

while True:
    url = "http://open.turingapi.com/v1/openapi"  # 接口地址
    headers = {   # 请求头
        "Content-Type": "application/json;charset=UTF-8"
    }
    input_text = input("请输入：")  # 获取聊天的内容
    if input_text == "退出":
        break
    data = {   # 接口的数据
        "input_text":input_text,
        "user_info":{"open_id":"b19b81b2-0ab9-42eb-86f6-8deb464d7d63"},
        "robot_id":"205436"
        }
    res = requests.request("POST",url,headers=headers,json=data)  # 调用接口，获取接口返回值
    result = res.json().get("result")  
    datas = result.get("datas")
    for i in datas:
        print("机器人说：",i["value"])
