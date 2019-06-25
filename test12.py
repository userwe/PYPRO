print("hello word!")

xxx=[1,2,5,"哈哈",True]
bbb={
    "name":"张三",
    "age":"22",
    "sex":"男",
}
print(bbb["age"])
ccc=bbb.copy()
print(ccc)
ddd=ccc.get("name")
print(ccc)
print(ddd)
bbb.clear
