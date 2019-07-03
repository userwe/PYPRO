print("hello word!")
c = ["张三","男",26,"179cm"]
print(c[0])

r = {
    "name":"张三",
    "sex":"男",
    "age":"26",
    "high":"179cm"
}
print(r)

#r["weight"] = "80kg"
#print(r)

name = r.get("name") # get 取值
sex = r["sex"] # 取值
print(name)
print(sex)

b = r.items() #键值转换为数组
print(b)

#[('name','张三')('sex','男')('age',26)('high','179cm')]

#x = ('name','张三')
#x.append("ggg") #无法修改

b = r.keys() #取走所有key值，转换为数组
print(b)
# dict_keys(['name', 'sex', 'age', 'high'])

print(r)
b = r.popitem() # 随机取走一对值，一般从末尾开始取
print(b)
print(r)

name = r.pop("name")#取走key值里面的东西
print(name)

b = r.values()
print(b)
#dict_values(['男', '26'])


 



