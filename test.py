print("Hello Word!")
print("你好，王文！")
# print（233333）



a = str(True)
print(type(a))

b = "哈哈哈哈"

xxx = [1,2,3,4,"哈哈","嘻嘻",True,88]
print(xxx)
print(xxx[4])
del xxx[4] # 删除
print(xxx)
xxx[0] = 99999 # 替换
print(xxx)
xxx.insert(0,"李万飞")
print(xxx)
xxx.insert(3,"海贼王")
print(xxx)
xxx.reverse()
print(xxx)
z = xxx.pop(3)
print(z)
print(xxx)
xxxx = []
for i in xxx:
    i = str(i)
    xxxx.append(i)
xxx = xxxx
xxxx.sort() # 按内容排序
print(xxx)

yyy = ["输入","规格","突然","贴图",'贴图"]
a = yyy.count("贴图")
print(a)

xxx

