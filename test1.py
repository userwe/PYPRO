print(1233)
'''
多行注释
变量 a = 11
赋值

a = str(123) # 强制转换字符窜 
print(type(a)) #print(type(str(a)))
b = "哈哈哈"   # 汉字转换不了
#c = int("233") # 强制转换数字
#c = float(b) 报错
c = float("33.22") # float转换小数       c = bool("true")
print(c+555)
print("c的类型",type(c))
'''
# ture 真
# false 假
#
#
#
#print(1 == 1 or 1 == 2)
xxx = [1,2,3,"哈哈哈",True,88]
#print(xxx)
#print(len(xxx))
#yy =  "11111111111111111111111111"
#print (len(yy))
print (xxx[5])
print(xxx)
del xxx[4] # 删除
print(xxx)
xxx.append("777") # 新增
print(xxx)
xxx.insert(0,"ni") # 指定位置插入
print(xxx)
xxx.reverse() # 按下标倒序
print(xxx)


xxxx = []
for i in xxx:
    i = str (i)
    xxxx.append(i)
xxx = xxxx
xxx.sort() # 按类容排序
print(xxx)


y = ["ff","ew"]
# print(xxx+y)
a = y.count("ff") #count统计
print(a)

#y = [0] = "2153"  不能赋值给文字
#print(y)
t = y.pop(1)# 取走
print(t)
print(y)
print(xxx[1] > xxx[2])