# 遍历

hlist =  ["哈哈","小杜","订单","方法","订单"]
print(hlist)

for i in hlist:
    print(i)

hstr = "dhdjdjd"
for i in hstr:
    print(i)

r = {
    "name":"张三",
    "sex":"男",
    "age":"26",
    "high":"179cm"
}
for i in r:
    print(i) #显示的key

#x = range(100)
#print(list(x))

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,"\t",end="")
    print("")


#print("好好好\t好好好\t好好好\n好好好\n好好好")

s = list(range(1,10))
print(s)

i = 1
while i < 10:
    print("天天")
    i = i+1

# while True:
#   print("天天")
    







