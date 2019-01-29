
#-----------------示例2-----------
# def myadd(x, y):  #此函数没有访问全局或外部嵌套函数的变量
#     print(x + y)
# print(myadd(100, 200))

# 不可重入函数
# s = 0 
# def myadd(x, y):
#     print(x + y + s) #注：s 为全局变量
# print(myadd(100, 200))  # 300
# s = 10000
# print(myadd(100, 200))  #10300

#----------------示例3----------
# def power2(x):
#     return x ** 2
# for x in map(power2,range(1, 10)):
#     print(x)

# for x in map(pow,[1, 2, 3, 4],(4, 3, 2, 1)):
#     print(x)

# def power(x):
#     return x ** 2
# s = 0
# for x in map(power, range(1, 10)):
#     s += x
# print(s)

# def power2(x):
#     return x ** 3
# s = 0
# for x in map(power2, range(1, 10)):
#     s += x
# print(s)

# s = 0
# for x in map(pow,[1, 2, 3, 4, 5, 6, 7, 8, 9], (9, 8, 7, 6, 5, 4, 3, 2, 1)):
#     s += x 
# print(s)



#-----------示例5--------------
# def isodd(x):
#     return x % 2 == 1
# for x in filter(isodd, range(1, 10)):
#     print(x)

# L = list(filter(lambda x: x % 2 == 0, range(10))):
#     print(L)

# def isprime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# L = list(filter(isprime, range(100)))
# print(L)
# L = [x for x in filter(isprime, range(100))]
# print(L)


# L = [(1, 5), (3, 9), (4, 1), (3, 6), (5, 3)]
# def sencound_value(t):
#     return t[1]
# L2 = sorted(L,key=sencound_value)
# print(L2)

# L3 = sorted(L,key=sencound_value, reverse=True)
# print(L3)

# def mysum(n):
#     if n == 1:
#         return 1
#     s = n + mysum(n - 1)
#     return s
# print(mysum(100))

# def get_age(n):
#     if n == 1:
#         return 10
#     return get_age(n - 1) + 2
# print(get_age(3))
# print(get_age(5))


L = [[3, 5, 8], 10, [[13, 14], 15, 18],20]
