# 示例1：
# def f1():
#     print("f1")

# def f2():
#     print("f2")

# f1, f2 = f2, f1
# f1()


#-------------------------------示例2：
# def f1():
#     print("f1函数被调用")

# def f2():
#     print("f2函数被调用")

# def fx(fn):
#     print(fn)
#     fn()

# fx(f1)
# fx(f2)
# fx(print)
# print("程序结束")

# def myfun(fn):
#     L = [1, 3, 5, 7, 9]
#     return fn(L)

# print(myfun(max))
# print(myfun(min))
# print(myfun(sum))

#------------------------------示例3
# def get_function():
#     s = input("请输入你要做的操作：")
#     if s == '求最大':
#         return max
#     elif s == '求最小':
#         return min
#     elif s == '求和':
#         return sum

# L = [2, 4, 6, 8, 10]
# f = get_function()
# print(f(L))

# def myadd(x, y):
#     return x + y
# def mysud(x, y):
#     return x - y
# def mymul(x, y):
#     return x * y

# def get_func(op):
#     if op == '+' or op == '加':
#         return myadd
#     elif op == '-' or op == '减':
#         return mysud
#     elif op == '*' or op == '乘':
#         return mymul

# def main():
#     while True:
#         s = input("请输入计算公式：")
#         L = s.split(' ')
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_func(L[1])
#         print("结果是：",fn(a,b))
# main()
#----------------------------示例4------------------
# def fn_outer():
#     print("fn_outer 被调用")

#     print("fn_outer 调用结束")

# count = 0 
# def hello(name):
#     print('你好',name)
#     global count
#     count += 1

# hello('小张')
# while True:
#     s = input('请输入姓名：')
#     if not s:
#         break
#     hello(s)
# print("hello函数被调用的次数",count)

# fx = lambda n:(n ** 2 + 1) % 5 == 0
# print(fx(3))
# print(fx(4))

# def mymax(x, y):
#     return x if x > y else y
# print(mymax(100,200))
# print(mymax("ABC","123"))



# mymax = lambda x, y: x if x > y else y
# print(mymax(100,200))
# print(mymax("ABC","123"))

# def fx(f, x, y):
#     print(f(x, y))
# fx((lambda a, b: a + b), 100, 200)
# fx((lambda a, b: a ** b), 3, 4)
#程序直到此处时有几个全局变量

def mysum(x):
    s = 0
    for a in range(1, x+1):
        s += a
    return s
print(mysum(100))


def myfac(n):
    s = 1
    for x in range(1, n + 1):
        s *= x
    return s
print(myfac(5))

def myadd(n):
    s = 0
    for x in range(1, n + 1):
        s += x ** x 
    return s 
print(myadd(3))
