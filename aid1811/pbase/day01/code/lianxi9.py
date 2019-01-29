

#def myfun(a, b, c):
#    print("a=",a)
#    print("b=",b)
#    print("c=",c)

#d = {'c':33,'b':22,'a':11}
#myfun(c = d['c'],b = d['b'],a = d['a'])
#myfun(**d)

#def myfun(a, b, c):
#    pass
#myfun(100,*[200,300])

#a = [1, 2, 3]
#b = 200
#def f1(x,y):
#    x = x +[y] 
#f1(a,b)
#print(a)
#print(b)

#def info(name,age='不详',address='不详'):
#    print(name,'今年',age, '岁，住址：',address)

#info("小张")

#def myadd(a =0, b = 0, c = 0, d = 0):
#    s = a + b + c + d
#    return s
#    

#print(myadd(10, 20))
#print(myadd(100, 200, 300))
#print(myadd(1, 2, 3, 4))




#def mysum(*args):
#    s = sum(args)
#    return s

#print(mysum(1, 2))
#print(mysum(1, 2, 3, 4))
#print(mysum(1, 2, 3, 4, 5, 6, 7, 8))


#def mymax(*args):
#    if len(args) == 1:
#        iterable = args[0]
#        zuida = iterable[0]
#       for x in iterable:
#            if x > zuida:
#                zuida = x
#        return zuida
#    elif len(args) > 1:
#        zuida = args[0]
#        for x in args:
#            if x > zuida:
#                zuida = x 
#        return zuida

#print(mymax([6, 8, 5, 3]))
#print(mymax(100,200))
#print(mymax(1, 2, 5, 9, 7))

# def isprime(x):
#     for i in range(2,x):
#         if x % i == 0:
#             print("False")
#             break
#     else:
#         print("True")

# isprime(8)



def prime_m2n(m, n):
    L = []
    for i in range(m, n):
        for x in range(2, i):
            if x % i == 0:
                break
        else:
            L.append(i)
L = prime_m2n(10, 20)
print(L)
        