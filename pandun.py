'''
zi = {
    "name":"张三1",
    "age":"28"
}

if zi.get("name") == "张三":
    print("张三的年龄是",zi["张三"])
#elif zi.get("age") == "28":
    #print("这个人的年龄是28")
else:
    print("字典里没有张三！")
'''

#num = 88
#num = 9
num = 11
if num > 100:
    print("这个数字大于10！")
elif num >50:
    print("这个数字大于50！")
elif num > 10:
    print("这个数字大于10！")
else:
    print("这个数字小于10！")


if 11 != 12:
    print("小小！")
else:
    print("大大！")

'''
不等于 ！=
在不在 in / not in
是不是 is / not is
'''
hlist = ["张三","李四","王二"]
if "王二" not in hlist:
    print("在里面")
else:
    print("不在里面")
'''
a = 888
if type(a) is int:
    print ("111")
else:
    print("222")
'''






