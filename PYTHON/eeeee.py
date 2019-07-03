#for i in range(1,100):
 #   print(i+1)
'''
i = 1
while i <= 100:
    print(i)
    i = i+1
    '''
a = [i for i in range(1,101)]
random.shuffle(a)
print(a)


testv = {
    'username':'test',
    'password':'123456'
}
print(testv)
def add_user(dic):

    l_e =[]
    for v in dic.values():
        l_e.append(v)
    print(l_e)
    return l_e
    